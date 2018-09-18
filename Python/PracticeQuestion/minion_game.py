''' The below code has two functions minion_game_1 and minion_game_2 which does the same operation except the len overhead which
is modified in two functions to check the number of function calls made through cProfiling . We could see the result that 
minion_game_1 has better performance then minion_game_2'''


import cProfile

def minion_game_1(string):
    # your code goes here
    vowels = 'AEIOU'
    ln=len(string)
    kevin_score = 0
    stuart_score = 0
    for i in range(ln):
        if s[i] in vowels:
            kevin_score += (ln-i)
        else:
            stuart_score += (ln-i)

    if kevin_score > stuart_score:
        print ("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print ("Stuart", stuart_score)
    else:
        print ("Draw")


def minion_game_2(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin_score += (len(string)-i)
        else:
            stuart_score += (len(string)-i)

    if kevin_score > stuart_score:
        print ("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print ("Stuart", stuart_score)
    else:
        print ("Draw")

def ctest(s):
    print('calling without len stats')
    cProfile.runctx("minion_game_1(s)", {'minion_game_1': minion_game_1},{'s':s})
    print('calling with len stats')
    cProfile.runctx("minion_game_2(s)", {'minion_game_2': minion_game_2}, {'s': s})

if __name__ == '__main__':
    s = input()
    ctest(s)
