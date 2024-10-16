class Car:
    brand = None  # Поле == Змінна
    color = None
    speed = None

    def select_car(self, brand, color, speed): # Метод == Функція
        self.brand = brand
        self.color = color
        self.speed = speed

    def get_data(self):
        print("Brand:", self.brand,"Color:", self.color, "Speed:", self.speed)



car1 = Car() # Обєкт на основі класу
car1.select_car("Audi", "green", "260")
car1.get_data()
car2 = Car()
car2.select_car("Nissan", "red", "360")
car2.get_data()

a = 5 #int
b = "П'ять" # srt
c = 5.0 # float