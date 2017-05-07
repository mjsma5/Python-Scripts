import math


class Point:
    # Object represents a point on a 3 dimensional grid
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point((self.y * other.z) - (self.z * other.y), self.z * other.x - self.x * other.z, self.x * other.y -
                     self.y * other.x)


def length(vector):
    # calculates the magnitude of a vector
    return math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)


def setup(file):
    # opens a file of points (xyz float locations)
    f = open(file, 'r')
    content = []
    for line in f.readlines():
        content.append([float(x) for x in line.split()])
    return content


def rx(start, end, point):
    # returns shortest distance from a vector to a point in space.
    # note: shortest line from vector to point will be perpendicular.
    d = length((point - start) * (point - end)) / length(end - start)
    return d


def line_segment_cost(segment):
    # defines the shortest path cost for a subset of locations
    if len(segment) < 1:
        return 0
    start = Point(segment[0][0], segment[0][1], segment[0][2])
    end = Point(segment[len(segment) - 1][0], segment[len(segment) - 1][1], segment[len(segment) - 1][2])
    line_vec = start - end
    vec_length = length(line_vec)
    if len(segment) <= 2:
        return vec_length*2
    p_length = 0
    for n in range(1, len(segment) - 1):
        current_point = Point(segment[n][0], segment[n][1], segment[n][2])
        current_length = rx(start, end, current_point)
        p_length += current_length
    return p_length + (2 * vec_length)


def path_segment(path, total_cost, index, content):
    # defines the shortest path for a subset of points
    if index >= len(content):
        path.append(len(content))
        result = [path, total_cost]
        return result
    else:
        curr_list = [content[index], content[index + 1]]
        segment_cost = line_segment_cost(curr_list)
        for n in range(index + 2, len(content)):
            curr_list.append(content[n])
            new_point_cost = line_segment_cost([curr_list[-1], curr_list[-2]])
            segment_cost += new_point_cost
            new_cost = line_segment_cost(curr_list)
            if new_cost < segment_cost:
                segment_cost = new_cost
            else:
                total_cost += segment_cost - new_point_cost
                index = n-1
                path.append(index)
                result = path_segment(path, total_cost, index, content)
                out = [result[0], result[1]]
                return out


def min_cost(file):
    # main running function, program takes as input a file of points, exacmple in source files, and utilises dynamic
    # programming to calculate the path and shortest distance possible to reach every location.
    content = setup(file)
    path = path_segment([0], 0, 0, content)
    print('Path = ' + str(path[0]) + 'Total Cost = ' + str(path[1]))


