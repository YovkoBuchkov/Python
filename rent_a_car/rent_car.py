def initialize_cars():
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True},
        {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": True},
        {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price": 55, "available": True},
        {"id": 4, "brand": "Tesla", "model": "XL", "rental_price": 100, "available": True},
        {"id": 5, "brand": "Mecendes", "model": "AMG", "rental_price": 135, "available": True},
        {"id": 6, "brand": "Ferary", "model": "Testarossa", "rental_price": 255, "available": True},
    ]
    return cars


def rent_car(cars, car_id):
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"You have rented the {car['brand']} {car['model']}."
    return "Car is unavailable or invalid car ID."


def return_car(cars, car_id, rental_days):
    for car in cars:
        if car["id"] == car_id and not car["available"]:
            car["available"] = True
            total_cost = rental_days * car["rental_price"]
            return f"You returned the {car['brand']} {car['model']}. Total cost: ${total_cost}"
    return "Invalid car ID or the car is not currently rented."



def display_cars(cars):
    print("\nAvailable Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")


def validate_car_id(cars, car_id):
    for car in cars:
        if car["id"] == car_id:
            return True
    return False


def validate_option(option, valid_options):
    return option in valid_options


def main_menu():
    print("\nWelcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return input("Please choose an option (1-4): ")


def rent_a_car(cars):
    try:
        car_id = int(input("Enter the car ID you want to rent: "))
        if validate_car_id(cars, car_id):
            print(rent_car(cars, car_id))
        else:
            print("Invalid car ID.")
    except ValueError:
        print("Please enter a valid numeric ID.")


def return_a_car(cars):
    try:
        car_id = int(input("Enter the car ID you want to return: "))
        if validate_car_id(cars, car_id):
            rental_days = int(input("How many days did you rent the car? "))
            print(return_car(cars, car_id, rental_days))
        else:
            print("Invalid car ID.")
    except ValueError:
        print("Please enter valid input.")


def car_rental_system():
    cars = initialize_cars()

    while True:
        option = main_menu()
        if validate_option(option, ['1', '2', '3', '4']):
            if option == '1':
                display_cars(cars)
            elif option == '2':
                rent_a_car(cars)
            elif option == '3':
                return_a_car(cars)
            elif option == '4':
                print("Thank you for using RentACar! Goodbye!")
                break
        else:
            print("Please select a valid option (1-4).")


car_rental_system()
