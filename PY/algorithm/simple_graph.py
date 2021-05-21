# A simple un-direction graph initialized by dict of {(s,d):weight, ..}


class InvalidData(Exception):
    pass

class SimpleGraph(object):
    """A simple un-direction graph initialized by 
             dict as {(s,d):weight, ..} or list as [(s,d,w), ...]
    """
    def __init__(self, edges_data) -> None:
        if type(edges_data) is dict:
            self.edges = edges_data    # {(source, dest):weight, ...}
        elif type(edges_data) is list:
            self.edges = self._edges_list2dict(edges_data)
        self.vertices = {}    # {s1:[(d11,w11), (d12,w12), ..], s2:[(d21,w21), (d22, w22), ..], ..}
        self.gen_graph()
    
    def _edges_list2dict(self, edges_list) -> dict:
        edges_dict = {}
        for s,d,w in edges_list:
            if (s,d) not in edges_dict:
                edges_dict[(s,d)] = w
            else:
                raise InvalidData(f'Duplicate edge data in input {(s,d)}')
        return edges_dict

    def gen_graph(self):
        """ generate self.vertices from self.edges data.
            self.vertices in form of {s1:[(d11,w11), (d12,w12), ..], s2:[(d21,w21), (d22, w22), ..], ..}
        """
        if self.vertices:
            self.vertices = {}    # reset graph data
        for (s, d) , w in self.edges.items():
            if s not in self.vertices:
                self.vertices[s] = [(d, w)]
            else:
                self.vertices[s].append((d, w))
            if d not in self.vertices:
                self.vertices[d] = [(s, w)]
            else:
                self.vertices[d].append((s, w))

    def __str__(self) -> str:
        s = f"{str(self.__class__).split('.')[-1][:-2]}:\n"
        # s += f'edges: {self.edges}\n'
        for v, edges in self.vertices.items():
            s += f'{v}: {edges}\n' 
        return s

    def check_loop(self, v:str=None) -> bool:
        if v:
            return self._check_loop_r(v)
        else:
            for v in self.vertices:
                if self._check_loop_r(v):
                    return True
            return False

    def _check_loop_r(self, v:str, path:list=None, visited:dict=None) -> bool:
        if path == None:
            path = []
        if visited == None:
            visited = dict()
        # if v in path and v not in visited:
        #     return True
        for e, _ in self.vertices[v]:
            if e in path and path[-1] != e and e not in visited:    # Note: for undirectional graph, every 'edge' has 2 a->b, b->a,
                                                                    # so v-e-v should be ommitted in loop-check
                # print(f'v->e {v},{e} found loop path: {path}')
                return True
            if e not in path and e not in visited:
                if self._check_loop_r(e, path+[v], visited):
                    return True
        visited[v] = True
        return False


def test():
    # data for undirectional graph
    print('SimpleGraph 1 (by list)')
    data_ls = [
        ('a', 'b', 3), ('a', 'c', 4), ('a', 'd', 5),  ('a', 'f', 1),
        ('b', 'c', 3), ('b', 'd', 8), ('c', 'd', 6),
        ('b', 'e', 4), ('d', 'e', 3), ('f', 'c', 7)
    ]
    sg1 = SimpleGraph(data_ls)
    print(sg1)

    print('SimpleGraph 2 (by dict)')
    data_dct = {
        ('a', 'b'):3, ('a', 'c'):4, ('a', 'd'):5,  ('a', 'f'):1,
        ('b', 'c'):3, ('b', 'd'):8, ('c', 'd'):6,
        ('b', 'e'):4, ('d', 'e'):3, ('f', 'c'):7
    }
    sg2 = SimpleGraph(data_dct)
    print(sg2)


test()
