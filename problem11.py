
def grid_max(g):
    """find the max value searching right, up, and diagaonally"""
    max = 0
    max = up(g, max)
    max = right(g, max)
    max = diag(g, max)
    return max


def right(g, max):
    """find the max value searching right to left"""

    n = len(g[0]) - 3
    for l in g:
        for m in xrange(n):
            p = l[m] * l[m+1] * l[m+2] * l[m+3]
            if max < p:
                max = p
    return max


def up(g, max):
    """find the max value searching up and down"""

    n = len(g[0]) - 3
    for l in xrange(len(g) - 1):
        for m in xrange(n):
            p = g[m][l] * g[m+1][l] * g[m+2][l] * g[m+3][l]
            if max < p:
                max = p
    return max


def diag(g, max):
    """find the max value searching diagaonally"""

    n = len(g[0]) - 3
    # \
    for l in xrange(n):
        for m in xrange(n):
            p = g[l][m] * g[l+1][m+1] * g[l+2][m+2] * g[l+3][m+3]
            if max < p:
                max = p
    # /
    for l in xrange(n, 0, -1):
        for m in xrange(n):
            p = g[l][m] * g[l+1][m-1] * g[l+2][m-2] * g[l+3][m-3]
            if max < p:
                max = p
    return max


def product_max(g):
    maxp = 0
    for l in xrange(len(G)):
        for m in xrange(len(G)):
            vertical = get(l, m) * get(l+1, m) * get(l+2, m) * get(l+3, m)
            # print "vertical is " + str(vertical)
            horizontal = get(l, m) * get(l, m+1) * get(l, m+2) * get(l, m+3)
            # print "horizontal is " + str(horizontal)
            rightdiag = get(l, m) * get(l+1, m+1) * get(l+2, m+2) * get(l+3, m+3)
            # print "rightdiag is " + str(rightdiag)
            if max(vertical, horizontal, rightdiag) > maxp:
                maxp = max(vertical, horizontal, rightdiag)
    for l in xrange(len(G), 0, -1):
        for m in xrange(len(G)):
            leftdiag = get(l, m) * get(l+1, m-1) * get(l+2, m-2) * get(l+3, m-3)
            if leftdiag > maxp:
                maxp = leftdiag
    return maxp


def get(i, j):
    try:
        return G[i][j]
    except IndexError:
        return 0


def grid_creator():
    """formats the given grid from project euler"""

    a = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
    b = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
    c = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
    d = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
    e = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
    f = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
    g = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
    h = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
    i = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
    j = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
    k = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
    l = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
    m = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
    n = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
    o = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
    p = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
    q = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
    r = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
    s = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
    t = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
    u = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

    grid = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
    for i in xrange(len(grid)):
        grid[i] = [int(s) for s in grid[i].split(' ')]
    return grid

G = grid_creator()

if __name__ == '__main__':
    print grid_max(grid_creator())
    print product_max(grid_creator())
