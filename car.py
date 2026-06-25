class Car:
    def __init__(self,license_num: int, manufacturer : str, model :str, year : int, color : str, price : int, size : str, status : bool, mile : int):
        self._license_num = license_num
        self._manufacturer = manufacturer
        self._model = model
        self._year = year
        self.color = color
        self.price = price
        self._size = size
        self.status = status
        self.mile = mile


    def __str__(self):
        return (f"""serial number: {self._license_num}
manufacturer: {self._manufacturer}
model: {self._model}
year: {self._year}""")



    @property
    def id_(self):
        return self._license_num


    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color):
        ans = input('Do you have a permission from Ministry of Transportation to execute it? (y/n)')
        self.color = color if ans == 'y' else self.color


    @property
    def size(self):
        return self._size

    
    @property
    def mile(self):
        return self.mile
    
    @mile.setter
    def mile(self, mile):
        while mile <= self.mile:
            print('😘the mile is wrong. try again!')
        self.mile = mile

