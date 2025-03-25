import sys
from MapNode import MapNode


class PlannerNode:
    def __init__(self):
        print("✅ PlannerNode initialized!")

        self.current_obj = MapNode()
        self.visited = set()   # Track all visited cells
        self.visited2 = set()  # Track cells visited twice
        self.path = []  # Stack to track movement for backtracking
        print(f"Starting at: {self.current_obj.current}")
        
        # First move down
        print("Initial move: down")
        self.current_obj.direction_callback("down")  
        self.wall_callback()

    def distance_bottom(self):
        return ((7 - (self.current_obj.current[0] + 1)) ** 2 + (7 - self.current_obj.current[1]) ** 2) ** 0.5
    
    def distance_top(self):
        return ((7 - (self.current_obj.current[0] - 1)) ** 2 + (7 - self.current_obj.current[1]) ** 2) ** 0.5
    
    def distance_left(self):
        return ((7 - self.current_obj.current[0]) ** 2 + (7 - (self.current_obj.current[1] - 1)) ** 2) ** 0.5
    
    def distance_right(self):
        return ((7 - self.current_obj.current[0]) ** 2 + (7 - (self.current_obj.current[1] + 1)) ** 2) ** 0.5

    def wall_callback(self):
        reset_mode = False  # **New mode to temporarily ignore visited cells**
        print("🔄 Starting wall_callback loop...")

        while self.current_obj.current != self.current_obj.map.end:
            # **Track visits correctly**
            if self.current_obj.current in self.visited:
                self.visited2.add(self.current_obj.current)  # Mark as visited twice
            
            self.visited.add(self.current_obj.current)  # Mark as visited
            self.path.append(self.current_obj.current)  # Track path for backtracking
            
            print(f"Current Position: {self.current_obj.current}")
            
            distances = {
                "left": self.distance_left(),
                "down": self.distance_bottom(),
                "up": self.distance_top(),
                "right": self.distance_right()
            }
            
            print(f"Distances: {distances}")
            
            # Check available moves
            available_moves = {}
            real_moves = {}

            # **Normal movement check**
            if not self.current_obj.map.check_left_wall(self.current_obj.current):
                new_pos = (self.current_obj.current[0], self.current_obj.current[1] - 1)
                real_moves['left'] = distances['left']
                if new_pos not in self.visited2 and new_pos not in self.visited:
                    available_moves["left"] = distances["left"]

            if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
                new_pos = (self.current_obj.current[0] + 1, self.current_obj.current[1])
                real_moves["down"] = distances["down"]
                if new_pos not in self.visited2 and new_pos not in self.visited:
                    available_moves["down"] = distances["down"]

            if not self.current_obj.map.check_top_wall(self.current_obj.current):
                new_pos = (self.current_obj.current[0] - 1, self.current_obj.current[1])
                real_moves["up"] = distances["up"]
                if new_pos not in self.visited2 and new_pos not in self.visited:
                    available_moves["up"] = distances["up"]

            if not self.current_obj.map.check_right_wall(self.current_obj.current):
                new_pos = (self.current_obj.current[0], self.current_obj.current[1] + 1)
                real_moves["right"] = distances["right"]
                if new_pos not in self.visited2 and new_pos not in self.visited:
                    available_moves["right"] = distances["right"]

            print(f"Available moves: {available_moves}")

            if available_moves:
                reset_mode = False  # **Return to normal mode**
                best_direction = min(available_moves, key=available_moves.get)
                print(f"Moving: {best_direction}")
                self.current_obj.direction_callback(best_direction)

            else:
                # **Reset Mode: Ignore visited cells**
                if not reset_mode:
                    print("🚨 No moves available! Entering reset mode...")
                    reset_mode = True  # **Enable reset mode**
                    self.visited.discard(self.current_obj.current)  # **Remove current position only**
                    self.visited2.discard(self.current_obj.current)  # **Prevent getting trapped**
                    continue  # Restart loop to find a new move

                # **If reset mode is active and still stuck, backtrack**
                if self.path:
                    print(f"Backtracking from {self.current_obj.current}")
                    self.path.pop()  # Remove current position from path
                    last_position = self.path[-1] if self.path else None
                    if last_position:
                        self.current_obj.current = last_position
                        print(f"Backtracked to: {self.current_obj.current}")
                else:
                    print("Bot is completely stuck! No way to backtrack.")
                    break  # **Exit the loop to prevent infinite loops**
print("✅ Script is running!")
