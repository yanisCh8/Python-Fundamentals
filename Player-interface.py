from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    @abstractmethod
    def level_up(self):
        pass

    def make_move(self):
        # Select a random move from the moves list
        move = random.choice(self.moves)
        
        # Calculate new coordinates
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]

        # Update position and history
        self.position = (new_x, new_y)
        self.path.append(self.position)

        return self.position

class Pawn(Player):
    def __init__(self):
        # Initialize parent attributes
        super().__init__()
        # Define basic movements: up, down, left, right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # Add the four diagonal movements to the existing moves list
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)


# 1. Create the Pawn (The "Object")
my_pawn = Pawn()

print(f"Starting Position: {my_pawn.position}")

# 2. Make some moves
for i in range(3):
    new_pos = my_pawn.make_move()
    print(f"Move {i+1}: {new_pos}")

# 3. Level up and check the new move options
print(f"Moves before level up: {len(my_pawn.moves)}")
my_pawn.level_up()
print(f"Moves after level up: {len(my_pawn.moves)}")

# 4. Show the full path taken
print(f"Full Path: {my_pawn.path}")




