"""
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any live cell with two or three live neighbours lives on to the next generation.
Any dead cell with exactly three live neighbours becomes a live cell.
Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:

print(htmlize(cells))

"""
import copy

def print_2d_arr(arr):
    for row in arr:
        print(row)
    print("\n\n")

def get_generation(cells, generations):
    def get_neighbors(ri, ci, rmax, cmax):
        n, s, e, w, ne, nw, se, sw = [(None, None)] * 8
        if ri - 1 >= 0:
            n = (ri-1, ci)
        if ri - 1 >= 0 and ci - 1 >= 0:
            nw = (ri-1, ci-1)
        if ri - 1 >= 0 and ci + 1 <= cmax:
            ne = (ri - 1, ci + 1)
        if ci - 1 >= 0:
            w = (ri, ci - 1)
        if ci + 1 <= cmax:
            e = (ri, ci + 1)
        if ri + 1 <= rmax and ci - 1 >= 0:
            sw = (ri + 1, ci - 1)
        if ri + 1 <= rmax:
            s = (ri + 1, ci)
        if ri + 1 <= rmax and ci + 1 <= cmax:
            se = (ri + 1, ci + 1)
        return n, s, e, w, ne, nw, se, sw
    copy_of_cells = copy.deepcopy(cells)
    for rindex, ritem in enumerate(cells):
        for cindex, citem in enumerate(cells[rindex]):
            neighbors = get_neighbors(rindex, cindex, len(cells)-1, len(ritem)-1)
            print(f"I am a {citem} located at {(rindex, cindex)}")
            print(
                f"My neighbors:"
                f"N{neighbors[0]} "
                f"S{neighbors[1]} "
                f"E{neighbors[2]} "
                f"W{neighbors[3]} "
                f"NE{neighbors[4]} "
                f"NW{neighbors[5]} "
                f"SE{neighbors[6]} "
                f"SW{neighbors[7]} "
            )
            consolidated_neighbors = []
            for neighbor in neighbors:
                x = neighbor[0]
                y = neighbor[1]
                if x is None or y is None:
                    continue
                consolidated_neighbors.append(cells[x][y])
            print(f"consolidated_neighbors -> {consolidated_neighbors}")
            
            if citem == 0:
                if neighbors.count(1) == 1:
                    copy_of_cells[rindex][cindex] = 1
            elif citem == 1:
                if neighbors.count(1) < 2 or neighbors.count(1) > 3:
                    copy_of_cells[rindex][cindex] = 0
            print_2d_arr(copy_of_cells)
    return cells

# -*- coding: utf-8 -*-
def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]
         
#test.describe('Glider<:LF:>' + htmlize(start))
#test.it('Glider 1')
print_2d_arr(start)
resp = get_generation(start, 1)
print_2d_arr(end)
print_2d_arr(resp)
#print(f'expected: {htmlize(resp)}')
#print(f'actual: {htmlize(resp)}')

#test.expect(resp == end, 'Got<:LF:>' + htmlize(resp) + '<:LF:>instead of<:LF:>' + htmlize(end))