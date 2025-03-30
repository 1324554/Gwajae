import random

# 틱택토 보드 초기화
board = [" "] * 9

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("\n")

def check_winner():
    win_cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # 가로 승리
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 세로 승리
                 (0, 4, 8), (2, 4, 6)]  # 대각선 승리

    for a, b, c in win_cases:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # 'X' 또는 'O' 반환 (승자)
    if " " not in board:
        return "D"  # 무승부 (Draw)
    return None  # 아직 승자가 없음

def player_turn():
    while True:
        try:
            move = int(input("0~8 사이의 위치를 선택하세요: "))
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("이미 선택된 자리입니다. 다시 입력하세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 0~8 숫자를 입력하세요.")

def bot_turn():
    empty_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_positions)
    board[move] = "O"
    print(f"봇이 {move}번 위치에 둡니다.")

# 게임 루프
print("게임 시작")
print_board()

while True:
    player_turn()
    print_board()
    winner = check_winner()
    if winner:
        break

    bot_turn()
    print_board()
    winner = check_winner()
    if winner:
        break

# 승자 출력
if winner == "X":
    print("플레이어 승리")
elif winner == "O":
    print("봇 승리")
else:
    print("무승부")
