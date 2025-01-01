#'Day 2: 30 Days of python programming'

first_name = "Camilo"
print(first_name)
print(type(first_name))
print(len(first_name))

last_name = "Alvarez"
print(last_name)
print(type(last_name))
print(len(last_name))

# we are compare the length of the first name and the last name 

if len(first_name)==   len(last_name):
    print("the length is the same")

elif len(first_name)> len(last_name):
    print("the fisrt name is longest than the last name")

else:
    print("the last name is longest than the first name ")

full_name = "Camilo Alvarez"
print(full_name)
print(type(full_name))

countrie = "Colombia"
print(countrie)
print(type(countrie))

city= "Medellin"
print(city)
print(type(city))

age = 18
print(age)
print(type(age))

year = 2024
print(year)
print(type(year))


is_married = False
print(is_married)
print(type(is_married))

is_true = True
print(is_true)
print(type(is_true))

is_ligth_on = True
print(is_ligth_on)
print(type(is_ligth_on))

num1, num2, num3, num4, num5 = 1, 4, 5, 5.6, 7.6
print(num1, num2, num3, num4, num5)
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))

num_one = 5

num_two = 4

total_variable = num_one + num_two
print(total_variable)

diff_variable = num_one-num_two
print (diff_variable)

product_variable = num_one*num_two
print(product_variable)

division_variable = num_one/num_two
print(division_variable)

remainder_variable = num_one % num_two
print(remainder_variable)

exp_variable = num_one**num_two
print(exp_variable)

floor_division_variable = num_one//num_two
print(floor_division_variable)

radius = 30
area_circle = 3.14*(radius*radius)
print(area_circle)

circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

radius = int(input("choose the radius you want "))
area_circle = 3.14*(radius*radius)
print(area_circle)

first_name = input("write your first name:")
print(first_name)

last_name = input("write your last name: ")
print(last_name)

countrie = input("write the countrie that do you from")
print(countrie)

city= input("write the city thah do you live")
print(city)

age = input("write your age")
print(age)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)