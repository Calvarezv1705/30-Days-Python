#day 3 of 30 days of python operators
age = 18
heigth = 1.80
complex_number = 1 + 1j

# we are calculating the area of a triangle
base = float(input("ingresa la base: "))
heigth = float(input("ingresa la altura: "))
area_triangle = 0.5*base*heigth
print("el area del triangulo es: ", area_triangle)

# we are calculating the perimeter of a triangle
side_a = float(input("ingresa el lado a: "))
side_b = float(input("ingrese el lado b: "))
side_c = float(input("ingrese el lado c: "))
perimeter_triangle = side_a + side_b + side_c
print("el perimetro del triangulo es: ", perimeter_triangle)

# we are calculating the area ad the perimeter of a rectangle
length = float(input("ingrese el largo del rectangulo: "))
width = float(input("ingrese el ancho del rectangulo: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("el area del rectanguo es: ", area_rectangle)
print("el perimetro del rectangulo es: ", perimeter_triangle)

# we are calculating the area and the circunference of a circule
radius = float(input("ingrese el radio del circulo: "))
area_circle = 3.14 * radius**2
circunference_circle = 2 * 3.14 * radius
print("el area del circulo es: ",area_circle)
print("la circunferencia del circulo es: ", circunference_circle)

# we are calculating the intercept of y
x = 0
y = 2 * x -2
print("el intersecto en el eje y es: ", y)

# we are calculating the slope and the distance 
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 -x1)
distance = ((x2- x1)**2) + ((y2 -y1)**2)
print("la pendiente es: ", slope)
print("la distancia entre los dos puntos es: ", distance)

# we are trying to find what number of x is going to made y = 0
x = 0
y = x**2 + 6*x +9*x
if y == 0:
    print("the value that made y=0 is: ", x)
    print(y)
else: 
    print("the value of ",x, " doesnt made y=0")
    print(y)

# here we are comparing the words with a false comparison 
word_pyton = len("Python")
word_dragon = len("Dragon")
compare_words = word_pyton is not word_dragon
print(compare_words)

# here we are found if the word on is in the both words
word_on = "on"
word_pyton = "Python"
word_dragon = "Dragon"
found_on = word_on in word_pyton and word_on in word_dragon
print(found_on)

# here we are found if the word jargon is in the text
text = "I hope this course is not full of jargon"
word_jargon = "jargon"
found_word = word_jargon in text
print(found_word)

# here we are found if the word on is not in the both words
word_on = "on"
word_pyton = "Python"
word_dragon = "Dragon"
found_on = word_on not in word_pyton and word_on not in word_dragon
print(found_on)

#Find the length of the text python and convert the value to float and convert it to string
word_python = len("python")
convert_float = float(word_python)
print(convert_float)
print(type(convert_float))
convert_str = str(convert_float)
print(convert_str)
print(type(convert_str))

#How do you check if a number is even or not using python?
num = 3
if num % 2 == 0:
    print(num, "es un numero par")
else: 
    print(num, "es un numero impar")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7//3
int_convert = int(floor_division)
its_same = floor_division is int_convert
print(its_same)

#Check if type of '10' is equal to type of 10
num1 = type("10")
num2 = type(10)
same_type = num1 is num2
print(same_type)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = float(input("ingrese las horas que trabajo: "))
rate_per_hour = float(input("ingrese la tarifa por hora: "))
calculate_pay = hour*rate_per_hour
print(calculate_pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year_lived = int(input("ingrese los años que ha vivido: "))
seconds_lived = year_lived * 31536000
print("los segundos que has vivido son: ",seconds_lived)