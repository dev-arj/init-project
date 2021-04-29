width = 13
height = 3
def PlayerProfile():
    player1 = str(input("Enter the name of Player One: "))
    player2 = str(input("Enter the name of Player Two: "))
    return [player1, player2]
print("The game begins here!")
players = PlayerProfile()
print(f'{players[0]} plays "X" and {players[1]} plays with "O"')
Soman = True
XPlay = True
positionList = [0,0]
while Soman:
    if XPlay:    
        positionList[0] = int(input())
        positionList[1] = int(input())
    continew = str(input("Enter Q to exit!"))
    if continew == 'q' or continew == 'Q':
        Soman = False
        print("The End!!!")


print('-' * width)
for i in range(height):
    print('|',  f'{i:^3d}' * 3, '|')
print('-' * width)
