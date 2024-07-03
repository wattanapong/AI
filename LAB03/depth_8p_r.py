import pdb

class PuzzleState:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.visited = set()
        self.solution_found = False
        self.paths = []
        self.states = []

    def move(self, state, direction):
        new_state =  state.copy()
        blk = new_state.index(0)
        
        if direction == 'up' and blk >= 3:
            new_state[blk], new_state[blk - 3] = new_state[blk - 3], new_state[blk]

        elif direction == 'down' and blk < 6:
            new_state[blk], new_state[blk + 3] = new_state[blk + 3], new_state[blk]

        elif direction == 'left' and blk % 3 != 0:
            new_state[blk], new_state[blk - 1] = new_state[blk - 1], new_state[blk]

        elif direction == 'right' and (blk + 1) % 3 != 0:
            new_state[blk], new_state[blk + 1] = new_state[blk + 1], new_state[blk]
        else:
            return None

        return new_state

    def dfs(self, state, path):
        if self.solution_found:
            return
        
        self.visited.add(tuple(state))
        self.states.append(state)  # Store the current state
        self.paths.append(path)  # Store the current path

        if state == self.goal_state:
            self.solution_found = True
            return

        directions = ['up', 'down', 'left', 'right']
        for direction in directions:
            new_state = self.move(state, direction)
            if new_state and tuple(new_state) not in self.visited:
                self.dfs(new_state,direction)
                if self.solution_found:
                    return

        self.states.pop()  # Backtrack
        self.paths.pop()  # Backtrack

    def solve(self):
        self.dfs(self.initial_state, [])
        print(self.initial_state)
        if self.solution_found:
            return self.states, self.paths
        else:
            return None, None

    def print_solution(self):
        paths, states = self.solve()
        if paths and states:
            print("Solution Path:")
            for step, (path, state) in enumerate(zip(paths, states)):
                print(f"Step {step}: Move {path[-1] if path else 'Start'}")
                for row in state:
                    print(row)
                print()
        else:
            print("No solution found.")

# only run directly, __name__ variable is set to bet '__main__'
# when it was imported, the __name__ will be set to file name (depth_8p)
if __name__ == '__main__':
    # Example usage:
    initial_puzzle = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    # initial_puzzle =  [1, 2, 3, 4, 5, 6, 0, 7, 8]
    goal_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    puzzle = PuzzleState(initial_puzzle, goal_puzzle)

    states, solution_path = puzzle.solve()

    if solution_path:
        print(f"Solution Path: {solution_path}")
        print(states)
    else:
        print("No solution found.")
