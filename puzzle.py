import copy
import operator
import time
#import heapq as hq

goal_state_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_state_2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
goal_state_flag = 0


# Each node represents the current state the puzzle is in
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.branching_factor = 0
        self.approximate_cost = 0 # This is g(n) which is actual cost to reach node n
        self.estimated_cost = 0 # This is h(n) which is estimated cost to goal
        self.total_cost = 0 # This is f(n) = g(n) + h(n)

        # Next state or otherwise children
        self.child_left = None
        self.child_up = None
        self.child_right = None
        self.child_down = None

    # Check to see if node is goal state
    def goal_test(self):
        if self.state == goal_state_1 or self.state == goal_state_2:
            print("REACHED GOAL STATE")
            return True
        else:
            return False

    # Print the state of the puzzle
    def print_current_state(self):
        for puzzle_piece in self.state:
            print(*puzzle_piece)

    # Returns true if the state has children
    def has_children(self):
        if self.child_left != None or self.child_up != None or self.child_right != None or self.child_down != None:
            return True
        else:
            return False
    
    # Measure branching factor(Number of new nodes/children created when expanding a node)
    def get_branching_factor(self):
        self.branching_factor = 0
        if self.child_left != None:
            self.branching_factor += 1
        if self.child_up != None:
            self.branching_factor += 1
        if self.child_right != None:
            self.branching_factor += 1
        if self.child_down != None:
            self.branching_factor += 1
        
        return self.branching_factor

    # Measure current states misplaced tile heuristic value or how far they are from the goal state and return it
    def get_misplaced_tile_heuristic(self):
        num_misplaced_tiles = 0

        if goal_state_flag == 1:
            for i in range(len(goal_state_1)):
                for j in range(len(goal_state_1[i])):
                    if goal_state_1[i][j] != self.state[i][j]:
                        num_misplaced_tiles += 1
        
        if goal_state_flag == 2:
            for i in range(len(goal_state_2)):
                for j in range(len(goal_state_2[i])):
                    if goal_state_2[i][j] != self.state[i][j]:
                        num_misplaced_tiles += 1
        
        self.estimated_cost = num_misplaced_tiles

    # Combine to approximate cost and estimated cost to get the total cost of cheapest solution
    def get_total_cost(self):
        self.total_cost = self.approximate_cost + self.estimated_cost


# The tree holds the states of the puzzle
class Tree:
    def __init__(self, starting_state):
        self.starting_state = starting_state #root node
        self.depth = 0
    
    # Pass in the state of the puzzle you want to generate moves for. These mores are the operators where the puzzle or 0(otherwise known as the blank space) can move
    def generate_child(self, current_state):
        if(current_state.state[0][0] != 0 and current_state.state[1][0] != 0 and current_state.state[2][0] != 0): # Can move left
            #print("Generate state where 0 can be moved left")
            current_state.child_left = copy.deepcopy(current_state)
            current_state.child_left.parent = current_state
            current_state.child_left.approximate_cost += 1
            #for row in range(len(current_state.child_left.state)):
            #    for column in range(len(current_state.child_left.state[row])):
            #        if current_state.child_left.state[row][column] == 0:
            #            zero_index_row = row
            #            zero_index_column = column
            zero_index_row, zero_index_column = get_row_column_index(current_state.child_left.state, 0)

            current_state.child_left.state[zero_index_row][zero_index_column - 1], current_state.child_left.state[zero_index_row][zero_index_column] = current_state.child_left.state[zero_index_row][zero_index_column], current_state.child_left.state[zero_index_row][zero_index_column - 1] # swap to the left
            #current_state.child_left.print_current_state()

        if(current_state.state[0][0] != 0 and current_state.state[0][1] != 0 and current_state.state[0][2] != 0): # Can move up
            #print("Generate state where 0 can be moved up")
            current_state.child_up = copy.deepcopy(current_state)
            current_state.child_up.parent = current_state
            current_state.child_up.approximate_cost += 1
            #for row in range(len(current_state.child_up.state)):
            #    for column in range(len(current_state.child_up.state[row])):
            #        if current_state.child_up.state[row][column] == 0:
            #            zero_index_row = row
            #            zero_index_column = column
            zero_index_row, zero_index_column = get_row_column_index(current_state.child_up.state, 0)

            current_state.child_up.state[zero_index_row - 1][zero_index_column], current_state.child_up.state[zero_index_row][zero_index_column] = current_state.child_up.state[zero_index_row][zero_index_column], current_state.child_up.state[zero_index_row - 1][zero_index_column] # swap up
            #current_state.child_up.print_current_state()

        if(current_state.state[0][2] != 0 and current_state.state[1][2] != 0 and current_state.state[2][2] != 0): # Can move right
            #print("Generate state where 0 can be moved right")
            current_state.child_right = copy.deepcopy(current_state)
            current_state.child_right.parent = current_state
            current_state.child_right.approximate_cost += 1
            #for row in range(len(current_state.child_right.state)):
            #    for column in range(len(current_state.child_right.state[row])):
            #        if current_state.child_right.state[row][column] == 0:
            #            zero_index_row = row
            #            zero_index_column = column
            zero_index_row, zero_index_column = get_row_column_index(current_state.child_right.state, 0)

            current_state.child_right.state[zero_index_row][zero_index_column + 1], current_state.child_right.state[zero_index_row][zero_index_column] = current_state.child_right.state[zero_index_row][zero_index_column], current_state.child_right.state[zero_index_row][zero_index_column + 1] # swap to the right
            #current_state.child_right.print_current_state()
        
        if(current_state.state[2][0] != 0 and current_state.state[2][1] != 0 and current_state.state[2][2] != 0): # Can move down
            #print("Generate state where 0 can be moved down")
            current_state.child_down = copy.deepcopy(current_state)
            current_state.child_down.parent = current_state
            current_state.child_down.approximate_cost += 1
            #for row in range(len(current_state.child_down.state)):
            #    for column in range(len(current_state.child_down.state[row])):
            #        if current_state.child_down.state[row][column] == 0:
            #            zero_index_row = row
            #            zero_index_column = column
            zero_index_row, zero_index_column = get_row_column_index(current_state.child_down.state, 0)
            
            current_state.child_down.state[zero_index_row + 1][zero_index_column], current_state.child_down.state[zero_index_row][zero_index_column] = current_state.child_down.state[zero_index_row][zero_index_column], current_state.child_down.state[zero_index_row + 1][zero_index_column] # swap to the right
            #current_state.child_down.print_current_state()



