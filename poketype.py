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
        self.map = {self.types[i]: i for i in range(NUM)}

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
        eff = self.get_matchup(ptype)
        tot = self.sum_matchup(eff)
        return tot[0]+tot[1]

    def tierlist(self):
        scores = {t: typechart.score(t) for t in typechart.get_types()}
        scorelist = sorted(scores.values(),reverse=True)
        typelist = sorted(scores.values(),reverse=True)
        for key,val in scores.items():
            index = typelist.index(val)
            typelist[index] = key
        tierlist = {typelist[i]: scorelist[i] for i in range(NUM)}
        return tierlist

    '''
    def matchup(self,ptype):
        eff = self.get_matchup(ptype)
        a,d = eff[0],eff[1]
        for x in a:
            if x != 0:
                i = a.index(x)
                attack[i] = self.get_ptype(x)
        for y in d:
            if y != 0:
                i = d.index(y)
                defense[i] = self.get_ptype(y)
        return attack,defense
        '''

typechart = TypeChart()
chart = typechart.get_chart()
