
PUZZLE_LIMIT = [3,3]


class Node(object):
    def __init__(self, pN = None, t = [], oper = None):
        self.pai = None
        self.table = t
        self.oper = oper

        for x in range(PUZZLE_LIMIT[1]):
            self.table.append([0]*PUZZLE_LIMIT[0])


    def __str__(self):
        op = '' if self.oper is None else self.oper
        return 'Node:' + op + ';'  #+ str(self.b1) +';' + str(self.b2)

    def path(self):
        if self.pai is None:
           return [str(self)]
        else:
           return [str(self)] + self.pai.path()


    def move_up(self, from_x, from_y):
        if self.table[from_x,from_y] != 0 and from_y > 0 and self.table[from_x,from_y - 1] == 0:
            n_table = self.table.copy()
            n_table[from_x,from_y - 1] = n_table[frozensetm_x,from_y]
            n_table[from_x,from_y] = 0

            return Node(self,n_table,'UP-' + str(from_x) + ',' + str(from_y))
        else:
            return None

    def move_down(self, from_x, from_y):
        if self.table[from_x,from_y] != 0 and from_y < PUZZLE_LIMIT[1] - 1 and self.table[from_x,from_y + 1] == 0:
            n_table = self.table.copy()
            n_table[from_x,from_y + 1] = n_table[from_x,from_y]
            n_table[from_x,from_y] = 0

            return Node(self,n_table,'DOWN-' + str(from_x) + ',' + str(from_y))
        else:
            return None

    def move_left(self, from_x, from_y):
        if self.table[from_x,from_y] != 0 and from_x > 0 and self.table[from_x - 1,from_y] == 0:
            n_table = self.table.copy()
            n_table[from_x - 1,from_y] = n_table[from_x,from_y]
            n_table[from_x,from_y] = 0

            return Node(self,n_table,'LEFT-' + str(from_x) + ',' + str(from_y))
        else:
            return None

    def move_right(self, from_x, from_y):
        if self.table[from_x,from_y] != 0 and from_x < PUZZLE_LIMIT[0] - 1 and self.table[from_x + 1,from_y] == 0:
            n_table = self.table.copy()
            n_table[from_x + 1,from_y] = n_table[from_x,from_y]
            n_table[from_x,from_y] = 0

            return Node(self,n_table,'RIGHT-' + str(from_x) + ',' + str(from_y))
        else:
            return None    

    def is_goal(self):
        for Y in range(PUZZLE_LIMIT[1]):
            for x in range(PUZZLE_LIMIT[0]):
                if self.table[y][x] != x + (y*PUZZLE_LIMIT[1]):
                    return False
        return True 

    def repeated(self, node):

        if self.pai is None:
            return False

        for i in range(0,PUZZLE_LIMIT[0]):
            for j in range(0,PUZZLE_LIMIT[1]):
                if node.table[i][j] != self.table[i][j]:
                    return self.pai.repeated(node)
        return True


    def all_moves(self, from_x, from_y):
        nodes = []

        x = self.move_up(from_x,from_y)
        if x != None and not self.repeated(x):
            nodes += [x]

        x = self.move_down(from_x,from_y)
        if x != None and not self.repeated(x):
            nodes += [x]

        x = self.move_left(from_x,from_y)
        if x != None and not self.repeated(x):
            nodes += [x]

        x = self.move_right(from_x,from_y)
        if x != None and not self.repeated(x):
            nodes += [x]

        return nodes

    def print_table(self):
        line = ''
        line_break = ' ' + ('-' * 4 * PUZZLE_LIMIT[0])
        for i in range(0,PUZZLE_LIMIT[0]):
            print(line_break)
            line = '| '
            for j in range(0,PUZZLE_LIMIT[1]):
                line += str(self.table[i][j]) + ' | '
            print(line)
            print(line_break)





x = Node()
x.print_table()









