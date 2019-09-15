from lark import Lark, UnexpectedInput
from lark import Transformer
from abaqus_grammar import abaqus_grammar
import abaqus_test

# TODO Transformer
## TODO Node __repr__

### cast away trailing redudancy
### list iterator (filter out Node and list of Nset)

class Coordinate():
    def __init__(self, x, y, z):
        self.coordinate = (x, y, z)
    def __repr__(self):
        (x, y, z) = self.coordinate
        return "<%f, %f, %f>" % (x, y, z)

class Node():
    kind = "Node"
    def __init__(self):
        self.rows = {}
    def add_data(self, index, coordinate):
        self.rows[index] = coordinate
    def __repr__(self):
        return "(NODE)%d" % len(self.rows)

class NSet():
    kind = "NSet"
    def __init__(self):
        self.nset = []
    def add_nset(self, i):
        self.nset.append(i)
    def __repr__(self):
        return "(NSET)%d" % len(self.nset)
        # return str(self.nset)


class AbaqusTransformer(Transformer):
    def list(self, items):
        return items

    def node(self, items):
        n = Node()
        for row in items:
            i = row[0]
            co = row[1]
            n.add_data(i, co)
        return n

    def indexed4fields(self, fields):
        return (fields[0], Coordinate(fields[1], fields[2], fields[3]))

    def floatingpoint(self, fields):
        return float(fields[0])

    def argument (self, (k,v)):
        return k, v

    def nset(self, args):
        nset = NSet()
        print args[0]
        for nums in args[-1]:
            nset.add_nset(nums)
        return nset

    def nsetgenerate(self, args):
        nset = NSet()
        print args[0]
        start = args[-1][0]
        end   = args[-1][1]
        step  = args[-1][2]
        for i in range(start, end + 1, step):
            nset.add_nset(i)
        return nset

    def listnumber (self, args):
        l = []
        for n in args:
            l.append(int(n))
        return l

    index = lambda self, i: int(i[0])

    def elset(self, args):
        return
    def elsetgenerate(self, args):
        return
    def misc(self, args):
        return
    def heading(self, args):
        return
    def shellsection(self, args):
        return
    def value(self, args):
        return
    def instance(self, args):
        return
    def surface(self, args):
        return
    def element(self, args):
        return

abaquas_parser = Lark(abaqus_grammar, parser='lalr')
abaquas_read = abaquas_parser.parse


def main():
    file = open("./testModel1_s8r.inp", "r")
    input = file.read()
    (beforeEA, EA, _) = input.partition("*End Assembly")
    input = beforeEA + EA
    # print input
    result = abaquas_read(input)
    transResult = AbaqusTransformer().transform(result)
    notNone = list(filter(lambda x: x is not None, transResult))
    print((notNone))



    # while True:
    #     try:
    #         file = open("./nlBuckle_test.inp", "r")
    #         input = file.read()
    #         input = input.partition("*End Assembly\n")[0]
    #     except EOFError:
    #         break
    #     print(abaquas_read(input))

def test():
    testString = abaqus_test.testString
    (beforeEA, EA, _) = testString.partition("*End Assembly\n")
    testString = beforeEA + EA
    result = abaquas_read(testString)
    transResult = AbaqusTransformer().transform(result)
    print transResult
    # node = transResult[-3]
    # print(node[3])
    # node = AbaqusTransformer().transform(result)[0]
    # print node.data

if __name__ == '__main__':
    # test()
    main()

# TODO Error Handling
# This goes last for development
class AbaqusInpError(SyntaxError):
    def __str__(self):
        context, line, column = self.args
        return '%s at line %s, columns %s. \n\n%s' % (self.label, line, column, context)

