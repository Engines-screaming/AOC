'''
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
'''

class Grid:

    def __init__(self, world_path):
        self.layout = []

        with open(world_path) as f:
            for line in f:
                grid_row = []
                for square in line:
                    if square != '\n':
                        grid_row.append(square)
                self.layout.append(grid_row)


if __name__ == '__main__':
    g = Grid('world.txt')

            