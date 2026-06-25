from datetime import date

from car import Car


class SaleCar(Car):
    def __init__(self,license_num: int, manufacturer : str, model :str, year : int, color : str, price : int, size : str, status : bool, mile : int):
        super().__init__(license_num,manufacturer, model, year, color, price, size, status, mile)
        self.__sale_price = self.if_status(self.price)


    def __str__(self):
        car_details = super().__str__()
        return f"""{car_details}
Sale Price: {self.__sale_price}"""

    def if_status(self, sale_price : int) -> int:
        current_year = date.today().year
        year_price_depreciation = int((current_year - self.year) * 0.02)
        mile_price_depreciation = int(self.mile * 0.05)
        status_price_depreciation = int(sale_price * 0.80)
        sale_price -= (year_price_depreciation + mile_price_depreciation + status_price_depreciation)
        sale_profit = int(sale_price * 0.30)
        sale_price += sale_profit
        return sale_price


    @property
    def sale_price(self):
        return self.sale_price





