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

TYPES = [
    'normal','fire','water','electric','grass','ice','fighting',
    'poison','ground','flying','psychic','bug','rock','ghost',
    'dragon','dark','steel',
    ]

class TypeChart:

    def __init__(self):
        self.table = TABLE
        self.types = TYPES
        self.num = len(self.types)

        # {type:index}
        self.type_index = {t: i for i,t in enumerate(self.types)}

    # pokemon type to table index
    def get_index(self,ptype):
        ind = self.type_index[ptype]
        return ind

    # table index to pokemon type
    def get_type(self,ind):
        ptype = self.types[ind]
        return ptype

    # row of type effectiveness multiplier table
    def get_attack(self,ptype):
        ind = self.get_index(ptype)
        row = self.table[ind]
        return row

    # column of type effectiveness multiplier table
    def get_defense(self,ptype):
        ind = self.get_index(ptype)
        col = [x[ind] for x in self.table]
        return col

    # attacking type 2x effective coverage
    def get_attack_double(self,ptype):
        row = self.get_attack(ptype)
        att_doub = []
        for key,val in self.type_index.items():
            if row[val] == 2:
                att_doub.append(key)
            else:
                pass
        return att_doub

    # attacking type 0.5x effective coverage
    def get_attack_half(self,ptype):
        row = self.get_attack(ptype)
        att_half = []
        for key,val in self.type_index.items():
            if row[val] == .5:
                att_half.append(key)
            else:
                pass
        return att_half

    # attacking type 0x effective coverage
    def get_attack_immune(self,ptype):
        row = self.get_attack(ptype)
        att_imun = []
        for key,val in self.type_index.items():
            if row[val] == 0:
                att_imun.append(key)
            else:
                pass
        return att_imun

    # defending type 2x effective weakness
    def get_defense_double(self,ptype):
        col = self.get_defense(ptype)
        def_doub = []
        for key,val in self.type_index.items():
            if col[val] == 2:
                def_doub.append(key)
            else:
                pass
        return def_doub

    # defending type 0.5x effective resistance
    def get_defense_half(self,ptype):
        col = self.get_defense(ptype)
        def_half = []
        for key,val in self.type_index.items():
            if col[val] == .5:
                def_half.append(key)
            else:
                pass
        return def_half

    # defending type 0x effective immunity
    def get_defense_immune(self,ptype):
        col = self.get_defense(ptype)
        def_imun = []
        for key,val in self.type_index.items():
            if col[val] == 0:
                def_imun.append(key)
            else:
                pass
        return def_imun

    # sum number of each attack/defense positive/negative matchup
    # (attack positive, attack negative, defense positive, defense negative)
    def get_matchup_sums(self,ptype):
        att_pos = self.get_attack_double(ptype)
        att_neg = self.get_attack_half(ptype) + self.get_attack_immune(ptype)
        def_pos = self.get_defense_half(ptype) + self.get_defense_immune(ptype)
        def_neg = self.get_defense_double(ptype)
        sums = (len(att_pos),-len(att_neg),len(def_pos),-len(def_neg))
        return sums

    # score type based on sum of number of positive and negative matchups
    # (attack score, defend score, total score)
    def get_matchup_scores(self,ptype):
        sums = self.get_matchup_sums(ptype)
        scores = (sums[0]+sums[1],sums[2]+sums[3],sum(sums))
        return scores

    # pretty display type matchup effectiveness, sums and scores
    def get_matchup_summary(self,ptype):
        summary = {'Attack Double': self.get_attack_double(ptype),
                   'Attack Half': self.get_attack_half(ptype),
                   'Attack Immune': self.get_attack_immune(ptype),
                   'Defense Weak': self.get_defense_double(ptype),
                   'Defense Resist': self.get_defense_half(ptype),
                   'Defense Immune': self.get_defense_immune(ptype),
                   'Matchup Sums': self.get_matchup_sums(ptype),
                   'Matchup Scores': self.get_matchup_scores(ptype),}
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

# type tierlist grouped by score [{score:(ptypes)}]
def format_tierlist(scores):
    # sort scores values for later
    scorelist = sorted(scores.values(),reverse=True)
    # sorted scorelist to [score,ptype]
    for key,val in scores.items():
        ind = scorelist.index(val)
        scorelist[ind] = [val, key]
    compare = [(scorelist[i],scorelist[i+1]) for i in range(chart.num-1)]
    for pair in compare:
        try:
            ind = scorelist.index(pair[0])
        except ValueError:
            pass
        if pair[0][0] == pair[1][0]:
            scorelist[ind].append(pair[1][1])
            scorelist.pop(ind+1)
    tierlist = [{tier[0]: tuple(tier[1:])} for tier in scorelist]
    return tierlist

# pokemon type tiers by sum number of positive vs negative matchups
# treat immunities same as resist, binary ignore neutral
def get_tierlist_binary():
    # {ptype:score}
    scores = {t: chart.get_matchup_scores(t)[2] for t in chart.types}
    tiers = format_tierlist(scores)
    return tiers

# pokemon type tiers by net sum of effectiveness multipliers
# subtract chart.num from sum and make defense negative to center about 0
def get_tierlist_effective():
    mult  = [(chart.get_attack(t),chart.get_defense(t)) for t in chart.types]
    mult_sums = [(sum(m[0])-chart.num,-(sum(m[1])-chart.num)) for m in mult]
    # {ptype:(*sum)}
    sums = {t: mult_sums[chart.get_index(t)] for t in chart.types}
    scores = {t: sum(sums[t]) for t in chart.types}
    # {ptype:score}
    tiers = format_tierlist(scores)
    return tiers

tierlist_binary = get_tierlist_binary()
tierlist_effective = get_tierlist_effective()
