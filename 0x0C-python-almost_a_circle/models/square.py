#!/usr/bin/python3
''' Square module inheriting from rectangle '''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Represents a square '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Class constructor '''
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Returns a string representation of a Square instance.'''

        form = '[Square] ({id}) {x}/{y} - {w}'
        return form.format(w=self.__width, id=self.id, x=self.x, y=self.y)

    @property
    def size(self):
        ''' size accessor '''
        return self.__width

    @size.setter
    def size(self, val):
        ''' size mutator
        args:
            val: value to set width to
        Raises:
            TypeError: if val is not an integer
            ValueError: if val is <= 0
        '''

        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be > 0')
        self.__width = val
        self.__height = val

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            if len(args) > 0:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    if type(val) != int and val is not None:
                        raise TypeError("id must be an integer")
                    self.id = val
                if key == 'size':
                    self.size = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        ''' Returns the dictionary representation of a Square '''
        sq_dict = {'id': self.id, 'size': self.size,
                    'x': self.x, 'y': self.y}
        return sq_dict
