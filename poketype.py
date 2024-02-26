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

    def get_chart(self):
        return self.table

    def get_types(self):
        return self.types

    def get_index(self,ptype):
        index = self.types.index(ptype)
        return index

    def get_ptype(self,index):
        ptype = self.types[index]
        return ptype

    def get_matchup(self,ptype):
        col = self.get_index(ptype)
        attack = self.table[col]
        defense = [row[col] for row in self.table]
        return (attack,defense)

    def sum_matchup(self,tup):
        sum0 = sum(tup[0])
        sum1 = -sum(tup[1])
        return (sum0,sum1)

    def score(self,ptype):
        matchup = self.get_matchup(ptype)
        tot = self.sum_matchup(matchup)
        return tot[0]+tot[1]

typechart = TypeChart()
chart = typechart.get_chart()

scores = {t: typechart.score(t) for t in typechart.get_types()}
scorelist = sorted(scores.values(),reverse=True)
typelist = sorted(scores.values(),reverse=True)

for k,v in scores.items():
    i = typelist.index(v)
    typelist[i] = k

tierlist = {typelist[i]: scorelist[i] for i in range(NUM)}
