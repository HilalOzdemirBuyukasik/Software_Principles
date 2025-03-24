
# WET (Write Everything Twice) - Calculate the area of a rectangle and a square.
def calculate_rectangle_area(lenght, width):
    return lenght * width

def calculate_square_area(side):
    return side * side

lenght = float(input('Dikdörtgen için uzunluk giriniz: '))
width = float(input('Dikdörtgen için genişlik giriniz: '))
side = float(input('Karenin kenarını giriniz: '))

rectangle_area = calculate_rectangle_area(lenght,width)
square_area = calculate_square_area(side)

print(f'Dikdörtgen Alanı: {rectangle_area} dir.!')
print(f'Karenin alanı: {square_area} dır.!')


