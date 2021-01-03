# Travelling Salesman Problem (TSP) : 
# Given a set of cities and distances between every pair of cities, 
# the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point.
#  
# Note the difference between Hamiltonian Cycle and TSP. 
# The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once. 
# Here we know that Hamiltonian Tour exists (because the graph is complete) and in fact, many such tours exist, the problem is to find a minimum weight Hamiltonian Cycle. 
# 
# The problem is a famous NP-hard problem. There is no polynomial-time known solution for this problem. 


from call_counter import call_counter, show_call_counter


# tsp with duplicates
# This method is DFS 
# T(n!)
@call_counter
def tsp(citygraph:dict, cur_city:str, total:int=0, path:list=None, best:tuple=None)->(int, list):
    first_call = False
    if None == path:
        path = [cur_city]
    if None == best:
        best = tuple()    # (<distance>, <path>)
        first_call = True

    N = len(citygraph)
    if len(path) ==  N:
        total += citygraph.get_distance(path[0], path[-1])
        print(total, path)
        if not best:
            best = (total, path)
        elif total < best[0]:
            best = (total, path)        
        return best

    for neighbor in citygraph.get_neighbors(cur_city):
        if neighbor not in path:
            best = tsp(citygraph, neighbor, total + citygraph.get_distance(cur_city, neighbor), path + [neighbor], best)
    if first_call:
        best[1].append(cur_city)
    return best

def tsp2(citygraph:dict, cur_city:str, total:int=0, path:list=None, best:tuple=None)->(int, list):
    if None == path:
        path = [cur_city]
    if None == best:
        best = tuple()    # (<distance>, <path>)

    N = len(citygraph)
    if len(path) ==  N:
        total += citygraph.get_distance(path[0], path[-1])
        if not best:
            best = (total, path)
        elif total < best[0]:
            best = (total, path)
        print(best)
        return best

    for neighbor in citygraph.get_neighbors(cur_city):
        if neighbor not in path:
            best = tsp(citygraph, neighbor, total + citygraph.get_distance(cur_city, neighbor), path + [neighbor], best)
    return best



class CityGraph(object):
    def __init__(self, data:dict=None)->None:
        if not data:
            self._data = dict()
        else:
            self._data = self.refine_city_graph(data)

    def refine_city_graph(self, data:dict)->dict:
        ''' generate complete graph
            return:   {'city1':[('city2', <distance>), ('city3', <distance>)],}
        '''
        cityg = data.copy()
        for c, dsts in data.items():
            for dst,distance in dsts:
                if dst not in cityg:
                    cityg[dst] = [(c, distance)]
                elif c not in [n for n,v in cityg[dst]]:
                    cityg[dst].append((c, distance))
        return cityg

    def get_neighbors(self, city_name:str)->list:
        if city_name in self._data:
            return [n for (n,d) in self._data[city_name]]
        return []

    def get_distance(self, city_from:str, city_to:str)->int:
        if city_from in self._data:
            for name, dist in self._data[city_from]:
                if name == city_to:
                    return dist
        raise Exception()

    def show(self):
        for c, lst in self._data.items():
            print('{}: {}'.format(c, lst))

    def __len__(self):
        return len(self._data)


def init_distance_map(data:dict)->dict:
    '''
        return:   {('a','b'):<distance>), }
    '''
    citym = dict()
    for c, dsts in data.items():
        for dst in dsts:
            if (c, dst[0]) not in citym:
                citym[(c, dst[0])] = dst[1]
            if (dst[0], c) not in citym:
                citym[(dst[0], c)] = dst[1]
    return citym


def test():
    cities = {
        'a':[('b', 10), ('c', 15), ('d', 20)],
        'b':[('c', 35), ('d', 25)],
        'c':[('d', 30)],
    }

    cg = CityGraph(cities)
    cg.show()

    print(tsp(cg,  'a'))
    show_call_counter()

test()

