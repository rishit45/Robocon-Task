import sys
from MapNode import MapNode

class PlannerNode:
    def __init__(self):
        self.medi_list=[1]
        self.medi_obj =MapNode()
        self.current_obj = MapNode()
        self.visited = set()#this stores the coords of the cells the block has visited
        self.current_obj.direction_callback("down")  
        
        self.wall_callback()
   #The basic premise of the algorithim is that the bot goes to the cell that is closest to the end point
    def distance_bottom(self):
        return ((self.current_obj.map.end[0] - (self.current_obj.current[0] + 1)) ** 2 + (self.current_obj.map.end[1] - self.current_obj.current[1]) ** 2) ** 0.5
    
    def distance_top(self):
        return ((self.current_obj.map.end[0] - (self.current_obj.current[0] - 1)) ** 2 + (self.current_obj.map.end[1] - self.current_obj.current[1]) ** 2) ** 0.5
    
    def distance_left(self):
        return ((self.current_obj.map.end[0] - self.current_obj.current[0]) ** 2 + (self.current_obj.map.end[1] - (self.current_obj.current[1] - 1)) ** 2) ** 0.5
    
    def distance_right(self):
        return ((self.current_obj.map.end[0] - self.current_obj.current[0]) ** 2 + (self.current_obj.map.end[1] - (self.current_obj.current[1] + 1)) ** 2) ** 0.5

    def wall_callback(self):
        while self.current_obj.current != self.current_obj.map.end:
            #the bot current position is appended to the visited list
            self.visited.add(self.current_obj.current)
            
            distances = {
                "left": self.distance_left(),
                "down": self.distance_bottom(),
                "up": self.distance_top(),
                "right": self.distance_right()
            }
            #as the bot can get stuck in a reapeating loop we make it so it does not revist the alredy visited cells
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

            if available_moves:
                best_direction = min(available_moves, key=available_moves.get)
                move_mapping = {"up": 0, "down": 1, "left": 2, "right": 3}
                self.medi_list.append(move_mapping[best_direction])
                print(move_mapping[best_direction],end='')
                self.current_obj.direction_callback(best_direction)

            #if the bot is at a deadend with no available moves it esentially restarts its journey forgeting about the visited blocks until
            #it finds a available move not in the visited originaly

            if len(available_moves) == 0:
                while len(available_moves) == 0:
                    self.visited2 = set() #this stores the coords that the bot is forced on to go on twice
                    self.visited2.add(self.current_obj.current)
                    real_moves = {}
                    
                    if not self.current_obj.map.check_left_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0], self.current_obj.current[1] - 1)
                        if new_pos not in self.visited2:
                            real_moves["left"] = distances["left"]
                        if new_pos not in self.visited:
                            available_moves["left"] = distances["left"]

                    if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0] + 1, self.current_obj.current[1])
                        if new_pos not in self.visited2:
                            real_moves["down"] = distances["down"]
                        if new_pos not in self.visited:
                            available_moves["down"] = distances["down"]

                    if not self.current_obj.map.check_top_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0] - 1, self.current_obj.current[1])
                        if new_pos not in self.visited2:
                            real_moves["up"] = distances["up"]
                        if new_pos not in self.visited:
                            available_moves["up"] = distances["up"]

                    if not self.current_obj.map.check_right_wall(self.current_obj.current):
                        new_pos = (self.current_obj.current[0], self.current_obj.current[1] + 1)
                        if new_pos not in self.visited2:
                            real_moves["right"] = distances["right"]
                        if new_pos not in self.visited:
                            available_moves["right"] = distances["right"]

                    if real_moves:
                        best_direction = min(real_moves, key=real_moves.get)
                        move_mapping = {"up": 0, "down": 1, "left": 2, "right": 3}
                        self.medi_list.append(move_mapping[best_direction])
                        print(move_mapping[best_direction],end='')
                        self.current_obj.direction_callback(best_direction)
      #for medical bot to follow(shown in another tinker tab)
    def move_medical_bot(self):
        print("\nThe medical bot is now following the main bot's path.")
                                
        for movement in self.medi_list:
            if movement == 0:
                self.medi_obj.direction_callback("up")
            elif movement == 1:
                self.medi_obj.direction_callback("down")
            elif movement == 2:
                self.medi_obj.direction_callback("left")
            elif movement == 3:
                self.medi_obj.direction_callback("right")

            if self.medi_obj.current == self.current_obj.map.end:
                print("\nThe medical bot has also reached the goal!")

if __name__ == '__main__':
    print("the path followed by the bot is: ")
    print(1,end='')
    start_obj = PlannerNode()
    start_obj.move_medical_bot()
    start_obj.current_obj.print_root.mainloop()
    print('the medical bot also needs to follow this task')
    
