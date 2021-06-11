# ----------------------------------------------------------------------------------------
# 1. Zamiana wartosciami dwoch zmiennych
# ----------------------------------------------------------------------------------------

# Sposob 1
x = 10
y = 20

print("------------------------------------------ 1 -------------------------------------")
print('Sposob 1')
print(f'x = {x} y = {y}')
temp = x
x = y
y = temp
print(f'x = {x} y = {y}')

# Sposob 2
print('Sposob 2')
print(f'x = {x} y = {y}')
y, x = x, y
print(f'x = {x} y = {y}')

# ----------------------------------------------------------------------------------------
# 2. Przypisywanie wartosci z wykorzystaniem instrukcji if
# ----------------------------------------------------------------------------------------

print("------------------------------------------ 2 -------------------------------------")
is_adult = True

# Sposob 1
if is_adult:
    message = 'ADULT'
else:
    message = 'NOT ADULT'

print(message)

# Sposob 2
message = 'ADULT' if is_adult else 'NOT ADULT'
print(message)

# ----------------------------------------------------------------------------------------
# 3. Wyluskiwanie wartosci z tuple
# ----------------------------------------------------------------------------------------

person = ('JOHN', 'BLACK', 23, 183, 76.5)
name, surname, age, height, weight = person
print(f'Name: {name} Surname: {surname} Age: {age} Height: {height} Weight: {weight}')

name, surname, *numbers = person
print(numbers)

name, surname, age, *_ = person  # wyluskanie tylko 3 pierwszych elementow
print(f'Name: {name} Surname: {surname} Age: {age}')


# ----------------------------------------------------------------------------------------
# 4. Odwracanie napisu
# ----------------------------------------------------------------------------------------
city = 'London'
print(city)
print(city[::-1])

# ----------------------------------------------------------------------------------------
# 5. Przejscie z listy napisow na pojedynczy napis
# ----------------------------------------------------------------------------------------
print(''.join(['A', 'B', 'C']))

# ----------------------------------------------------------------------------------------
# 6. Wykorzystanie enums z przypisanymi wartosciami
# ----------------------------------------------------------------------------------------
class Color:
    Red, Green, Blue = range(3)

print(Color.Red)
print(Color.Green)
print(Color.Blue)


class ColorStr:
    Red, Green, Blue = ["RED", "GREEN", "BLUE"]

print(ColorStr.Red)
print(ColorStr.Green)
print(ColorStr.Blue)


# ----------------------------------------------------------------------------------------
# 7. Najczesciej wystepujaca wartosc w liscie
# ----------------------------------------------------------------------------------------
elements = [1, 2, 2, 3, 1, 1, 1, 3, 3, 1, 1, 1]
print(max(set(elements), key=elements.count))

# ----------------------------------------------------------------------------------------
# 8. Sprawdzenie ile miejsca w pamieci zajmuje obiekt
# ----------------------------------------------------------------------------------------
import sys
print(sys.getsizeof(elements))


