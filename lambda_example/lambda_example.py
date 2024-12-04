for key, value in sorted(stored_names.items(), key=lambda x: x[0]):
    print(f"{key} - {value['health']} health, {value['damage']:.2f} damage")
################################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_number = list(filter(lambda x: x % 2 == 0, numbers))

print(even_number)  #[2, 4, 6, 8]
################################################################

max_value = lambda x, y: x if x > y else y

print(max_value(10, 20))  #20

################################################################

square = lambda x: x ** 2

print(square(5))  #25

################################################################
movies = [
    (1994, 'The Shawshank Redemption', 9.2),
    (1999, 'Fight Club', 8.8),
    (1994, 'Pulp Fiction', 8.9),
    (1972, 'The Godfather', 9.2),
    (2008, 'The Dark Knight', 9.0)
]

movies = sorted(movies, key=lambda movie: movie[2], reverse=True)

for movie in movies:
	print(movie)
################################################################

is_even = lambda num: num % 2 == 0

print(is_even(10))  #True
print(is_even(20))  #True
print(is_even(15))  #False

################################################################


cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True},
    {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": True},
    {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price": 55, "available": True},
    {"id": 4, "brand": "Tesla", "model": "XL", "rental_price": 100, "available": True},
    {"id": 5, "brand": "Mecendes", "model": "AMG", "rental_price": 135, "available": True},
    {"id": 6, "brand": "Ferary", "model": "Testarossa", "rental_price": 255, "available": True},
]

sorted_cars = sorted(cars, key=lambda car: car['rental_price'])
for car in sorted_cars:
	print(car)

################################################################

repeat_str = lambda string, n: string * n

input_str = input()
counter = int(input())
result = repeat_str(input_str, counter)
print(result)

################################################################
add = lambda x,y : x + y
result = add(3,4)
print(result)

################################################################

square = lambda x: x ** 2
result = square(5)
print(result)

################################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_number = list(filter(lambda x: x % 2 == 0, numbers))

print(even_number)  #[2, 4, 6, 8]

################################################################
my_list = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, my_list))
print(result)  #[1, 4, 9, 16, 25]

################################################################
my_list = [1, 2, 3, 4, 5]
result = reduce(lambda x,y: x * y, my_list)
print(result)  #120

################################################################