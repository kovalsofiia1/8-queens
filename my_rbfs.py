import time
import common as c

num_of_states = 0
num_of_states_in_memory=1

class Node:
    def __init__(self, state, parent=None, h=0, g=0):
        self.state = state  # State of the board
        self.parent = parent  # Parent node
        self.g = g  # Cost from the start node to this node
        self.h = h  # Heuristic value
        self.f = g + h  # Evaluation function f

    def get_g(self):
        return self.g

def generate_successors(board):#board is a node
    global num_of_states, num_of_states_in_memory
    num_of_states_in_memory=0
    n= len(board.state)
    successors = []
    for i in range(n):
        for j in range(n):
            if board.state[i] != j:
                next_board = list(board.state)
                next_board[i] = j
                new_g=board.get_g()
                new_g+=1
                new_node=Node(next_board, board,  heuristic_f2(next_board),new_g)
                successors.append(new_node)
                num_of_states+=1
                num_of_states_in_memory+=1
    return successors


def rbfs(node, f_limit):
    if c.is_safe(node.state):
        return (node.state, node.f, node)

    successors = generate_successors(node)
    for s in successors:
        if c.is_safe(node.state):
            return (node.state, node.f,node)
        s.f = max(s.g + s.h, node.f)

    while True:
        successors.sort(key=lambda x: x.f)
        best = successors[0]

        if best.f > f_limit:
            return ([], best.f, best)  # Exceeded the limit

        alternative = successors[1].f if len(successors) > 1 else float('inf')

        result, best.f,best = rbfs(best, min(f_limit, alternative))
        if result:
            return result, best.f, best

def heuristic_f2(state):
    n = len(state)  # Assuming the state is an array representing the board

    # Initialize the conflict count to zero
    conflict_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens in positions i and j are in the same column
            if state[i] == state[j]:
                conflict_count += 1

            # Check if queens in positions i and j are in the same diagonal
            if abs(state[i] - state[j]) == abs(i - j):
                conflict_count += 1

    return conflict_count

def rbfs_logic(initial_board):

    c.printSolution(initial_board, "INITIAL BOARD")
    print("Heuristic: "+ str(heuristic_f2(initial_board)))
    start = time.time()
    result,_, res_node = rbfs(Node(initial_board, None, heuristic_f2(initial_board)), float("inf"))
    end = time.time()
    execution = end-start
    print("Execution time: " + str(execution))
    print("Number of states generated: {}".format(num_of_states))
    print("Number of states in memory: {}".format(num_of_states_in_memory))
    if result!=None:
        c.printResults(res_node, result, 1)
    else:
        print("Solution not found!")
