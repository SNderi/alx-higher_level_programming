#!/usr/bin/python3
''' Module Rectangle inheriting from base '''


from models.base import Base


class Rectangle(Base):
    ''' Represents a rectangle
    Private attributes:
        width
        height
        x
        y

    Methods:
        area: finds area of rectangle
        display: Prints rectangle using #
        update: uses args and kwargs to assign an argument to attributes
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width accessor '''
        return self.__width

    @width.setter
    def width(self, val):
        ''' Width mutator
        args:
            val: value to set width to
        Raises:
            TypeError: if val is not an integer
            ValueError: if val is <= 0
        '''
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        ''' height accessor '''
        return self.__height

    @height.setter
    def height(self, val):
        ''' Height mutator
        args:
            val: value to set height to
        Raises:
            TypeError: if val is not an integer
            ValueError: if val is <= 0
        '''
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        ''' x accessor '''
        return self.__x

    @x.setter
    def x(self, val):
        ''' x mutator
        args:
            val: value to set x to
        Raises:
            TypeError: if val is not an integer
            ValueError: if val is <= 0
        '''
        if not isinstance(val, int):
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        ''' y accessor '''
        return self.__y

    @y.setter
    def y(self, val):
        ''' y mutator
        args:
            val: value to set y to
        Raises:
            TypeError: if val is not an integer
            ValueError: if val is <= 0
        '''
        if not isinstance(val, int):
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        ''' Returns rectangle area '''
        return self.__height * self.__width

    def display(self):
        ''' Prints in stdout the Rectangle instance with the character # '''

        print('\n' * self.__y, end='')
        for col in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        ''' Returns a string representation of a Rectangle instance. '''

        form = '[Rectangle] ({id}) {x}/{y} - {w}/{h}'
        form = form.format(h=self.__height, w=self.__width, id=self.id,
                           x=self.__x, y=self.__y)
        return form

    def update(self, *args, **kwargs):
        ''' Assigns an argument to each attribute
        Args:
            id
            width
            height
            x
            y
        '''
        if args is not None and len(args) != 0:
            if len(args) > 0:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    if type(val) != int and val is not None:
                        raise TypeError("id must be an integer")
                    self.id = val
                if key == 'width':
                    self.width = val
                if key == 'height':
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        ''' Returns the dictionary representation of a Rectangle '''

        rect_dict = {'id': self.id, 'width': self.__width,
                     'height': self.__height, 'x': self.__x, 'y': self.__y}
        return rect_dict
