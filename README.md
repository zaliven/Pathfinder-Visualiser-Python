# Pathfinder-Visualizer-Python
A visualization tool to compare pathfinding algorithms. Using pygame as the visualizer, Dijkstra's, A* and Greedy Best First Search are implemented.

![imgur](https://i.imgur.com/KZclLdo.gif)

# Requirements
Pygame

## Usage
```
python main.py -algorithm astar -rows 40
```
ALGORITHM - Algorithm of choice {options: dijkstra, astar, gbf}. Defaults to astar

ROWS - Number of rows to use. Defaults to 40

Both are optional arguments. <br/>&nbsp;

First click - start point

Second click - end point

All other clicks - barriers <br/>&nbsp;

SPACEBAR Key - begin visualizing algorithm

C Key - Clear (when board is not active)
