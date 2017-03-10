# The following are some test strings to pass in to the play_game function.
import random
quiz1 = """
==========Languag=War=======
In  Language War II there is _A_,_B_,_C_,_D_,_E_,_F_  6  language want to raise a game, 
But becase it is in war so there is some limit :
"""

notice1="only 'y' and 'n' is valid input!!!"
country_names_lib = ['Ruby','Python','Go','Java','PHP','Cpp','CSharp','Klingons',
'C','Lisp','Kotlin','Groovy','Scala','Haskell','Delphi','Pascal','COLBOL']

country_name_replacer=['_A_','_B_','_C_','_D_','_E_','_F_']
country_names=[]

def gen_random_countries():
    while len(country_names)<6:
        i=random.randint(0,len(country_names_lib)-1) 
        if(country_names_lib[i]) not in country_names:
            country_names.append(country_names_lib[i])
rule1_desp="( 1 ) in _A_ and _B_  , at least one join the game"       
def rule1(answer):
    if '_A_' not in answer and '_B_' not in answer:
        return False
    return True
rule2_desp="( 2 ) in _A_,_E_,_F_  , 2 of them join the game"
def rule2(answer):
    count = 0 
    if '_A_'  in answer:
        count+=1
    if '_E_'  in answer:
        count+=1
    if '_F_'  in answer:
        count+=1
    return count == 2
rule3_desp="( 3 ) _B_ and _C_ will all join the game ,or they all don't join the game"
def rule3(answer):
    if '_B_' not in answer and '_C_' not in answer:
        return True
    if '_B_'  in answer and '_C_'  in answer:
        return True
    return False
rule4_desp="( 4 ) _A_ and _D_ are enemy , so only on of them will join the game "
def rule4(answer):
    if '_A_'  in answer and '_D_'  in answer:
        return False
    return True
rule5_desp="( 5 ) if _D_ don't join game , _E_ also don't join the game"
def rule5(answer):
    if '_D_' not in answer and '_E_' not in answer:
        return True
rule6_desp="( 6 ) _C_ and _D_ are enemy , only one of them will join the game"
def rule6(answer):
    if '_C_' in answer and '_D_' in answer:
        return False
    return True

rules=[
    rule1_desp,
    rule2_desp,
    rule3_desp,
    rule4_desp,
    rule5_desp,
    rule6_desp
]
rule_methods=[
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6
]
def play_quiz1():
    gen_random_countries()
    print quiz1

    replaces_rules = []
    for rule in rules:
        replaced_rule=rule
        for i in range(0,6):
            replaced_rule=replaced_rule.replace(country_name_replacer[i],country_names[i])
        replaces_rules.append(replaced_rule)
        print replaced_rule
    user_answer=[]
    for i in range(0,6):
        while(True):
            k = raw_input("Will " + country_names[i] +" join the game?(y/n)")
            if (k=='y'):
                user_answer.append(country_name_replacer[i])
                break
            if (k=='n'):
                break
            print notice1 
    error_count=0
    for i in range(0,6):
        if not rule_methods[i](user_answer):
            error_count+=1
            print replaces_rules[i]
    if (error_count==0):
        print 'You Win!'
    else:
        print 'You Failed!'
    
#print 'nameslen:' +str(len(country_names))
#print random.randint(0,len(country_names))
#gen_random_countries()
#print country_names
play_quiz1()
