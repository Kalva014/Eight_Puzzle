import copy

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.branching_factor = 0

        # Next state or otherwise children
        self.child_left = None
        self.child_up = None
        self.child_right = None
        self.child_down = None

    # Check to see if node is goal state
    def goal_test(self):
        if self.state == goal_state:
            print("REACHED GOAL STATE")

    # These are the operators where the puzzle can move(YOU CAN PROBABLY IMPROVE THIS FUNCTION TO BE MORE GENERAL)
    def generate_child(self):
        if(self.state[0][0] != 0 and self.state[1][0] != 0 and self.state[2][0] != 0): # Can move left
            print("Generate state where 0 can be moved left")
            self.child_left = copy.deepcopy(self.state)
            for row in range(len(self.child_left)):
                for column in range(len(self.child_left[row])):
                    if self.child_left[row][column] == 0:
                        zero_index_row = row
                        zero_index_column = column
            
            self.child_left[zero_index_row][zero_index_column - 1], self.child_left[zero_index_row][zero_index_column] = self.child_left[zero_index_row][zero_index_column], self.child_left[zero_index_row][zero_index_column - 1] # swap to the left

        if(self.state[0][0] != 0 and self.state[0][1] != 0 and self.state[0][2] != 0): # Can move up
            print("Generate state where 0 can be moved up")
            self.child_up = copy.deepcopy(self.state)
            for row in range(len(self.child_up)):
                for column in range(len(self.child_up[row])):
                    if self.child_up[row][column] == 0:
                        zero_index_row = row
                        zero_index_column = column
            
            self.child_up[zero_index_row - 1][zero_index_column], self.child_up[zero_index_row][zero_index_column] = self.child_up[zero_index_row][zero_index_column], self.child_up[zero_index_row - 1][zero_index_column] # swap up

        if(self.state[0][2] != 0 and self.state[1][2] != 0 and self.state[2][2] != 0): # Can move right
            print("Generate state where 0 can be moved right")
            self.child_right = copy.deepcopy(self.state)
            for row in range(len(self.child_right)):
                for column in range(len(self.child_right[row])):
                    if self.child_right[row][column] == 0:
                        zero_index_row = row
                        zero_index_column = column
            
            self.child_right[zero_index_row][zero_index_column + 1], self.child_right[zero_index_row][zero_index_column] = self.child_right[zero_index_row][zero_index_column], self.child_right[zero_index_row][zero_index_column + 1] # swap to the right
        
        if(self.state[2][0] != 0 and self.state[2][1] != 0 and self.state[2][2] != 0): # Can move down
            print("Generate state where 0 can be moved down")
            self.child_down = copy.deepcopy(self.state)
            for row in range(len(self.child_down)):
                for column in range(len(self.child_down[row])):
                    if self.child_down[row][column] == 0:
                        zero_index_row = row
                        zero_index_column = column
            
            self.child_down[zero_index_row + 1][zero_index_column], self.child_down[zero_index_row][zero_index_column] = self.child_down[zero_index_row][zero_index_column], self.child_down[zero_index_row + 1][zero_index_column] # swap to the right
    
    # Print the state of the puzzle
    def print_current_state(self):
        for puzzle_piece in self.state:
            print(*puzzle_piece)

class Tree:
    def __init__(self, starting_state):
        self.starting_state = starting_state #root node
        self.depth = 0
        self.cost = 0


def main():
    puzzle = [[], [], []]

    print("Welcome to 862026376 8 puzzle solver.")
    print("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.")
    user_choice = input()

    if user_choice == '1':
        puzzle[0].append(2)
        puzzle[0].append(1)
        puzzle[0].append(3)
        puzzle[1].append(4)
        puzzle[1].append(7)
        puzzle[1].append(6)
        puzzle[2].append(5)
        puzzle[2].append(8)
        puzzle[2].append(0)
        print(puzzle)
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
        print(puzzle)

    print("Enter your choice of algorithm")
    print("1.) Uniform Cost Search")  
    print("2.) A* with the Misplaced Tile Heuristic")
    print("3.) A* with the Euclidean distance Heuristic")

    user_choice = input()
    if user_choice == '1':
        print("Algorithm chosen is Uniform Cost Search")
    elif user_choice == '2':
        print("Algorithm chosen is A* with the Milsplaced Tile heuristic")
    else:
        print("Algorithm chosen is A* with the Euclidean distance heuristic")

    starting_state = Node(puzzle, None)
    starting_state.generate_child()
    starting_state.print_current_state()
    #tree = Tree(puzzle, starting_state)
    


if __name__ == "__main__":
    main()