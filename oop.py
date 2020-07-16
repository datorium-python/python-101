# OOP in Python


class Car:
    brand = None
    wheel_count = 4
    engine_status = "off"
    # is_engine_on = False

    def __init__(self, model, color="white", fuel_type="petrol", gearbox_type="automatic", door_count=4):
        self.model = model
        self.color = color
        self.fuel_type = fuel_type
        self.gearbox_type = gearbox_type
        self.door_count = door_count

    @property
    def is_engine_on(self):
        if self.engine_status == 'off':
            return False
        else:
            return True

    @staticmethod
    def sound_alarm(mins=1):
        print('ALAAAARM! ' * mins)

    @classmethod
    def get_brand_info(cls):
        return cls.brand

    def get_car_brand_info(self):
        return self.brand

    def engine_turn_on(self):
        print('STARTING ENGINE...')
        self.engine_status = "on"
        print('ENGINE STARTED')

    def engine_turn_off(self):
        print('STOPPING ENGINE...')
        self.engine_status = "off"
        print('ENGINE STOPPED')

    def print_engine_status(self):
        print('ENGINE STATUS: ', self.engine_status)

    def print_info(self):
        print('')
        print(f'### {self.brand} {self.model} CAR OBJECT ###')
        print('BRAND: ', self.brand)
        print('MODEL: ', self.model)
        print('COLOR: ', self.color)
        print('FUEL: ', self.fuel_type)
        print('GEARBOX: ', self.gearbox_type)
        print('DOORS: ', self.door_count)
        print('WHEELS: ', self.wheel_count)
        print('ENGINE STATUS: ', self.engine_status)
        print('ENGINE STATUS BOOL:', self.is_engine_on)


class BMW(Car):
    brand = "BMW"


class Audi(Car):
    brand = "Audi"


class Peugeot(Car):
    brand = "Peugeot"


class Character:
    health = 100
    mana = 100

    def walk(self):
        pass

    def jump(self):
        pass


class Wizard(Character):

    def do_fireball(self):
        self.mana -= 10
        return "FIREBALL"


class Necromancer(Wizard):

    def raise_skeleton(self):
        self.mana -= 20
        return "SKELETON"


# car = Car(brand="Peugeot", model="205")
#
# # Change property of a class
# car.color = "blue"

# print(BMW.get_car_brand_info())
# print(BMW.get_brand_info())

bmw = BMW(model="530")
audi = Audi(model="A6")

# BMW object brand
bmw.brand = "MWB"
print('BMW OBJECT BRAND:', bmw.get_car_brand_info())

# BMW class brand
print('BMW CLASS BRAND:', bmw.get_brand_info())

# DEFAULT
# car.print_info()

# BMW
bmw.print_info()

bmw.engine_turn_on()
bmw.print_engine_status()

bmw.engine_turn_off()
bmw.print_engine_status()

# Audi
audi.print_info()
audi.sound_alarm(mins=10)
