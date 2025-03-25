import sys

from MapNode import MapNode

class PlannerNode:
    def __init__(self):
        self.current_obj=MapNode()
        
        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1
        self.wall_callback()

    def distance_bottom(self):
       return ((7-self.current_obj.current[0]+1)**2+(7-self.current_obj.current[1])**2)**.5
    
    def distance_top(self):
       return ((7-self.current_obj.current[0]-1)**2+(7-self.current_obj.current[1])**2)**.5
    
    def distance_left(self):
       return ((7-self.current_obj.current[0])**2+(7-self.current_obj.current[1]-1)**2)**.5
    
    def distance_right(self):
       return ((7-self.current_obj.current[0])**2+(7-self.current_obj.current[1]+1)**2)**.5

    def wall_callback(self):
        directions = ['left', 'down', 'right', 'up']
        origin_distance=[distance_bottom(),distance_left(),distance_right(),distance_top()]
        #as the bot moves down initialy we need to start surveing from the left and then go clockwise to find the optimal path
        # for direction in directions:
        #     if direction == 'left' and not self.current_obj.map.check_left_wall(self.current_obj.current):
        #         best_direction = 'left'
        #         print(2,end='')
        #         break
        #     elif direction == 'down' and not self.current_obj.map.check_bottom_wall(self.current_obj.current):
        #         best_direction = 'down'
        #         print(2,end='')
        #         break
        #     elif direction == 'right' and not self.current_obj.map.check_right_wall(self.current_obj.current):
        #         best_direction = 'right'
        #         print(2,end='')
        #         break
        #     elif direction == 'up' and not self.current_obj.map.check_top_wall(self.current_obj.current):
        #         best_direction = 'up'
        #         print(2,end='')
        #         break
        
        #self.current_obj.direction_callback(best_direction)
        while self.current_obj.current != self.current_obj.map.end:
        #now the block is at the second cell to now find the path it could rotate clockwise from the direction it came
            # if best_direction == 'left':
            #     if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("down")
            #         print(2,end='')
            #         best_direction = 'down'
            #     elif not self.current_obj.map.check_right_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("right")
            #         print(2,end='')
            #         best_direction = 'right'
            #     elif not self.current_obj.map.check_top_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("up")
            #         print(2,end='')
            #         best_direction = 'up'
            #     elif not self.current_obj.map.check_left_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("left")
            #         print(2,end='')
            #         best_direction = 'left'

            # elif best_direction == 'right':
            #     if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("down")
            #         print(1,end='')
            #         best_direction = 'down'
            #     elif not self.current_obj.map.check_right_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("right")
            #         print(3,end='')
            #         best_direction = 'right'
            #     elif not self.current_obj.map.check_top_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("up")
            #         print(0,end='')
            #         best_direction = 'up'
            #     elif not self.current_obj.map.check_left_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("left")
            #         print(2,end='')
            #         best_direction = 'left'

            # elif best_direction == 'down':
            #     if not self.current_obj.map.check_right_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("right")
            #         print(3,end='')
            #         best_direction = 'right'
            #     elif not self.current_obj.map.check_bottom_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("down")
            #         print(1,end='')
            #         best_direction = 'down'
            #     elif not self.current_obj.map.check_left_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("left")
            #         print(2,end='')
            #         best_direction = 'left'
            #     elif not self.current_obj.map.check_top_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("up")
            #         print(0,end='')
            #         best_direction = 'up'

            # elif best_direction == 'up':
            #     if not self.current_obj.map.check_left_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("left")
            #         print(2,end='')
            #         best_direction = 'left'
            #     elif not self.current_obj.map.check_top_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("up")
            #         print(0,end='')
            #         best_direction = 'up'
            #     elif not self.current_obj.map.check_right_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("right")
            #         print(3,end='')
            #         best_direction = 'right'
            #     elif not self.current_obj.map.check_bottom_wall(self.current_obj.current):
            #         self.current_obj.direction_callback("down")
            #         print(1,end='')
            #         best_direction = 'down'
            if(len(set(origin_distance))==len(origin_distance)):

               if not self.current_obj.map.check_left_wall(self.current_obj.current):
                  if distance_left()==min(origin_distance):
                     self.current_obj.direction_callback("left")

               if not self.current_obj.map.check_bottom_wall(self.current_obj.current):
                  if distance_bottom()==min(origin_distance):
                     self.current_obj.direction_callback("down")

               if not self.current_obj.map.check_top_wall(self.current_obj.current):
                  if distance_top()==min(origin_distance):
                     self.current_obj.direction_callback("up")

               if not self.current_obj.map.check_right_wall(self.current_obj.current):
                  if distance_right()==min(origin_distance):
                     self.current_obj.direction_callback("right")
                
                
               
            
                
                

if __name__ == '__main__':
    print('the path taken by the bot is:')
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 