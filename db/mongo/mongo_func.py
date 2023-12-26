#!/usr/bin/python

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import InvalidName

from collections import defaultdict
from datetime import datetime
from functools import lru_cache
import json



class MyMongDb():
    MONGO_CONN_STRING = "mongodb+srv://<account>:<passwd>@<mongodb-connection-string>"

    def __init__(self, conn_str:str = "") -> None:
        self.conn_str = conn_str if conn_str else self.MONGO_CONN_STRING
        self._client = None
        self._db = None             # cache the last used db
        self._col = None            # cache the last used collection
        self._col_cache = {}        # local cache for collections
        self._simple_obj_cache = {} # cache for single obj search
        self._col_indexing = {}
        self.client()
        

    def client(self):
        if self._client:
            return self._client
        try:
            self._client = MongoClient(self.conn_str)
        except Exception as e:
            print("Failed to connect database")
            raise e
        return self._client

    def db(self, db_name: str):
        # assert self._client, "No valid client."
        self._db = self._client[db_name]
        return self._db

    def query(self, db_name:str, col_name:str, filter:str) -> Cursor:
        assert db_name in self._client.list_database_names(), f"Non existing db name {db_name}"
        db = self.db(db_name)
        try:
            col = db[col_name]
            self._col = col
        except InvalidName as e:
            raise e
        return col.find(filter)

    def _dict2tuple(self, d:dict) -> tuple:
        return tuple([(k,v) for k,v in d.items()])
    
    def _tuple2dict(self, t:tuple) -> dict:
        return {k:v for k,v in t}
            
    def get_obj(self, filter:dict, db_name:str="", col_name:str="") -> dict:
        """Get the data by querying a db.collection. """
        @lru_cache    # TODO:  lru_cache doesn't work for inner function
        def _get_obj(filter_t:tuple, db_name:str="", col_name:str=""):
            filter_d = self._tuple2dict(filter_t)
            assert (db_name and col_name) or (not db_name and not col_name), "invalid db_name & col_name combination."
            assert db_name in self._client.list_database_names(), f"Non existing db name {db_name}"
            if col_name:
                assert col_name in self._client[db_name].list_collection_names(), f"Non existing collection {col_name}"
                self._col = self._client[db_name][col_name]
            cur = self._col.find(filter_d)
            data = [d for d in cur]
            # if not data:
            #     raise KeyError("Cannot find document with the uid")
            return data
        return _get_obj(self._dict2tuple(filter), db_name, col_name)

    def simple_get_obj(self, filter:dict, db_name:str, col_name:str) -> dict:
        """A simple version of get obj. 
          Using local collection data cache for bettr performance,
          Only support simple k,v matching with the filter.
        """
        col_name_key = self.db_col_name_key(db_name, col_name)
        cache_key = f"{col_name_key}-{str(filter)}"
        if cache_key in self._simple_obj_cache:
            return self._simple_obj_cache[cache_key]
        
        if col_name_key not in self._col_cache:  # load data to local cache
            self.load_col_to_cache(db_name, col_name)
        
        obj_list = self._col_cache[col_name_key]
        if col_name_key in self._col_indexing:
            for fk in filter.keys():
                if fk in self._col_indexing[col_name_key]:  # local index exist
                    if filter[fk] in self._col_indexing[col_name_key][fk]:
                        obj_list = self._col_indexing[col_name_key][fk][filter[fk]]
                    else:
                        obj_list = []
                    break
        result = self._match_objs(filter, obj_list)
        
        self._simple_obj_cache[cache_key] = result
        return result

    def _match_objs(self, filter:dict, obj_list:list) -> list:
        if not filter:
            return obj_list
        data = []
        for obj in obj_list:
            if all([k in obj and obj[k]==v for k,v in filter.items()]):
                data.append(obj)
        return data

    def db_col_name_key(self, db_name:str, col_name:str) -> str:
        return f"{db_name}-{col_name}"

    def collection_exist(self, db_name:str, col_name:str) -> bool:
        if not db_name or not col_name:
            print(f"db_name & col_name ({db_name}.{col_name}) validation failed.")
            return False
        elif db_name not in self._client.list_database_names():
            print(f"Non existing db name {db_name}")
            return False
        elif col_name not in self._client[db_name].list_collection_names():
            print(f"Non existing collection {col_name}")
            return False
        return True

    def load_col_to_cache(self, db_name:str, col_name:str, override:bool=False):
        """Load the db.collection into local cache.
          If existing in cache, the collection will be reloaded.
        """
        assert self.collection_exist(db_name, col_name), f"collection {db_name}.{col_name} not found."
        col_key = self.db_col_name_key(db_name, col_name)
        if not override and col_key in self._col_cache:
            return
        print(f"Loading {db_name}.{col_name} to cache.")
        self._col = self._client[db_name][col_name]
        cur = self._col.find({})
        self._col_cache[col_key] = [d for d in cur]
        
    def local_indexing(self, db_name:str, col_name:str, field_to_index:str) -> bool:
        """Create an indexing for the local cached collection.
           Only support indexing non-nested field at the momemnt.
           self._col_indexing:
             {<db_col_name_key>:
                {<field_to_index>: {<filed_value>: [<doc_reference>, ], 
                                    ...}
                }
             }
        """
        if not self.collection_exist(db_name, col_name):
            return False
        col_key = self.db_col_name_key(db_name, col_name)
        if col_key not in self._col_cache:
            print(f"collection {self.db_col_name_key(db_name, col_name)} not cached, cannot index locally.")
            return False
        if col_key not in self._col_indexing:
            self._col_indexing[col_key] = {}
        self._col_indexing[col_key][field_to_index] = defaultdict(list)    # clear old index if exist
        for doc in self._col_cache[col_key]:
            if field_to_index in doc:
                self._col_indexing[col_key][field_to_index][doc[field_to_index]].append(doc)

    
    def backup_col(self, db_name:str, col_name:str, keep_origin:bool=True):
        """ Create a _bak collection for the given DB collection. """
        
        if not self.collection_exist(db_name, col_name):
            print("Collection to backup does not exist.. abort.")
            return
        
        client = self.client()
        collection_names = client[db_name].list_collection_names()
        backup_name = f"{col_name}_bak"
        if backup_name in collection_names:
            client[db_name][backup_name].drop()
        if keep_origin:
            self.clone_col(db_name, col_name, backup_name, override=True)
        else:
            client[db_name][col_name].rename(new_name=backup_name)

    
    def save_to_db(self, data:list, db_name:str, col_name:str, backup:bool=True, history:bool=False):
        """ Save the data into DB collection. """
        
        if not data:
            print("Empty data, skip the operation of saving into collection..")
            return
        
        client = self.client()
        collection_names = client[db_name].list_collection_names()
        if col_name in collection_names:
            if backup:    # save the current collection to <col_name>_old
                self.backup_col(db_name, col_name, keep_origin=False)
            else:
                client[db_name][col_name].drop()
        col = client[db_name][col_name]
        col.insert_many(data)
        
        if history:    # keep a copy with timestamp
            ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            col = client[db_name][f"{col_name}_{ts}"]
            col.insert_many(data)
        
    def rename_col(self, db_name:str, org_col_name:str, new_col_name:str, override:bool=False):
        client = self.client()
        if not self.collection_exist(db_name, org_col_name):
            print(f"Failed to rename, the org colllection {org_col_name} not exist.")
            return
        if new_col_name in client[db_name].list_collection_names():
            if not override:
                print(f"new collection {new_col_name} exist, abort.")
                return
            else:
                 client[db_name][new_col_name].drop()
        client[db_name][org_col_name].rename(new_col_name)

    def clone_col(self, db_name:str, org_col_name:str, new_col_name:str, override:bool=False):
        """clone a collection.
           if override == True and the collection with the new_col_name exist, it will be overwritten. 
        """
        client = self.client()
        if not self.collection_exist(db_name, org_col_name):
            print(f"Failed to rename, the org colllection {org_col_name} not exist.")
            return
        if new_col_name in client[db_name].list_collection_names():
            if not override:
                print(f"new collection {new_col_name} exist, abort.")
                return
            else:
                 client[db_name][new_col_name].drop()
        pipeline = [
            {"$match": {}},
            {"$out": f"{new_col_name}"}
        ]
        client[db_name][org_col_name].aggregate(pipeline)


    def save_col_history(self, db_name:str, org_col_name:str, bak_col_name:str="", keep_origin:bool=True):
        t = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_col_name = bak_col_name
        if not backup_col_name:
            backup_col_name = f"{org_col_name}_{t}"
        if keep_origin:
            self.clone_col(db_name,org_col_name, backup_col_name)
        else:
            self.rename_col(db_name, org_col_name, backup_col_name)

    def drop_col(self, db_name:str, col_name:str):
        client = self.client()
        if not self.collection_exist(db_name, col_name):
            print(f"colllection {col_name} not exist, skip..")
        client[db_name][col_name].drop()



