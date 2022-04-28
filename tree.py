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

    # Generate child node
    def generate_child(self):
        print("CHILD NODE GENERATED")
    
    # Generate state to move down
    def move_down(self):
        print(" down")

class tree:
    def __init__(self, starting_state):
        self.starting_state = starting_state #root node
        self.depth = 0
        self.cost = 0