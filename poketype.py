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

    def get_attack(self,ptype):
        row = self.get_index(ptype)
        return self.table[row]

    def get_defense(self,ptype):
        col = self.get_index(ptype)
        return [row[col] for row in self.table]

    def score_attack(self,ptype):
        attack = self.get_attack(ptype)
        return sum(attack)

    def score_defense(self,ptype):
        defense = self.get_defense(ptype)
        return -sum(defense)

    def score(self,ptype):
        attack = self.score_attack(ptype)
        defense = self.score_defense(ptype)
        return attack+defense

typechart = TypeChart()
chart = typechart.get_chart()

scores = {t: typechart.score(t) for t in typechart.get_types()}
scorelist = sorted(scores.values(),reverse=True)
typelist = sorted(scores.values(),reverse=True)

for k,v in scores.items():
    i = typelist.index(v)
    typelist[i] = k

tierlist = {typelist[i]: scorelist[i] for i in range(NUM)}
