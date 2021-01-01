'''
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
'''


class Grid:
    ''' Class that takes in a world layout for reference'''

    def __init__(self, world_path):
        self.layout = []

        with open(world_path) as f:
            for line in f:
                grid_row = []
                for square in line:
                    if square != '\n':
                        grid_row.append(square)
                self.layout.append(grid_row)

        self.rows = len(self.layout)
        self.cols = len(self.layout[0])

    def check_for_trees(self, row, col):
        if self.layout[row][col] == '#':
            return True
        else:
            return False


class Toboggan:
    ''' Toboggan class that interacts with grid'''

    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = Grid('world.txt')

    def travel_slope(self, travel_cols, travel_rows, verbose=False):
        ''' toboggan moves down whole slope'''

        trees_hit = 0

        while self.y < self.grid.rows - 1:
            new_x = (self.x + travel_cols) % self.grid.cols
            new_y = self.y + travel_rows

            if self.grid.check_for_trees(new_y, new_x):
                trees_hit += 1
            
            # update coords
            self.x = new_x
            self.y = new_y

            if verbose:
                print(f'toboggan coords: {self.x, self.y} Trees hit: {trees_hit}')

        return trees_hit


if __name__ == '__main__':

    test_paths = [(1, 1),
                  (3, 1),
                  (5, 1),
                  (7, 1),
                  (1, 2)]
    
    path_trees = []

    for path in test_paths:
        t = Toboggan()
        trees = t.travel_slope(path[0], path[1])
        path_trees.append(trees)
        print(f'Trees hit for {path}: {trees} trees')

    multiplied = 1
    for count in path_trees:
        multiplied = count * multiplied

    print(f'Tree counts multiplied together: {multiplied}')