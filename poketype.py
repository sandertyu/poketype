#!/usr/bin/ipython -i

TABLE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,.5,0,1,1,.5],
    [1,.5,.5,1,2,2,1,1,1,1,1,2,.5,1,.5,1,2],
    [1,2,.5,1,.5,1,1,1,2,1,1,1,2,1,.5,1,1],
    [1,1,2,.5,.5,1,1,1,0,2,1,1,1,1,.5,1,1],
    [1,.5,2,1,.5,1,1,.5,2,.5,1,.5,2,1,.5,1,.5],
    [1,.5,.5,1,2,.5,1,1,2,2,1,1,1,1,2,1,.5],
    [2,1,1,1,1,2,1,.5,1,.5,.5,.5,2,0,1,2,2],
    [1,1,1,1,2,1,1,.5,.5,1,1,1,.5,.5,1,1,0],
    [1,2,1,2,.5,1,1,2,1,0,1,.5,2,1,1,1,2],
    [1,1,1,.5,2,1,2,1,1,1,1,2,.5,1,1,1,.5],
    [1,1,1,1,1,1,2,2,1,1,.5,1,1,1,1,0,.5],
    [1,.5,1,1,2,1,.5,.5,1,.5,2,1,1,.5,1,2,.5],
    [1,2,1,1,1,2,.5,1,.5,2,1,2,1,1,1,1,.5],
    [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,.5,.5],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,.5],
    [1,1,1,1,1,1,.5,1,1,1,2,1,1,2,1,.5,.5],
    [1,.5,.5,.5,1,2,1,1,1,1,1,1,2,1,1,1,.5],
    ]

'''
TABLE2 = [
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
'''

TYPES = [
    'normal','fire','water','electric','grass','ice','fighting',
    'poison','ground','flying','psychic','bug','rock','ghost',
    'dragon','dark','steel',
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
    def get_multipliers(self,ptype):
        ind = self.get_index(ptype)
        row = self.table[ind]
        col = [x[ind] for x in self.table]
        return (row,col)

    # prettier get_multipliers
    def get_matchup(self,ptype):
        row,col = self.get_multipliers(ptype)
        # {ptype:index}
        ptypeindex = {t: self.get_index(t) for t in self.types}
        # attack type super eff and res, defense type res and super eff
        attpos,attneg,defpos,defneg = [],[],[],[]
        # sort attack/defense super eff/res into lists
        for key,val in ptypeindex.items():
            if row[val] == 1:
                pass
            elif row[val] > 1:
                attpos.append(key)
            else:
                attneg.append(key)
            if col[val] == 1:
                pass
            elif col[val] < 1:
                defpos.append(key)
            else:
                defneg.append(key)
        return attpos,attneg,defpos,defneg

    # sum number of each attack/defend positive/negative matchup
    # (attack positive, attack negative, defend positive, defend negative)
    def get_matchup_sums(self,ptype):
        matchup = self.get_matchup(ptype)
        attpos,attneg,defpos,defneg = matchup[0],matchup[1],matchup[2],matchup[3]
        sums = (len(attpos),-len(attneg),len(defpos),-len(defneg))
        return sums

    # score ptype based on sum of number of positive and negative matchups
    # (attack score, defend score, total score)
    def get_matchup_scores(self,ptype):
        sums = self.get_matchup_sums(ptype)
        scores = (sums[0]+sums[1],sums[2]+sums[3],sum(sums))
        return scores

    # pretty display full ptype matchup, sums and scores
    def get_matchup_summary(self,ptype):
        summary = {'Attack Positive': self.get_matchup(ptype)[0],
                   'Attack Negative': self.get_matchup(ptype)[1],
                   'Defense Positive': self.get_matchup(ptype)[2],
                   'Defense Negative': self.get_matchup(ptype)[3],
                   'Sums': self.get_matchup_sums(ptype),
                   'Scores': self.get_matchup_scores(ptype),}
        return summary

chart = TypeChart()

matchup_tree = {t: chart.get_matchup_summary(t) for t in chart.types}
normal_summary = matchup_tree['normal']
fire_summary = matchup_tree['fire']
water_summary = matchup_tree['water']
electric_summary = matchup_tree['electric']
grass_summary = matchup_tree['grass']
ice_summary = matchup_tree['ice']
fighting_summary = matchup_tree['fighting']
poison_summary = matchup_tree['poison']
ground_summary = matchup_tree['ground']
flying_summary = matchup_tree['flying']
psychic_summary = matchup_tree['psychic']
bug_summary = matchup_tree['bug']
rock_summary = matchup_tree['rock']
ghost_summary = matchup_tree['ghost']
dragon_summary = matchup_tree['dragon']
dark_summary = matchup_tree['dark']
steel_summary = matchup_tree['steel']

# format tierlist {ptype:(balance,score)}
# balances = {ptype:(balance)} , scores = {ptype:score}
def format_tierlist(balances,scores):
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
    balancelist = [balances.get(t) for t in ptypelist]
    # sorted {ptype:(balance,score)}
    tiers = {ptypelist[i]: (*balancelist[i],scorelist[i]) for i in range(NUM)}
    return tiers

# pokemon type tiers by sorted multiplier sum balance and score
def get_tierlist():
    mult = [chart.get_multipliers(t) for t in chart.types]
    mult_sums = [(sum(m[0]),-sum(m[1])) for m in mult]
    # {ptype:(balance)}
    balances = {t: mult_sums[chart.get_index(t)] for t in chart.types}
    # {ptype:score}
    scores = {t: sum(balances[t]) for t in chart.types}
    tiers = format_tierlist(balances,scores)
    return tiers

# sum number of positive matchups vs negative matchups
# treat immunities same as resist
def get_simple_tierlist():
    balances = {t: chart.get_matchup_sums(t) for t in chart.types}
    scores = {t: sum(balances[t]) for t in chart.types}
    tiers = format_tierlist(balances,scores)
    return tiers

tierlist = get_tierlist()
simple_tierlist = get_simple_tierlist()
