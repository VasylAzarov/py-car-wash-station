from app.Car import Car


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings


    def serve_cars(self, cars: list):
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_price, 1)


    def calculate_washing_price(self, car: Car):
        return round(
            car.comfort_class * (
                        self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center,
            1
        )


    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power


    def rate_service(self, rate: float) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
