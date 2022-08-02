# 틱택토 게임 Python 3.x
# v1

import random

# 1.1 플레이어의 기호 선택
def inputPlayerLetter():
    letter = ' '
    while letter not in ['X', 'O']:         # letter !='X' and letter !='O':
        print ('Do you want be X or O?')
        letter = input().upper()

    # 튜플의 첫 번째 요소가 플레이어의 글자이고 두 번째 요소는 컴퓨터의 글자
    if letter == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

# 1.2 선플레이어 결정
def whoGoesFirst():
    if random.randint(0,1):
        return 'computer'
    else:
        return 'player'

# 1.3 게임판 그리기
def drawBoard(board):
    print( '+---+---+---+')
    print( '| '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print( '+---+---+---+')
    print( '| '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print( '+---+---+---+')
    print( '| '+board[1]+' | '+board[2]+' | '+board[3]+' |')
    print( '+---+---+---+')


# 2.1 게임판에 수를 입력
def makeMove(board, letter, move):
    board[move] = letter

# 2.2 칸이 비어있는지 확인
def isSpaceFree(board, move):
    return board[move] == ' '

# 2.3 게임판이 꽉찼는지 확인
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    else:
        return True

# 2.4 승자가 있는지 확인
def isWinner(bo, le):
    # 보드(bo)와 플레이어 글자(le)를 파라미터로 받아,
    # (le)마크가 이겼을 때 True를 반환한다.
    return (
            (bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[1]==le and bo[4]==le and bo[7]==le) or
            (bo[2]==le and bo[5]==le and bo[8]==le) or
            (bo[3]==le and bo[6]==le and bo[9]==le) or
            (bo[3]==le and bo[5]==le and bo[7]==le) or
            (bo[1]==le and bo[5]==le and bo[9]==le)           
            )


# 3.1
def undoMove(board, move):
    pass
    
# 3.2 다음 수의 위치를 플레이어에게 입력 받는다.
def getPlayerMove(board):
    move = 0
    # 1<=move<=9가 아니거나 board[move]가 빈칸이 아니면 새 move를 입력 받음
    while move not in range(1,10) or not isSpaceFree(board, move):
        move = input('What is your next move? (1-9) ')
        # 입력에 숫자만 있는지 확인
        if move.isdigit():
            move = int(move)
        else:
            move = 0
    else:
        return move

# 3.3
def getWinMove(board, letter):
    pass

# 3.4
def getComputerMove(board, computerLetter):
    # playerLetter = 'O' if computerLetter=='X' else 'X'

    # (3)만약 비어있으면 중앙(5)을 차지한다.
    # (4)만약 비어있으면 코너(1,3,7,9)를 차지한다.
    # (5)만약 비어있으면 한쪽 면(2,4,6,8)을 차지한다.
    loc1 = [7,9,1,3]
    loc2 = [8,4,2,6]
    random.shuffle(loc1)
    random.shuffle(loc2)
    locList = [5]+loc1+loc2
    for i in locList:
        if isSpaceFree(board, i):
            return i
             
# 프로그램 실행 시작
print( 'Welcome to Tic Tac Toe!')
playerLetter, computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
print(turn, '가 먼저 시작합니다.')
# 길이 10의 배열을  만들고, 인덱스 0번은 사용하지 않음
theBoard= [' ']*10
gameIsPlaying = True
while  gameIsPlaying:
    if turn == 'computer':
        # 컴퓨터가 수를 둔다.
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)
        # 승자가 정해지면 게임 종료
        if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print('컴퓨터 승리..!')
            gameIsPlaying = False
        # 무승부 확인
        elif isBoardFull(theBoard):
            drawBoard(theBoard)
            print('무승부입니다..')
            gmaeIsPlaying = False
        # 승자가 결정되지 않으면 플레이어 차례
        else:
            turn =  'player'
    else:
        # 게임판을 그린다.
        drawBoard(theBoard)
        # 플레이어의 수를 입력 받는다.
        move = getPlayerMove(theBoard)
        # 입력받은 수를 적용한다.
        makeMove(theBoard, playerLetter, move)
        # 승자가 정해지면 게임 종료
        if isWinner(theBoard, playerLetter):
            drawBoard(theBoard)
            print('만세!! 당신이 이겼네요..!')
            gameIsPlaying = False
        # 무승부 확인
        elif isBoardFull(theBoard):
            drawBoard(theBoard)
            print('무승부입니다..')
            gmaeIsPlaying = False  
        # 승자가 결정되지 않으면 컴퓨터 차례
        else:
            turn = 'computer'

