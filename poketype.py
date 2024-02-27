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

    def get_matchup_sum(self,tup):
        sum0 = sum(tup[0])
        sum1 = -sum(tup[1])
        return (sum0,sum1)

    def score(self,ptype):
        eff = self.get_matchup(ptype)
        tot = self.get_matchup_sum(eff)
        return tot[0]+tot[1]

    def tierlist(self):
        scores = {t: self.score(t) for t in self.types}
        scorelist = sorted(scores.values(),reverse=True)
        typelist = sorted(scores.values(),reverse=True)
        for key,val in scores.items():
            index = typelist.index(val)
            typelist[index] = key
        tierlist = {typelist[i]: scorelist[i] for i in range(NUM)}
        return tierlist

    def matchup(self,ptype):
        row,col = self.get_matchup(ptype)
        for key,val in self.map.items():
            if row[val] != 0:
                row[val] = key
            if col[val] != 0:
                col[val] = key
        attack = [x for x in row if x != 0]
        defense = [y for y in col if y != 0]
        return attack,defense

typechart = TypeChart()
chart = typechart.table
