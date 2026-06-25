class Car:
    def __init__(self, id_ : int, manufacturer : str, model :str, year : int, color : str, price : int, size : tuple, status : bool, mile : int):
        self.__serial_num = id_
        self.__manufacturer = manufacturer
        self.__model = model
        self.__year = year
        self.color = color
        self.price = price
        self.__size = size
        self.status = status
        self.mile = mile


    def __str__(self):
        print(f"""serial number: {self.__serial_num}
manufacturer: {self.__manufacturer}
model: {self.__model}
year: {self.__year}""")



    @property
    def id_(self):
        return self.__serial_num


    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color):
        ans = input('Do you have a permission from Ministry of Transportation to execute it? (y/n)')
        self.color = color if ans == 'y' else self.color


    @property
    def size(self):
        return self.__size

    
    @property
    def mile(self):
        return self.mile
    
    @mile.setter
    def mile(self, mile):
        while mile <= self.mile:
            print('😘the mile is wrong. try again!')
        self.mile = mile

