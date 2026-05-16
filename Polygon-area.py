import math

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
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Calculates the diagonal using the formula from image_d350f4.png
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        # Creates a string of * with a newline at the end of each row
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        # Uses floor division to find how many fit along each axis
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        return horizontal_fit * vertical_fit

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        # Initializes both width and height with the side value
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
    
rect = Rectangle(4, 2)

print(rect.get_area())

print(rect.get_picture())




