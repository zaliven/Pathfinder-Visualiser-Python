import argparse


def get_cli_args():
    parser = argparse.ArgumentParser(description="Algorithm Visualizer")
    parser.add_argument("-algorithm", default='astar', dest="algorithm", help="Enter algorithm to use (astar, dijkstra, gbf)",
                        choices=["astar", "dijkstra", "gbf"])
    parser.add_argument("-rows", default='40', dest="rows", help="Enter number of rows (10-100)",
                        choices=range(10, 100))
    return parser.parse_args()