# Returns the row and column index for a specific value in a matrix
def get_row_column_index(puzzle_state, value_to_find):
    for i, rows in enumerate(puzzle_state):
        try:
            j = rows.index(value_to_find)
        except ValueError:
            continue
        return i, j



# Return the nodes path and its cost
def get_path(starting_node, current_node):
    path = []
    cost = 0

    while(current_node.parent != None):
        path.append(current_node)
        current_node = current_node.parent
        cost += 1
        
    path.append(starting_node)
    return path, cost



# Prints out path from  initial state to goal state
def print_path(solution_path):
    print("Solution path:")
    for i in reversed(solution_path):
        print("\n")
        print(f"The best state to expand with g(n)={i.approximate_cost} and h(n)={i.estimated_cost} is...")
        i.print_current_state()



# Expand the cheapest node and the cost is the path cost
def uniform_cost_search(tree):
    frontier = [] # Priority Queue
    #hq.heappush(frontier, (tree.starting_state.cost ,tree.starting_state))
    frontier.append(tree.starting_state)
    
    visited = []

    while(frontier): # loop until frontier is empty
        if(not frontier):
            print("Frontier is empty and no solution was found!")
            return

        frontier.sort(key=operator.attrgetter('approximate_cost'))
        current_node = frontier.pop(0)
        
        #hq.heapify(frontier)
        #node = hq.heappop(frontier)
        #current_node = node[1]
        
        #print("\n")
        #current_node.print_current_state()
        #print("Current Node Cost")
        #print(current_node.cost)
        #print("Branching Factor:")
        #print(current_node.get_branching_factor())
        #print("\n")

        if(current_node.goal_test()):
            solution_path, path_cost = get_path(tree.starting_state, current_node)
            print(f"Path cost is: g(n)={path_cost}")
            print_path(solution_path)
            return solution_path # MIGHT NEED TO PUT THIS OUTSIDE OF THE WHILE LOOP TO LOOK AT BETTER SOLUTION PATHS
        
        visited.append(current_node.state) # THIS MIGHT BE THE ERROR WHERE I AM COMPARING THE MATRIX ITSELF INSTEAD OF THE NODE(CONTAINS THE MATRIX, COST, ETC.)
        
        tree.generate_child(current_node)
        
        if(current_node.has_children()):
            if(current_node.child_left != None):
                if((current_node.child_left.state in visited) == False):
                    frontier.append(current_node.child_left)
                    #hq.heappush(frontier, (current_node.child_left.cost, current_node.child_left))
            if(current_node.child_up != None):
                if((current_node.child_up.state in visited) == False):
                    frontier.append(current_node.child_up)
                    #hq.heappush(frontier, (current_node.child_up.cost, current_node.child_up))
            if(current_node.child_right != None):
                if((current_node.child_right.state in visited) == False):
                    frontier.append(current_node.child_right)
                    #hq.heappush(frontier, (current_node.child_right.cost, current_node.child_right))
            if(current_node.child_down != None):
                if((current_node.child_down.state in visited) == False):
                    frontier.append(current_node.child_down)
                    #hq.heappush(frontier, (current_node.child_down.cost, current_node.child_down))



