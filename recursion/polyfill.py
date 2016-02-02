import sys
import random
GREEN = 0
RED = 1
BLUE = 2
YELLOW = 3
ORANGE = 4

COLORS = {0: 'GREEN', 1: 'RED', 2: 'BLUE', 3: 'YELLOW', 4: 'ORANGE'}

def print_grid(grid):
    for row in grid:
        for col in row:
            sys.stdout.write('%8s |' % COLORS[col])
        print ''

def random_grid(height=5, width=5):
    """
    creates a grid filled with random colors
    """
    grid = [[random.randint(0, len(COLORS)-1) for col in range(width)] for row in range(height)]
    return grid
    
def out_of_bounds(grid, x, y):
    if x >= len(grid):
        return True

    if y >= len(grid[x]):
        return True

    return False

def neighbors(grid, x, y):
    directions = {'W': lambda x, y: (x, y-1), 'S': lambda x, y: (x+1, y), 'E': lambda x, y: (x, y+1), 'N': lambda x, y: (x-1, y)}
    for d in directions.keys():
        x1, y1 = directions[d](x, y)

        # boundh check
        if x1 < 0:
            continue

        if x1 > len(grid) - 1:
            continue

        if y1 < 0:
            continue

        if y1 > len(grid[x1]) - 1:
            continue

        yield (x1, y1)


def polyfill(grid, x, y, original_color, new_color):
    # base cases

    # if of different color
    if grid[x][y] != original_color:
        return 

    # mark current cell with new color
    grid[x][y] = new_color

    # recursive case
    for new_x, new_y in neighbors(grid, x, y):
        polyfill(grid, new_x, new_y, original_color, new_color)


def fill(grid, x, y, color):
    """
    fills the given grid with given color starting from (x,y) untill 
    all neighboring pixels are of same color
    """
    current = grid[x][y]
    polyfill(grid, x, y, current, color)

def main():
    grid = random_grid(5, 5)
    print "current grid : "
    print_grid(grid)

    # get a random point
    x = random.randint(0, len(COLORS)-1)
    y = random.randint(0, len(COLORS)-1)
    new_color = original_color = grid[x][y]
    while new_color == original_color:
        new_color = random.randint(0, len(COLORS)-1)

    print "going to fill (%d, %d, %s) with %s" % (x, y, COLORS[original_color], COLORS[new_color]) 
    fill(grid, x, y, new_color)
    print_grid(grid)

if __name__ == "__main__":
    main()
