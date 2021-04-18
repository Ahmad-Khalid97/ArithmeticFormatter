class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        s = ""
        if self.width > 50 or self.height > 50:
            s = "Too big for picture."
            print(s)
        else:
            s = ('*' * self.width + '\n') * self.height
        return s

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def get_amount_inside(self, shape):
        self.shape = shape
        x = self.get_area() // shape.get_area()
        if x > 0:
            return x
        else:
            return 0


class Square(Rectangle):
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)

    def set_side(self, side_length):
        self.height = side_length
        self.width = side_length

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
