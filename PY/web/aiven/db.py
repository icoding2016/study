# The database operations

import logging
import psycopg2 
from config import WebMonConfig


class WebMonDB(object):
    def __init__(self) -> None:
        self._dbcfg = None
        self._dbconn = None
        logging.basicConfig(level=logging.INFO)
        self._load_cfg()
        self._prepare_db()      
    
    def _load_cfg(self) -> None:
        self._dbcfg = WebMonConfig().config()['db']

    def _prepare_db(self) -> None:
        """Prepare the webmon database.
           If the database not exit, then create it.
        """ 
        conn = cur = None 
        try:
            if not self._dbconn:
                conn = self._connect(
                    host = self._dbcfg['host'],
                    port = self._dbcfg['port'],
                    user = self._dbcfg['user'],
                    password = self._dbcfg['password'],
                    database = self._dbcfg["database"])
            else:
                conn = self._dbconn
            # create the database if not exist
            if not self._check_db_exist(conn, self._dbcfg["database"]):
                cur = conn.cursor()
                cur.execute(f'CREATE DATABASE {self._dbcfg["database"]};')
                conn.commit()
                logging.info(f'Database {self._dbcfg["database"]} not exist, create now.')
            # create table if not exist
            if not self._check_table_exist(dbconn=conn, table=self._dbcfg["table"]):
                cur = conn.cursor()
                cur.execute(f'CREATE TABLE {self._dbcfg["table"]} (url TEXT, success BOOLEAN, errcode TEXT, rsptime TEXT)')
                conn.commit()
                logging.info(f'Creating table {self._dbcfg["table"]}.')
        except Exception as e:
            logging.exception(f'Database error: {e}')
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def _connect(self, user:str, password:str, host:str=None, port:str='5432', database:str=''):
        """Connect to the database.
        
           The connection is recorded in self._dbconn
        Return: 
          The connection object to the database
        """
        if self._dbconn:
            self._dbconn.close()

        conn_args = f'user={user} password={password}'
        if host:
            conn_args += f' host={host}'
        conn_args += f' port={port}'
        if database:
            conn_args += f' dbname={database}'
        try:
            self._dbconn = psycopg2.connect(conn_args)
            self._dbconn.autocommit = True
            logging.info(f'Database connected')
        except Exception as e:
            logging.exception(f'Database connection error: {e}')
            if self._dbconn:
                self._dbconn.close()
                self._dbconn = None
            raise e
        return self._dbconn

    def _check_table_exist(self, dbconn, table):
        exist = True
        if dbconn:
            try:
                cur = dbconn.cursor()
                cur.execute(f"""SELECT * from information_schema.tables
                            WHERE TABLE_NAME='{table}'""")
                exist = bool(cur.rowcount)
            except Exception as e:
                logging.exception(f'Database check table error: {e}')
                raise e
        return exist

    def _check_db_exist(self, dbconn, db):
        exist = True
        if dbconn:
            try:
                cur = dbconn.cursor()
                cur.execute('SELECT datname FROM pg_database;')
                fetched = cur.fetchall()
                dbs = [rec[0] for rec in fetched]
                if db in dbs:
                    exist = True
                else:
                    exist = False
            except Exception as e:
                logging.exception(f'Database check table error: {e}')
                raise e
        return exist

    def connection(self):
        """Get current connection to the database
           The connection is kept open until explicitly closed by self.disconnect()
           This is for the consideration performance in case of high QPS.
           The class need to take case of the cleanup at del or exit
        """
        if not self._dbconn or self._dbconn.closed:
            self._dbconn = self._connect(
                user = self._dbcfg['user'],
                password = self._dbcfg['password'],
                host = self._dbcfg['host'],
                port = self._dbcfg['port'],
                database = self._dbcfg['database'])
        return self._dbconn

    def disconnect(self) -> None:
        if self._dbconn:
            self._dbconn.close()

    def write(self, rec:dict) -> None:
        """Add a record to webmon_db.webmon_records table.

        Args:
            rec: a dict with website check metrics info.
                {
                    'url':'http://a.url',
                    'success':True,
                    'errcode':0,
                    'resptime':55
                }

        Raise:
            Database operation Exceptions. 
        """
        conn = cur = None
        try:
            conn = self.connection()
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO {self._dbcfg["table"]} VALUES('{rec["url"]}', {rec["success"]}, '{rec["errcode"]}', '{rec["rsptime"]}')""")
            # cur.commit()    # use autocommit
            logging.info(f'Insert into {self._dbcfg["table"]}: ({rec["url"]}, {rec["success"]}, {rec["errcode"]}, {rec["rsptime"]})')
        except Exception as e:
            logging.exception(f'DB error: {e}')
            raise e
        finally:
            if cur:
                cur.close()

    def _cleanup(self) -> None:
        if self._dbconn:
            self._dbconn.close()
    
    def __exit__(self,  exc_type, exc_val, exc_tb):
        self._cleanup()

    def __del__(self):
        self._cleanup()
