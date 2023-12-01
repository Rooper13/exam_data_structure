class Rectangle:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    
    def contains(self, point):
        return (self.x - self.w < point[0] < self.x + self.w and
                self.y - self.h < point[1] < self.y + self.h)

class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary, self.capacity, self.points, self.divided = boundary, capacity, [], False
    
    def insert(self, point):
        if not self.boundary.contains(point): return False
        if len(self.points) < self.capacity: return self.points.append(point) or True
        if not self.divided: self.subdivide()
        return (self.northeast.insert(point) or self.northwest.insert(point) or
                self.southeast.insert(point) or self.southwest.insert(point))
    
    def subdivide(self):
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.w / 2, self.boundary.h / 2
        ne, nw, se, sw = Rectangle(x + w, y - h, w, h), Rectangle(x - w, y - h, w, h), Rectangle(x + w, y + h, w, h), Rectangle(x - w, y + h, w, h)
        self.northeast, self.northwest, self.southeast, self.southwest, self.divided = QuadTree(ne, self.capacity), QuadTree(nw, self.capacity), QuadTree(se, self.capacity), QuadTree(sw, self.capacity), True
    
    def query(self, range):
        points_in_range = [point for point in self.points if range.contains(point)]
        if self.divided:
            for tree in [self.northeast, self.northwest, self.southeast, self.southwest]:
                points_in_range.extend(tree.query(range))
        return points_in_range

# Example usage
boundary = Rectangle(0, 0, 100, 100)
quad_tree = QuadTree(boundary, 4)

points_to_insert = [(10, 20), (30, 40), (70, 80), (90, 90), (50, 60), (25, 75)]

for point in points_to_insert:
    quad_tree.insert(point)

search_range = Rectangle(40, 30, 30, 30)
points_in_range = quad_tree.query(search_range)

print("Points within the search range:", points_in_range)