# Use tile misplaced heuristic so that the search algorithm is not blind but informed
def A_star_misplaced_tile(tree):
    frontier = [] # Priority Queue
    #hq.heappush(frontier, (tree.starting_state.cost ,tree.starting_state))
    tree.starting_state.get_misplaced_tile_heuristic()
    tree.starting_state.get_total_cost()
    frontier.append(tree.starting_state)
    
    visited = []

    while(frontier): # loop until frontier is empty
        if(not frontier):
            print("Frontier is empty and no solution was found!")
            return

        frontier.sort(key=operator.attrgetter('total_cost'))
        current_node = frontier.pop(0)
        
        #hq.heapify(frontier)
        #node = hq.heappop(frontier)
        #current_node = node[1]
        
        #print("\n")
        #current_node.print_current_state()
        #print("Current Node Cost")
        #print(current_node.cost)
        #print("Branching Factor:")
        #print(current_node.get_branching_factor())
        #print("\n")

        if(current_node.goal_test()):
            solution_path, path_cost = get_path(tree.starting_state, current_node)
            print(f"Path cost is: g(n)={path_cost}")
            print("Branching")
            print_path(solution_path)
            return solution_path # MIGHT NEED TO PUT THIS OUTSIDE OF THE WHILE LOOP TO LOOK AT BETTER SOLUTION PATHS
        
        visited.append(current_node.state) # THIS MIGHT BE THE ERROR WHERE I AM COMPARING THE MATRIX ITSELF INSTEAD OF THE NODE(CONTAINS THE MATRIX, COST, ETC.)
        
        tree.generate_child(current_node)
        
        if(current_node.has_children()):
            if(current_node.child_left != None):
                if((current_node.child_left.state in visited) == False):
                    current_node.child_left.get_misplaced_tile_heuristic()
                    current_node.child_left.get_total_cost()
                    frontier.append(current_node.child_left)
                    #hq.heappush(frontier, (current_node.child_left.cost, current_node.child_left))
            if(current_node.child_up != None):
                if((current_node.child_up.state in visited) == False):
                    current_node.child_up.get_misplaced_tile_heuristic()
                    current_node.child_up.get_total_cost()
                    frontier.append(current_node.child_up)
                    #hq.heappush(frontier, (current_node.child_up.cost, current_node.child_up))
            if(current_node.child_right != None):
                if((current_node.child_right.state in visited) == False):
                    current_node.child_right.get_misplaced_tile_heuristic()
                    current_node.child_right.get_total_cost()
                    frontier.append(current_node.child_right)
                    #hq.heappush(frontier, (current_node.child_right.cost, current_node.child_right))
            if(current_node.child_down != None):
                if((current_node.child_down.state in visited) == False):
                    current_node.child_down.get_misplaced_tile_heuristic()
                    current_node.child_down.get_total_cost()
                    frontier.append(current_node.child_down)
                    #hq.heappush(frontier, (current_node.child_down.cost, current_node.child_down))





def main():
    puzzle = [[], [], []]

    print("Welcome to 862026376 8 puzzle solver.")
    print("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.")
    user_choice = input()

    if user_choice == '1':
        puzzle[0].append(1)
        puzzle[0].append(0)
        puzzle[0].append(3)
        puzzle[1].append(4)
        puzzle[1].append(2)
        puzzle[1].append(6)
        puzzle[2].append(7)
        puzzle[2].append(5)
        puzzle[2].append(8)
        print(f"Here is the puzzle: {puzzle}")
    else:
        print("Enter your puzzle, use a zero to represent the blank")
        print("Enter the first row, press enter after entering a number")
        puzzle[0].append(int(input()))
        puzzle[0].append(int(input()))
        puzzle[0].append(int(input()))

        print("Enter the second row, press enter after entering a number")
        puzzle[1].append(int(input()))
        puzzle[1].append(int(input()))
        puzzle[1].append(int(input()))

        print("Enter the third row, press enter after entering a number")
        puzzle[2].append(int(input()))
        puzzle[2].append(int(input()))
        puzzle[2].append(int(input()))
        print(f"Here is the puzzle: {puzzle}")


    print("\nEnter 1 if you want your goal state to be...")
    print(goal_state_1)
    print("\nEnter 2 if you want your goal_state to be...")
    print(goal_state_2)
    user_choice = input()
    global goal_state_flag
    if user_choice == '1':
        goal_state_flag = 1
    else:
        goal_state_flag = 2
    print(f"Goal state flag set to {goal_state_flag}\n")


    starting_state = Node(puzzle, None)
    tree = Tree(starting_state)
    

    print("Enter your choice of algorithm")
    print("1.) Uniform Cost Search")  
    print("2.) A* with the Misplaced Tile Heuristic")
    print("3.) A* with the Euclidean distance Heuristic")
    
    user_choice = input()
    if user_choice == '1':
        print("\nAlgorithm chosen is Uniform Cost Search")
        init_time = time.perf_counter()
        uniform_cost_search(tree)
        end_time = time.perf_counter()
        print(f"Solution found in {end_time - init_time} seconds")

    elif user_choice == '2':
        print("\nAlgorithm chosen is A* with the Milsplaced Tile heuristic")
        init_time = time.perf_counter()
        A_star_misplaced_tile(tree)
        end_time = time.perf_counter()
        print(f"Solution found in {end_time - init_time} seconds")
        
    else:
        print("\nAlgorithm chosen is A* with the Euclidean distance heuristic")
        init_time = time.perf_counter()
        A_star_misplaced_tile(tree)
        end_time = time.perf_counter()
        print(f"Solution found in {end_time - init_time} seconds")


if __name__ == "__main__":
    main()