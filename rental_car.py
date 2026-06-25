from car import Car
from customer import Customer

class Rental_car(Car):
    def __init__(self, id_: int, manufacturer: str, model: str, year: int, color: str,
                 price: int, size: str, status: bool, mile: int,
                 renter: Customer, days_rent: int, mile_req: int):
        super().__init__(id_, manufacturer, model, year, color, price, size, status, mile)
        self.renter = renter
        self.days_rent = days_rent
        self.mile_req = mile_req
        self._mile_default = 300

    @property
    def base_price(self):
        return 250 if self.size == "Small" else 400

    @property
    def day_price(self):
        extra = 50.0 if self.mile_req > self._mile_default else 0.0
        return float(self.base_price + extra)

    @property
    def week_price(self):
        return self.day_price * 5

    @property
    def month_price(self):
        return self.week_price * 3

    def calculate_total_price(self) -> float:
        if self.days_rent >= 30:
            return (self.days_rent // 30) * self.month_price + (self.days_rent % 30) * self.day_price
        if self.days_rent >= 7:
            return (self.days_rent // 7) * self.week_price + (self.days_rent % 7) * self.day_price
        return self.days_rent * self.day_price

    def update_mile(self) -> None:
        self.mile += self.mile_req

    def __str__(self) -> str:
        return (f"Rental Car [{self.manufacturer} {self.model}] - Renter: {self.renter}, "
                f"Days: {self.days_rent}, Total Price: {self.calculate_total_price():.2f}")