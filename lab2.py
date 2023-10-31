import my_rbfs as rbfs
import bfs_node as bfs
import common as c

n=c.get_number_of_range("Enter number of queens: ", 4, 20)
answer = c.get_answer("Want to generate board? (y/n): ", "y","n")
initial_board = c.get_board(n, answer)
choice= int(c.get_answer("\nChoose algorithm \n1 - BFS; 2 - RBFS : ","1","2"))
if choice==1:
    bfs.bfs_logic(initial_board)
else:
    rbfs.rbfs_logic(initial_board)
