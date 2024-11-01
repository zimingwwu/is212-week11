class Shape:
    def calculate_area(self, shape_type, **kwargs):
        pass

class Circle(Shape):
    def calculate_area(self, **kwargs):
        radius = kwargs.get('radius')
        return 3.14 * radius * radius

class Rectangle(Shape):
    def calculate_area(self, **kwargs):
        length = kwargs.get('length')
        width = kwargs.get('width')
        return length * width


class Triangle(Shape):
    def calculate_area(self, **kwargs):
        base = kwargs.get('base')
        height = kwargs.get('height')
        return 0.5 * base * height
