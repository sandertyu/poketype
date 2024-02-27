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
        ind = self.types.index(ptype)
        return ind

    # table index to pokemon type
    def get_ptype(self,ind):
        ptype = self.types[ind]
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
        # attack type super eff and res, defense type res and super eff
        attsup = []
        attres = []
        defres = []
        defsup = []
        # sort attack/defense super eff/res into lists
        for key,val in ptypeindex.items():
            if row[val] == 0:
                pass
            elif row[val] > 0:
                attsup.append(key)
            else:
                attres.append(key)
            if col[val] == 0:
                pass
            elif col[val] < 0:
                defres.append(key)
            else:
                defsup.append(key)
        return attsup,attres,defres,defsup

chart = TypeChart()