def example():   
    smd = SnSMongoDb()
    db_name = "discovery_v2"
    col_src = "tmp_export_mds_report"
    col_output = "tmp_yan_test_db_func"

    filter = {"nat_org_src_ip": '10.39.192.43', "name":"B2B GTM"}
    ret = smd.query(db_name, col_src, filter)
    result = [r for r in ret]  
    for r in result:
        rc = r.copy()
        if "_id" in r:
            rc["_id"] = f"{rc['_id']}"
        sr = json.dumps(rc, indent=4)
        print(sr)
    #
    print("test simple_get_obj")
    data = smd.simple_get_obj(filter, db_name, col_src)
    for r in data:
        rc = r.copy()
        if "_id" in r:
            rc["_id"] = f"{rc['_id']}"
        sr = json.dumps(rc, indent=4)
        print(sr)
    print(f"result match: {data==result}")
    print(f"Writing data ({len(result)} rec) into database: {db_name}.{col_output}...", end=" ")
    smd.save_to_db(result, db_name, col_output, history=True)
    print("done.")

def test_clone(db_name: str, col0: str, col1: str):
    smd = SnSMongoDb()
    print(f"Clone {db_name}.{col0} to {db_name}.{col1}...", end="")
    smd.clone_col(db_name, col0, col1)
    print("done")
    
def test_rename(db_name: str, col0: str, col1: str):
    smd = SnSMongoDb()
    print(f"Rename {db_name}.{col0} to {db_name}.{col1}...", end="")
    smd.rename_col(db_name, col0, col1)
    print("done")
    
def test_backup(db_name: str, col0: str, col1: str, keep_origin: bool):
    smd = SnSMongoDb()
    print(f"Backup {col0} into {col1} (keep_origin={keep_origin})...", end="")
    smd.save_col_history(db_name, col0, col1, keep_origin)
    print("done")
    

def test():
    # example()
    # test_clone("discovery_v2", "tmp_yan_test_db_func", "tmp_yan_test_db_func_clone")
    # test_rename("discovery_v2", "correlate_checkpoint_nat_policy", "correlate_checkpoint_nat_policy_backup20231204")
    # test_rename("discovery_v2", "tmp_correlate_checkpoint_nat_policy_yan_fullsize", "tmp_correlate_checkpoint_nat_policy_yan_fullscope")
    pass


if __name__ == "__main__":
    test()
