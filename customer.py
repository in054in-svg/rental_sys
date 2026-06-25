class Customer:
    def __init__(self, name: str, id_: int, age: int, tel: int)-> None:
        self._name = name
        self._id_ = id_
        self.age = age
        self.tel = tel

    @property
    def name(self)-> str:
        return self._name

    @property
    def id_(self)-> int:
        return self._id_

    @property
    def age(self)-> int:
        return self._age
    @age.setter
    def age(self, age: int)-> None:
        if age < 0:
            raise ValueError("גיל לא יכול להיות מספר שלילי!")
        if age < 18:
            raise ValueError("הלקוח חייב להיות בן 18 ומעלה כדי לשכור רכב!")
        self._age = age

    @property
    def tel(self)-> int:
        return self._tel
    @tel.setter
    def tel(self, tel: int)-> None:
        if tel < 500000000 or tel > 599999999:
            raise ValueError("מספר פלאפון נייד חייב להתחיל ב-5 ולהכיל 9 ספרות!")
        self._tel = tel

    def __str__(self)-> str:
        return f"Valued Customer: {self.name} | ID: {self.id_} | Age: {self.age} | Phone: 0{self.tel}"

