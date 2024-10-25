class Shape:
    def calculate_area(self, shape_type, **kwargs):
        if shape_type == 'circle':
            radius = kwargs.get('radius')
            return 3.14 * radius * radius
        elif shape_type == 'rectangle':
            length = kwargs.get('length')
            width = kwargs.get('width')
            return length * width
        elif shape_type == 'triangle':
            base = kwargs.get('base')
            height = kwargs.get('height')
            return 0.5 * base * height
