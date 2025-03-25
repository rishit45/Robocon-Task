import sys
from MapNode import MapNode


class PlannerNode:
    def __init__(self):
        self.current_obj = MapNode()
        self.visited = []
        self.visited2 = []
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
        while self.current_obj.current != self.current_obj.map.end:
            self.visited.append(self.current_obj.current)
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
            
            if not self.current_obj.map.check_left_wall(self.current_obj.current):
               
                new_pos = (self.current_obj.current[0], self.current_obj.current[1] - 1)
                if new_pos not in self.visited:
                    available_moves["left"] = distances["left"]

            if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
              
                new_pos = (self.current_obj.current[0] + 1, self.current_obj.current[1])
                if new_pos not in self.visited:
                    available_moves["down"] = distances["down"]

            if not self.current_obj.map.check_top_wall(self.current_obj.current):
             
                new_pos = (self.current_obj.current[0] - 1, self.current_obj.current[1])
                if new_pos not in self.visited:
                    available_moves["up"] = distances["up"]

            if not self.current_obj.map.check_right_wall(self.current_obj.current):
                
                new_pos = (self.current_obj.current[0], self.current_obj.current[1] + 1)
                if new_pos not in self.visited:
                    available_moves["right"] = distances["right"]

            print(f"Available moves: {available_moves}")

            if available_moves:
                best_direction = min(available_moves, key=available_moves.get)
                print(f"Moving: {best_direction}")
                self.current_obj.direction_callback(best_direction)
                # if len(real_moves)==1:
                #     self.current_obj.direction_callback(best_direction)
                #     if best_direction == "up":
                #         self.current_obj.map.add_top_wall((self.current_obj.current[0]+1,self.current_obj.current[1]))
                #     if best_direction == "down":
                #         self.current_obj.map.add_top_wall((self.current_obj.current[0]-1,self.current_obj.current[1]))
                #     if best_direction == "right":
                #         self.current_obj.map.add_top_wall((self.current_obj.current[0],self.current_obj.current[1]-1))
                #     if best_direction == "left":
                #         self.current_obj.map.add_top_wall((self.current_obj.current[0],self.current_obj.current[1]+1))
                    
            if len(available_moves)==0:
                while len(available_moves)==0:
                    self.visited2.append(self.current_obj.current)
                    
                    distances2 = {
                        "left": self.distance_left(),
                        "down": self.distance_bottom(),
                        "up": self.distance_top(),
                        "right": self.distance_right()
                    }
                    
                    
                    # Check available moves
                    real_moves ={}
                    if not self.current_obj.map.check_left_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0], self.current_obj.current[1] - 1)
                        if new_pos not in self.visited2:
                            real_moves["left"] = distances["left"]

                    if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0] + 1, self.current_obj.current[1])
                        if new_pos not in self.visited2:
                            real_moves["down"] = distances["down"]

                    if not self.current_obj.map.check_top_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0] - 1, self.current_obj.current[1])
                        if new_pos not in self.visited2:
                            real_moves["up"] = distances["up"]

                    if not self.current_obj.map.check_right_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0], self.current_obj.current[1] + 1)
                        if new_pos not in self.visited2:
                            real_moves["right"] = distances["right"]

                    if real_moves:
                        best_direction = min(real_moves, key=real_moves.get)
                        print(f"Moving: {best_direction}")
                        self.current_obj.direction_callback(best_direction)
                        # if len(real_moves)==1:
                        #     self.current_obj.direction_callback(best_direction)
                        #     if best_direction == "up":
                        #         self.current_obj.map.add_top_wall((self.current_obj.current[0]+1,self.current_obj.current[1]))
                        #     if best_direction == "down":
                        #         self.current_obj.map.add_top_wall((self.current_obj.current[0]-1,self.current_obj.current[1]))
                        #     if best_direction == "right":
                        #         self.current_obj.map.add_top_wall((self.current_obj.current[0],self.current_obj.current[1]-1))
                        #     if best_direction == "left":
                        #         self.current_obj.map.add_top_wall((self.current_obj.current[0],self.current_obj.current[1]+1))
                            
                    

if __name__ == '__main__':
    print('The path taken by the bot is:')
    start_obj = PlannerNode()
    start_obj.current_obj.print_root.mainloop()
