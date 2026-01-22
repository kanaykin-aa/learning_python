def rps(p1, p2):
    k='rock'
    n='scissors'
    b='paper'
    if p1==p2:
        return 'Draw!'
    elif p1==k and p2==n:
        return 'Player 1 won!'
    elif p1==n and p2==b:
        return 'Player 1 won!'
    elif p1==b and p2==k:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'