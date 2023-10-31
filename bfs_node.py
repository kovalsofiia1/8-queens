from collections import deque
import random
import psutil
import os
import time
import common as c
class NodeBFS:
    def __init__(self, state, parent=None):
        self.state = state  # State of the board
        self.parent = parent  # Parent node


# Функція для пошуку першого розв'язку за допомогою BFS
def solve_n_queens_bfs(initial_board):
    n = len(initial_board)
    initial_node = NodeBFS(initial_board, None)
    queue = deque()
    queue.append(initial_node)
    num_of_states = 0
    num_of_states_in_memory=1
    while queue:
        board = queue.popleft() #board is node!!
        num_of_states_in_memory-=1
        if c.is_safe(board.state):
            return board  # Знайдено розв'язок

        pid = os.getpid() #retrieves the process ID (PID) of the current process
        process = psutil.Process(pid) # Get process object for the current process
        memory_info = process.memory_info()# Get memory usage in bytes
        memory_usage_bytes = memory_info.rss
        if (memory_usage_bytes > 1024 * 1024 * 1024):
            n = 0
            copy = board
            while copy != None:
                n += 1
                copy = copy.parent
            print("Number of iterations: {}".format(n))
            print("Number of states generated: {}".format(num_of_states))
            print("Number of states in memory: {}".format(num_of_states_in_memory))
            break

        # Генеруємо наступний стан, переміщаючи ферзів
        for i in range(n):
            for j in range(n):
                if board.state[i] != j:
                    next_board = list(board.state)
                    next_board[i] = j
                    queue.append(NodeBFS(next_board,board))
                    num_of_states+=1
                    num_of_states_in_memory += 1
                    if c.is_safe(next_board):
                        print("Number of states generated: {}".format(num_of_states))
                        print("Number of states in memory: {}".format(num_of_states_in_memory))
                        return NodeBFS(next_board,board)  # Знайдено розв'язок

    return None  # Розв'язок не знайдено


# Початковий стан дошки, де ферзі вже розставлені

def bfs_logic(initial_board):
    c.printSolution(initial_board,"INITIAL BOARD")
    start = time.time()
    result = solve_n_queens_bfs(initial_board)
    end = time.time()
    execution = end - start
    print("Execution time: " +  str(execution))
    if result!=None:
        c.printResults(result, result.state)
    else:
        print("Solution not found! Memory usage problem!")
