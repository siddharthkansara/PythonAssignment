#temperature table


Fahrenheit = list(range(0,100,5))

Celsius = [(round(((i - 32) * 5/9),2)) for i in Fahrenheit]

temp_table1 = list(zip(Fahrenheit,Celsius))

print(temp_table1)

Celsius_1 = list(range(-10,50,2))

Fahrenheit_1 = [(round(((i * 9/5) + 32),2)) for i in Celsius_1]

temp_table2 = list(zip(Celsius_1,Fahrenheit_1))

print(temp_table2)