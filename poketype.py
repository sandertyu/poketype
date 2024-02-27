TABLE = [
    [0,0,0,0,0,0,0,0,0,0,0,0,-1,-2,0,0,-1],
    [0,-1,-1,0,1,1,0,0,0,0,0,1,-1,0,-1,0,1],
    [0,1,-1,0,-1,0,0,0,1,0,0,0,1,0,-1,0,0],
    [0,0,1,-1,-1,0,0,0,-2,1,0,0,0,0,-1,0,0],
    [0,-1,1,0,-1,0,0,-1,1,-1,0,-1,1,0,-1,0,-1],
    [0,-1,-1,0,1,-1,0,0,1,1,0,0,0,0,1,0,-1],
    [1,0,0,0,0,1,0,-1,0,-1,-1,-1,1,-2,0,1,1],
    [0,0,0,0,1,0,0,-1,-1,0,0,0,-1,-1,0,0,-2],
    [0,1,0,1,-1,0,0,1,0,-2,0,-1,1,0,0,0,1],
    [0,0,0,-1,1,0,1,0,0,0,0,1,-1,0,0,0,-1],
    [0,0,0,0,0,0,1,1,0,0,-1,0,0,0,0,-2,-1],
    [0,-1,0,0,1,0,-1,-1,0,-1,1,0,0,-1,0,1,-1],
    [0,1,0,0,0,1,-1,0,-1,1,0,1,0,0,0,0,-1],
    [-2,0,0,0,0,0,0,0,0,0,1,0,0,1,0,-1,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,-1],
    [0,0,0,0,0,0,-1,0,0,0,1,0,0,1,0,-1,-1],
    [0,-1,-1,-1,0,1,0,0,0,0,0,0,1,0,0,0,-1],
    ]

TYPES = [
    "normal","fire","water","electric","grass","ice","fighting",
    "poison","ground","flying","psychic","bug","rock","ghost",
    "dragon","dark","steel",
    ]

NUM = len(TYPES)

class TypeChart():

    def __init__(self):
        self.table = TABLE
        self.types = TYPES

    # pokemon type to table index
    def get_index(self,ptype):
        index = self.types.index(ptype)
        return index

    # table index to pokemon type
    def get_ptype(self,index):
        ptype = self.types[index]
        return ptype

    # row and col of table for pokemon type matchup
    def get_matchup(self,ptype):
        ind = self.get_index(ptype)
        row = self.table[ind]
        col = [x[ind] for x in self.table]
        return (row,col)

    # row and column sum balance of pokemon type
    def get_balance(self,tup):
        sum0 = sum(tup[0])
        sum1 = -sum(tup[1])
        return (sum0,sum1)

    # pokemon types by sorted matchup and balance
    def tierlist(self):
        # {ptype:(balance)}
        balances = {t: self.get_balance(self.get_matchup(t))
                for t in self.types}
        # {ptype:score}
        scores = {t: balances[t][0]+balances[t][1] for t in self.types}
        # sort scores values for later
        scorelist = sorted(scores.values(),reverse=True)
        # scorelist to be replaced with ptypes
        ptypelist = sorted(scores.values(),reverse=True)
        # replace ptypelist scores with ptype
        for key,val in scores.items():
            # index of ptypelist score
            ind = ptypelist.index(val)
            ptypelist[ind] = key
        # sorted list of balance
        sumlist = [balances.get(t) for t in ptypelist]
        # sorted {ptype:(balance,score)}
        tier = {ptypelist[i]: (*sumlist[i],scorelist[i]) for i in range(NUM)}
        return tier

    # prettier get_matchup
    def matchup(self,ptype):
        row,col = self.get_matchup(ptype)
        # {ptype:index}
        ptypeindex = {i: self.get_index(i) for i in self.types}
        # replace non-zero row,col with ptype
        for key,val in ptypeindex.items():
            if row[val] != 0:
                row[val] = key
            if col[val] != 0:
                col[val] = key
        # remove non-zeros from ptype row,col
        attack = [x for x in row if x != 0]
        defense = [y for y in col if y != 0]
        return attack,defense

typechart = TypeChart()
chart = typechart.table
