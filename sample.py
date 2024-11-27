import tkinter as tk

# Define the grid size and cell size
GRID_SIZE = 5
CELL_SIZE = 60

class GridGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Grid Game")
        
        # Create a canvas for the grid
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()
        
        # Draw the grid
        self.cells = {}
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                self.cells[(row, col)] = cell
        
        # Initialize player position
        self.player_pos = (0, 0)
        self.update_player_position()
        
        # Bind arrow key events
        root.bind("<Up>", self.move_up)
        root.bind("<Down>", self.move_down)
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)

    def update_player_position(self):
        # Clear all cells
        for (row, col), cell in self.cells.items():
            self.canvas.itemconfig(cell, fill="white")
        
        # Highlight the player's position
        row, col = self.player_pos
        self.canvas.itemconfig(self.cells[(row, col)], fill="blue")
    
    def move_up(self, event):
        row, col = self.player_pos
        if row > 0:  # Check boundary
            self.player_pos = (row - 1, col)
        self.update_player_position()

    def move_down(self, event):
        row, col = self.player_pos
        if row < GRID_SIZE - 1:  # Check boundary
            self.player_pos = (row + 1, col)
        self.update_player_position()

    def move_left(self, event):
        row, col = self.player_pos
        if col > 0:  # Check boundary
            self.player_pos = (row, col - 1)
        self.update_player_position()

    def move_right(self, event):
        row, col = self.player_pos
        if col < GRID_SIZE - 1:  # Check boundary
            self.player_pos = (row, col + 1)
        self.update_player_position()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GridGame(root)
    root.mainloop()
