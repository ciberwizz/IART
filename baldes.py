from timeit import default_timer as timer
from queue import PriorityQueue


CAPACITY = {'B1':4, 'B2':3}
OBJECTIVE = {'B1':2, 'B2':None}


class Node(object):
        def __init__(self, p = None, op = None, b1 = 0, b2 = 0, cost = 1):
                self.pai = p
                self.oper = op
                self.b1 = b1
                self.b2 = b2
                self.cost = cost

        def __str__(self):
                op = '' if self.oper is None else self.oper
                return 'Node:' + op + ';' + str(self.b1) +';' + str(self.b2)

        def __lt__(self, other):
                return self.cost < other.cost

        def path(self):
                if self.pai is None:
                        return [str(self)]
                else:
                        return [str(self)] + self.pai.path()

        def heuristic_cost(self):
                hcost = 0
                if OBJECTIVE['B1'] != None:
                        hcost += OBJECTIVE['B1'] - self.b1
                if OBJECTIVE['B2'] != None:
                        hcost += OBJECTIVE['B2'] - self.b2
                return hcost

        def acomulated_cost(self):
                if self.pai is None:
                        return self.cost
                else:
                        return self.cost + self.pai.acomulated_cost()
                
                        
                

def test(n):
        if OBJECTIVE['B1'] == n.b1 or OBJECTIVE['B1'] is None:
                if OBJECTIVE['B2'] == n.b2 or OBJECTIVE['B2'] is None:
                        return True
        return False

def repeated(n):
        x = n.pai
        #print('repated n?: ' + str(n))
        while x is not None:
        #       print('father x: ' + str(x))
                if n.b1 == x.b1 and n.b2 == x.b2:
                        return True
                x = x.pai
        return False

def fill_b1(n):
        if n.b1 < CAPACITY['B1']:
                return Node(n,'FILL_B1',CAPACITY['B1'], n.b2, CAPACITY['B1'] - n.b1)
        else:
                return None


def fill_b2(n):
        if n.b2 < CAPACITY['B2']:
                return Node(n,'FILL_B2',n.b1 ,CAPACITY['B2'], CAPACITY['B2'] - n.b2)
        else:
                return None

def drain_b1(n):
        if n.b1 > 0:
                return  Node(n,'DRAIN_B1',0,n.b2,n.b1)
        else:
                return None

def drain_b2(n):
        if n.b1 > 0:
                return  Node(n,'DRAIN_B2',n.b1,0,n.b2)
        else:
                return None

# cost is 1 because none is wasted
def spill_b1_b2(n):
        if n.b1 > 0 and n.b2 < CAPACITY['B2']:
                if n.b1 + n.b2 <= CAPACITY['B2']:
                        return Node(n,'spill_b1_b2',0,n.b1 + n.b2)
                else:
                        return Node(n,'spill_b1_b2',n.b1 + n.b2 - CAPACITY['B2'], CAPACITY['B2'])
        else:
                return None

# cost is 1 because none is wasted
def spill_b2_b1(n):
        if n.b2 > 0 and n.b1 < CAPACITY['B1']:
                if n.b1 + n.b2 <= CAPACITY['B1']:
                        return Node(n,'spill_b2_b1',n.b1 + n.b2,0)
                else:
                        return Node(n,'spill_b2_b1',CAPACITY['B1'], n.b1 + n.b2 - CAPACITY['B1'])
        else:
                return None


def print_nodes(n = []):
        for x in n:
                print( str(x))

def print_correct(cor = []):
        for c in cor:
                x = c.path()
                print(x)


#################

def breath():
        nodes = []
        to_explore = [Node()]
        correct = []

        start = timer()

        while len(to_explore) > 0:
                #print('To explore: ' + str(len(to_explore)))
                nodes.append(to_explore[0])
                if test(to_explore[0]):
                        #print('correct!! ' + str(to_explore[0]))
                        correct.append(to_explore[0])
                else:
                        n = fill_b1(to_explore[0])
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.append(n)

                        n = fill_b2(to_explore[0])
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.append(n)

                        n = drain_b1(to_explore[0])
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.append(n)

                        n = drain_b2(to_explore[0])
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.append(n)

                        n = spill_b1_b2(to_explore[0])
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.append(n)

                        n = spill_b2_b1(to_explore[0])
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.append(n)

#               print('2To explore: ' + str(len(to_explore)))
                del to_explore[0]

        end = timer()


        #print('\ncorrect: ')
        #print_correct(correct)
        #print('number of nodes: ' + str(len(nodes)))
        print('time needed: ' + str(end - start))

