def minion_game(string):
    vowels='AEIOU'
    Kevin=0
    Stuart=0
    n=len(string)
    for i in range(n):
        if string[i] in vowels:
            Kevin+=n-i
        else:
            Stuart+=n-i
    if Kevin>Stuart:
        print("Kevin", Kevin)
    elif Kevin<Stuart:
        print("Stuart", Stuart)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
