import random
from quiz_lib import * 
welcom_message="""\
It's a quize about oppsite word.
 got 5 point first.
if your answer is wrong you ponit will +1(if combo will +2)
if your point is below 0 you will fail.
if the answer is pharse you should connect the word with ' '
eg.
"to free"
"""

level_choose_message="""Input the level to want play.
(1) easy -> you need  achieve 10 point(you got answer).
(2) middle -> you need achieve 20 point.(wrong  will -2 point)
(3) hard -> you need to achieve 30 point.(wrong will -3 point)
"""

level_choose_error_message="level choose error!"

quiz_word_replacer = "_QUIZ_WORD_"
quiz_message="""\
Please give an oppsite word of "_QUIZ_WORD_"
"""

point_replacer = "_POINT_"
combo_replacer = "_COMBO_"
quiz_count_repalcer="_QUIZ_COUNT_"
quiz_point_info="Point: _POINT_ Combo: _COMBO_ Quiz Count: _QUIZ_COUNT_"
quiz_right_message="""\
Your anwer is right! 
"""

quiz_wrong_message="""\
Your anwer is wrong! 
"""

right_answer_replacer="_RIGHT_ANSWER_"
show_answer_message="""\
Right anser is _RIGHT_ANSWER_.
"""

win_message="""You win the game!
"""


loose_message="""You loose the game!
"""
achieve_easy=10
minus_easy=1
achieve_middle=20
minus_middle=2
achieve_hard=30
minus_hard=3
point_start=5
plus =  1
combo_plus = 2
minus = -1
achieve = 10
show_answer=True
passed_quiz=[]
def is_right_answer(answer,quiz):
    answers=quiz[1].split(",")
    return answer in answers

def random_choose_quiz():
    while(True):
        quiz = quiz_lib[random.randint(0,len(quiz_lib)-1)]
        if quiz not in passed_quiz:
            return quiz
    
def choose_level():
    """to choose level
    """
    level = raw_input("please select the level(1/2/3)\n")
    while True:
        print level_choose_message
        if level == '1':
            show_answer=True
            achieve=achieve_easy
            break
        if level == '2':
            achieve = achieve_middle
            minus = achieve_hard
            show_answer=False
            break
        if level == '3':
            achieve = achieve_hard
            minus = minus_hard
            show_answer=False
            break
        print level_choose_error_message

def play_quiz():
    print welcom_message
    plus =  1
    combo_plus = 2
    minus = -1
    point = point_start 
    passed_quiz=[]
    quiz_count = 0
#choose level
    choose_level()
    combo_count=1
# main loop of quiz
    while(point >= 0 and point < achieve):
        quiz = random_choose_quiz()
        #print quiz
        answer = raw_input(quiz_message.replace(quiz_word_replacer,quiz[0]))
        if(is_right_answer(answer,quiz)):
            if(combo_count>1):
                point+=combo_plus
            else:
                point+=plus
            combo_count+=1
            print quiz_right_message
        else:
            combo_count=1
            point+=minus
            print quiz_wrong_message
        if show_answer:
            print show_answer_message.replace(right_answer_replacer,quiz[1])
        quiz_count+=1
        print quiz_point_info.replace(point_replacer,str(point))\
        .replace(combo_replacer,str(combo_count))\
        .replace(quiz_count_repalcer,str(quiz_count))
    
# print game result 
    if(point>=achieve):
        print win_message
    else:
        print loose_message
            
        

def test_quiz():
    assert is_right_answer("rear",['front','rear'])
    assert is_right_answer("to allow",['to forbid','to allow,to let,to permit'])
    assert not is_right_answer("to bellow",['to forbid','to allow,to let,to permit'])
    #assert is_right_answer("to bellow",['to forbid','to allow,to let,to permit'])
#test_quiz()
play_quiz()