###############################

def depth_first():
        correct = []
        nodes = []
        start = timer()
        correct = _depth(Node(),nodes,correct)
        end = timer()


        #print('\ncorrect: ')
        #print_correct(correct)
        print('time needed: ' + str(end - start))

def _depth(current_node, nodes, correct):
        to_explore = []

        nodes += [current_node]

        if test(current_node):
                #print('correct!! ' + str(current_node))
                return [current_node]
        else:
                n = fill_b1(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = fill_b2(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = drain_b1(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = drain_b2(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = spill_b1_b2(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = spill_b2_b1(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

        for node in to_explore:
                correct += _depth(node, nodes, correct)

        return []

##############
# cost is water used
def uniform_cost():
        tree = []
        nodes = []
        to_explore = PriorityQueue()
        to_explore.put((1,Node()))
        correct = []

        start = timer()

        while not to_explore.empty():
                nd = to_explore.get()[1]
                #print('To explore: ' + str(len(to_explore)))
                nodes.append(nd)
                if test(nd):
                        #print('correct!! ' + str(n))
                        correct.append(nd)
                else:
                        n = fill_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.cost,n))

                        n = fill_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.cost,n))

                        n = drain_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.cost,n))

                        n = drain_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.cost,n))

                        n = spill_b1_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.cost,n))

                        n = spill_b2_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.cost,n))

#               print('2To explore: ' + str(len(to_explore)))

        end = timer()


        #print('\ncorrect: ')
        #print_correct(correct)
        #print('number of nodes: ' + str(len(nodes)))
        print('time needed: ' + str(end - start))

################

def progressive_depth():
        correct = []
        start = timer()
        correct = _depth_p(Node(),correct)
        end = timer()


        #print('\ncorrect: ')
        #print_correct(correct)
        print('time needed: ' + str(end - start))

def _depth_p(current_node, correct):
        to_explore = []

        if test(current_node):
                #print('correct!! ' + str(current_node))
                return [current_node]
        else:
                n = fill_b1(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = fill_b2(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = drain_b1(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = drain_b2(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = spill_b1_b2(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

                n = spill_b2_b1(current_node)
                #print(str(n))
                if n != None and not repeated(n):
                        to_explore.append(n)

        for node in to_explore:
                correct += _depth_p(node,correct)

        return []

#################

def gready():
        tree = []
        nodes = []
        to_explore = PriorityQueue()
        to_explore.put((1,Node()))
        correct = []

        start = timer()

        while not to_explore.empty():
                nd = to_explore.get()[1]
                #print('To explore: ' + str(len(to_explore)))
                nodes.append(nd)
                if test(nd):
                        #print('correct!! ' + str(n))
                        correct.append(nd)
                        break
                else:
                        n = fill_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost(),n))

                        n = fill_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost(),n))

                        n = drain_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost(),n))

                        n = drain_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost(),n))

                        n = spill_b1_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost(),n))

                        n = spill_b2_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost(),n))


        end = timer()


        #print('\ncorrect: ')
        #print_correct(correct)
        #print('number of nodes: ' + str(len(nodes)))
        print('time needed: ' + str(end - start))

#################

def a_star():
        tree = []
        nodes = []
        to_explore = PriorityQueue()
        to_explore.put((1,Node()))
        correct = []

        start = timer()

        while not to_explore.empty():
                nd = to_explore.get()[1]
                #print('To explore: ' + str(len(to_explore)))
                nodes.append(nd)
                if test(nd):
                        #print('correct!! ' + str(n))
                        correct.append(nd)
                        break
                else:
                        n = fill_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost() + n.acomulated_cost(),n))

                        n = fill_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost() + n.acomulated_cost(),n))

                        n = drain_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost() + n.acomulated_cost(),n))

                        n = drain_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost() + n.acomulated_cost(),n))

                        n = spill_b1_b2(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost() + n.acomulated_cost(),n))

                        n = spill_b2_b1(nd)
                        #print(str(n))
                        if n != None and not repeated(n):
                                to_explore.put((n.heuristic_cost() + n.acomulated_cost(),n))


        end = timer()


        #print('\ncorrect: ')
        #print_correct(correct)
        #print('number of nodes: ' + str(len(nodes)))
        print('time needed: ' + str(end - start))
        



###########
print('breath:')
breath()
print('depth first:')
depth_first()
print('uniform_cost')
uniform_cost()
print('progressive depth')
progressive_depth()
print('gready')
gready()
print('a_star')
a_star()



