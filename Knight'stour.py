import sys
from collections import deque

line1 = input().split()
line2 = input().split()

alp = "abcdefghijklmnopqrstuvwx"
alplist = [x for x in alp]

nodes = []
nodes.append(line1[2])
nodes.extend(line2)

node2 = []
for i in nodes:
    node2.append([str(i[0]), str(i[1:])])


for i in node2:
    i[0] = alplist.index(i[0])
    i[1] = int(line1[0]) + 1 - int(i[1])



# A queue node used in BFS
class Node:
    # (x, y) represents chessboard coordinates
    # `dist` represents its minimum distance from the source
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

    # As we are using `Node` as a key in a dictionary,
    # we need to override the `__hash__()` and `__eq__()` function
    def __hash__(self):
        return hash((self.x, self.y, self.dist))

    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)


# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


# Check if (x, y) is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)


# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def findShortestDistance(src, dest, N):
    # set to check if the matrix cell is visited before or not
    visited = set()

    # create a queue and enqueue the first node
    q = deque()
    q.append(src)

    # loop till queue is empty
    while q:

        # dequeue front node and process it
        node = q.popleft()

        x = node.x
        y = node.y
        dist = node.dist

        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist

        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)

            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(len(row)):
                # get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]

                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))

    # return infinity if the path is not possible
    return sys.maxsize


if __name__ == '__main__':

    N = int(line1[0])  # N x N matrix


    def knighter(lis1, lis2, c=0):

        minlist = []
        if len(lis2) == 0:
            return c
        for i in range(len(lis2)):
            src = Node(int(lis1[0]), int(lis1[1]))  # source coordinates
            dest = Node(int(lis2[i][0]), int(lis2[i][1]))  # destination coordinates
            val = findShortestDistance(src, dest, N)
            if i == 0:
                min = val
            if val <= min:
                min = val
                minlist = lis2[i]
        c = c + min
        lis2.remove(minlist)

        return knighter(minlist, lis2, c)


    print(knighter(node2[0], node2[1:]))










