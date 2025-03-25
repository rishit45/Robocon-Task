import sys
import time
import tkinter
from MapClass import Map


class MapNode:
    def __init__(self):
        """Initialize MapNode and read the map from file."""
        
        f = open("map1.txt", "r")  # Change this location to the location of map1.txt on your device.
        dimensions = [int(i) for i in f.readline().split()]
        coords = [int(i) for i in f.readline().split()]
        array = []

        for i in range(dimensions[1]):
            array.append([int(i) for i in f.readline().split()])

        self.map = Map(dimensions[0], dimensions[1], (coords[0], coords[1]), (coords[2], coords[3]), array)
        self.current = self.map.start
        self.walls = Map(self.map.width, self.map.height, self.map.start, self.map.end)
        self.walls.array[self.current[0]][self.current[1]] = self.map.array[self.current[0]][self.current[1]]

        # Setup Tkinter
        self.print_root = tkinter.Tk()
        self.print_canvas = tkinter.Canvas(self.print_root, bg="white",
                                           height=(100 + self.walls.height * 50),
                                           width=(100 + self.walls.width * 50))
        self.print_canvas.pack()
        self.update_print()

    def direction_callback(self, direction):
        """Moves the bot in the specified direction if possible."""

        if direction == 'up' and not self.map.check_top_wall(self.current) and self.current[0] >= 1:
            self.current = (self.current[0] - 1, self.current[1])
        elif direction == 'left' and not self.map.check_left_wall(self.current) and self.current[1] >= 1:
            self.current = (self.current[0], self.current[1] - 1)
        elif direction == 'right' and not self.map.check_right_wall(self.current) and self.current[1] < self.map.width - 1:
            self.current = (self.current[0], self.current[1] + 1)
        elif direction == 'down' and not self.map.check_bottom_wall(self.current) and self.current[0] < self.map.height - 1:
            self.current = (self.current[0] + 1, self.current[1])

        if self.current == self.map.end:
            print('Goal reached')

        self.walls.array[self.current[0]][self.current[1]] = self.map.array[self.current[0]][self.current[1]]
        self.update_print()

    def update_print(self):
        """Updates the Tkinter canvas with the current map and colors."""
        self.print_canvas.delete("all")

        temp = self.walls

        # Mark the goal position in green
        self.print_canvas.create_rectangle(
            (50 + (temp.end[1] * 50)), (50 + (temp.end[0] * 50)),
            (50 + ((temp.end[1] + 1) * 50)), (50 + ((temp.end[0] + 1) * 50)),
            fill="#00ff00"
        )

        for i in range(temp.width):
            for j in range(temp.height):
                cell_value = temp.array[j][i]  # Get the value of the cell

                # 🌟 Color cells with value > 15 in red
                if cell_value > 15:
                    self.print_canvas.create_rectangle(
                        (50 + (i * 50)), (50 + (j * 50)),
                        (50 + ((i + 1) * 50)), (50 + ((j + 1) * 50)),
                        fill="#ff0000"  # Red color for values > 15
                    )

                # Draw walls
                if temp.check_top_wall((j, i)):
                    self.print_canvas.create_line(
                        (50 + (i * 50)), (50 + (j * 50)),
                        (50 + ((i + 1) * 50)), (50 + (j * 50)),
                        fill="#000000", width=2
                    )
                if temp.check_left_wall((j, i)):
                    self.print_canvas.create_line(
                        (50 + (i * 50)), (50 + (j * 50)),
                        (50 + (i * 50)), (50 + ((j + 1) * 50)),
                        fill="#000000", width=2
                    )
                if temp.check_right_wall((j, i)):
                    self.print_canvas.create_line(
                        (50 + ((i + 1) * 50)), (50 + (j * 50)),
                        (50 + ((i + 1) * 50)), (50 + ((j + 1) * 50)),
                        fill="#000000", width=2
                    )
                if temp.check_bottom_wall((j, i)):
                    self.print_canvas.create_line(
                        (50 + (i * 50)), (50 + ((j + 1) * 50)),
                        (50 + ((i + 1) * 50)), (50 + ((j + 1) * 50)),
                        fill="#000000", width=2
                    )

        # **🌟 Make the bot translucent using a semi-transparent color**
        bot_x1 = 50 + (self.current[1] * 50)
        bot_y1 = 50 + (self.current[0] * 50)
        bot_x2 = 50 + ((self.current[1] + 1) * 50)
        bot_y2 = 50 + ((self.current[0] + 1) * 50)

        self.print_canvas.create_oval(
            bot_x1 + 10, bot_y1 + 10, bot_x2 - 10, bot_y2 - 10,
            fill="#8080ff", outline="#0000ff"  # Light blue for translucent effect
        )

        self.print_canvas.update()
        time.sleep(0.1)


if __name__ == '__main__':
    print('The path taken by the bot is:')
    start_obj = MapNode()
    start_obj.print_root.mainloop()
