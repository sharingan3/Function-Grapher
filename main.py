import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, x_coordinate, y_coordinate):
        "Initialize all x and y inputs"
        self.all_x_coordinate = x_coordinate
        self.all_y_coordinate = y_coordinate
 
        "Define axis scale"
        self.x_axis = np.linspace(-np.pi, np.pi, 100) # X axis controll
        self.y_axis = 3 * np.sin(self.x_axis) # Y axis controll

        "Draw the axis"
        self.fig = plt.figure() # The window of the graph
        self.ax = self.fig#.add_subplot(111)
        self.ax.set_title("Function Grpaher")
        self.ax.plot(self.x_axis, self.y_axis)

        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_color('none')

        "Plot the dots"
        plt.scatter(self.all_x_coordinate, self.all_y_coordinate)

        "Show the output"
        plt.show()

class Function:
    def __init__(self, x):
        "Initilize all x and y inputs"
        self.all_x_input = x        
        self.all_y_input = []

        "Loop through all x inputs to define y inputs"
        for i in self.all_x_input:
            self.all_y_input.append(i ** 2) # Function here

        "Run graph class to display output"
        self.graph = Graph(self.all_x_input, self.all_y_input)

        self.correct()

    def correct(self):
        print(self.all_y_input)

if __name__ == "__main__":
    inputs = []
    
    "Initialize inputs"
    for i in range(-50, 50):
        inputs.append(i)

    "Run function"
    function = Function(inputs)
