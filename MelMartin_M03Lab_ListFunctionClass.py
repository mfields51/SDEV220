#Define Vehicle Class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Define Automobile class to inherit Vehicle class and add attributes
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
    #Initialize parent class attributes
        super().__init__(vehicle_type)
        #Initialize child attributes
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    #Output
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

#Define Main
def main():
    print("Enter your car information:")

    #User Input, v_type
    while True:
        v_type = input("Enter vehicle type (car, truck, plane, boat, or broomstick): ").lower()
        if v_type in ["car", "truck", "plane", "boat", "broomstick"]:
            break
        print("Please enter car, truck, plane, boat, or broomstick.")

    #User Input, strings    
    year = input("Enter the vehicle year: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the vehicle model: ")

    #User Input, doors
    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Please enter 2 or 4 only.")

    #User Input, roof
    while True:
        roof = input("Enter type of roof (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Please enter 'solid' or 'sun roof'.")

    my_car = Automobile(v_type, year, make, model, doors, roof)

    my_car.display_info()

if __name__ == "__main__":
    main()