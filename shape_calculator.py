class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            string_pic = ''
            for line in range(self.height):
                string_pic += '*' * self.width + '\n'
            return string_pic

    def get_amount_inside(self, rec):
        return (self.width // rec.width) * (self.height // rec.height)

    def __repr__(self):
        return self.__class__.__name__ + "(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):

    def __init__(self, side_length):
        self.side_length = side_length
        self.width = side_length
        self.height = side_length

    def set_side(self, side_length):
        self.side_length = side_length
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __repr__(self):
        return self.__class__.__name__ + "(side={})".format(self.side_length)
