class Shape:
    def clone(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        return Rectangle(self.width, self.height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def clone(self):
        return Square(self.length)

    def get_length(self):
        return self.length


class Test:
    def clone_shapes(self, shapes):
        cloned_shapes = []

        for shape in shapes:
            cloned_shapes.append(shape.clone())

        return cloned_shapes
