import random
def printSolution(result,s):
    print(s)
    for i in range(len(result)):
        row = ['|.'] * len(result)
        row += "|"
        row[result[i]] = '|Q'
        print("".join(row))

def printResults(result_node,result_list,alg=0):
        printSolution(result_list, "\nRESULT:")
        n=0
        k=1
        copy=result_node
        while copy!= None:
            n+=1
            copy=copy.parent
        print("\nSTEPS:")
        while n>0:
            copy=result_node
            for i in range(n-1):
                copy = copy.parent

            printSolution(copy.state, "STEP "+str(k))
            if alg==1:
                print("Heuristic: " + str(copy.h)+"\n")

            n-=1
            k+=1


def is_safe(board):
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False

    return True

def get_answer(text, option1, option2):
    while True:
        m=input(text)
        if m!=option1 and m!=option2:
            print("No such option!")
        else:
            return m

def get_number_of_range(s, n1, n2):
    is_number = False
    num = 0
    while not is_number:
        try:
            num = int(input(s))

            if num < n1:
                print("Minimum number is {}!".format(n1))
            elif num>n2:
                print("Maximum number is {}!".format(n2))
            else:
                is_number = True
        except ValueError:
            print("Entered value is not an integer.")
    return num
def get_board(n, answer):
    if answer=="n":
        board = [0]*n
        print("Input coordinates of queens (each queen in different row (from 1 to {})):".format(n))
        for i in range(n):
            board[i]=get_number_of_range("Row {}; column: ".format(i+1), 1, n)-1
        return board
    else:
        return [random.randint(0,n-1) for _ in range(n)]

