# To design a distributed hashtable
#
# 
# Key ideas:
#   - hashtable distributed to multiple nodes.
#     the hash-algorithm is on the 'controller', the hash-slots are distributed
#     e.g.   keys --> [hash] --> 100 slots --(10:1 map)-->  10 nodes
#   - Communication between controller/node(s),
#     controller/node-agent 
#     control plane message (nodeid:<id>, opration: add/get/del, data:<key,value>) 
#   - Node management (node add/del/monitor)
#     when node(s) added/deleted, the number of slots change
#     
#   - hashing algorithm
#     consistent hashing -- hash both objects and slots onto the circle, and map the objects to the nearest slot (clock/anti-clockwise)
#        
#     hash table resize/_rebalance:   
# 
#  
#  



from collections import defaultdict
import json
from typing import TypeVar



T = TypeVar('T')


class DhtNode(object):
    def __init__(self, id:str, addr:str) -> None:
        super().__init__()
        self.id = id
        self.addr = addr
        self.objs = []   # [<objid>]



class DHTError(Exception):
    pass

class DHT(object):
    """Distributed Hash Table."""

    CIRCLE_DEGREES = 10  # 360

    def __init__(self) -> None:
        super().__init__()
        self.circle_nodes = defaultdict(int)  # {degree:<nodeid>, }
        self.circle_objs = defaultdict(list)  # {degree:[<objid>,],}
        self._init_nodes()

    def _init_nodes(self) -> None:
        self._nodes = {}
        nodes = {
            'node_010':'10.1.1.10',
            'node_020':'10.1.1.20',
            'node_030':'10.1.1.30',
            'node_040':'10.1.1.40',
        }
        for id, addr in nodes.items():
            self.add_node(id, addr)
        self._sort_circle_nodes()
        

    def _sort_circle_nodes(self) -> None:
        self.circle_nodes = {k:self.circle_nodes[k] for k in sorted(self.circle_nodes)}

    def add_node(self, id:str, addr:str) -> bool:
        if id in self._nodes:
            return False
        self._nodes[id] = DhtNode(id, addr)
        self._circle_add_node(id)
        self._rebalance()
        return True

    def del_node(self, id:str) -> bool:
        if id in self._nodes:
            return False
        self._circle_del_node(id)
        del self._nodes[id]
        self._rebalance()
        return True

    def node_count(self) -> int:
        return len(self._nodes)

    def _circle_add_node(self, id:str) -> None:
        if id not in self._nodes:
            raise DHTError(f'node {id} not exist.')
        degree = self._hash(id)
        self.circle_nodes[degree] = id
        self._sort_circle_nodes()

    def _circle_del_node(self, id:str) -> None:
        if id not in self._nodes:
            raise DHTError(f'node {id} not exist.')
        degree = self._hash(id)
        del self.circle_nodes[degree]
        self._sort_circle(self.circle_nodes)

    def _circle_add_obj(self, key:T) -> None:
        degree = self._hash(key)
        if key not in self.circle_objs[degree]:
            self.circle_objs[degree].append((key, self._key_to_node(key)))

    def _circle_del_obj(self, key:T) -> None:
        degree = self._hash(key)
        if key in self.circle_objs[degree]:
            del self.circle_objs[degree]

    def _hash(self, key:T, slot_num:int=0) -> int:
        """Basic hash algorithm to get the slot index from the key."""
        if not slot_num:
            slot_num = DHT.CIRCLE_DEGREES
        index = 0
        if isinstance(key, int):
            return key % slot_num
        s = ''
        if not isinstance(key, str):
            s = json.dumps(key)
        else:
            s = key
        count = 0
        for c in s:
            count += ord(c)
        return count % slot_num

    def _key_to_node(self, key:T) -> int:
        """Consistent Hash from key to a node id.
           The id is for a distributed DHT node.
           The algorithm calculate the hash(key) which is the degree on the circle,
           then find the nestest (clockwise) DHT node
        """
        degree = self._hash(key)
        # get_nearest_node
        if len(self.circle_nodes) == 0:
            raise DHTError('No node exist for the DHT.')
        if degree in self.circle_nodes:
            return self.circle_nodes[degree]
        degrees = [d for d in self.circle_nodes]
        if len(degrees) == 1:
            return degrees[0]
        if degree > degrees[-1] or degree < degrees[0]:
            return self.circle_nodes[degrees[0]]
        left, right = degrees[0], degrees[-1]
        while left < right:
            mid = left + (right-left+1)//2    # take the upper round-off
            if degree < mid:
                right = mid
            elif degree > mid:
                left = mid
            else:
                right = mid
                break
        return self.circle_nodes[right]

    def _get_node_objs(self, nodeid:int) -> list:
        if nodeid not in self._nodes:
            return []
        return self._nodes[nodeid].objs[:]


    def _rebalance(self, nodes:list=None):
        """rebalance the mapping when some nodes changes (e.g. added/removed).
        Args:
            nodes: the nodes that is added or removed.  [<id>, ]
                   If None then do the full rebalance.
        """
        # if not nodes:
        #     nodes = [self.circle_nodes[degree] for degree in self.circle_nodes]
        # for node in nodes:
        #     if node not in self.circle_nodes:   # the case of removing node, remap the objs on the node the next node
        #         pass
        # TODO: finish it.
        pass

    def add(self, id:str, obj:T) -> None:
        self._circle_add_obj(id)
        nodeid = self._key_to_node(id)
        self._nodes[nodeid].objs.append(obj)


    def __str__(self):
        s = f'DHT:\n'
        for nodeid in self._nodes:
            s += f'Node_{nodeid} <{self._hash(nodeid)}>: {[o[0] for o in self._get_node_objs(nodeid)]}\n'
        return s




def test():
    data = [
        ('German', 4, 83, 'Industry power', 'Science, engineering, discipline'),
        ('China', 2, 1400, 'Industry power & culture', 'Long continuous history, smart and peaceful nation'),
        ('U.S.A', 1, 330, 'Military + Finance power', 'World Police + Terrorest'),
        ('Russa', 20, 144, 'Military power', 'Tough nation'),
        ('India', 25, 1390, 'Large pupulation and multi nation/culture', 'Dont believe what they say'),
        ('Japan', 8, 126, 'Industry power', 'A branch of Chinese culture developed into a special direction'),
        ('France', 15, 65, 'Culture', 'Food, romance and culture'),
        ('UK', 10, 67, 'Finance and industory legacy', 'Deprecated power'),
        ('Italy', 40, 60, 'Nice food, passionate people lack of discipline'),
        ('<ALIEN>', 0, '?', 'Alien civilization', 'Unknown'),
        ('_', 0, 0, '', ''),
    ]
    dht = DHT()
    for obj in data:
        dht.add(obj[0], obj)
    print(dht)

    dht.add_node('node_050', '10.1.1.50')
    dht.add_node('node_060', '10.1.1.60')
    print(dht)



test()


