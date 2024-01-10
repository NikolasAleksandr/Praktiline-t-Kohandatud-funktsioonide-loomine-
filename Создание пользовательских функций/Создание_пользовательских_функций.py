#Praktiline töö "Kohandatud funktsioonide loomine"

#1
def arithmetic():
    num1 = float(input("Sisesta esimene arv: "))
    num2 = float(input("Sisesta teine arv: "))
    op = input("Sisesta tehe (+, -, *, /): ")

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Viga: nulliga jagamine"
    else:
        return "Tundmatu tehe"

result = arithmetic()
print(result)

#2
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

user_input = input("Sisesta aasta: ")

try:
    year_to_check = int(user_input)
    result = is_year_leap(year_to_check)

    if result:
        print(f"{year_to_check} on liigaasta.")
    else:
        print(f"{year_to_check} ei ole liigaasta.")
except ValueError:
    print("Viga: Palun sisestage korrektne aasta arv.")
    
#3
import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    
    return perimeter, area, diagonal

side_length = float(input("Sisestage ruudu külje pikkus: "))

perimeter, area, diagonal = square(side_length)

print(f"Ruudu ümbermõõt: {perimeter}")
print(f"Ruudu pindala: {area}")
print(f"Ruudu diagonaal: {diagonal}")

#4 

def season(month):
    if month in (1, 2, 12):
        return "talv" 
    elif month in (3, 4, 5):
        return "kevad" 
    elif month in (6, 7, 8):
        return "suvi"  
    elif month in (9, 10, 11):
        return "sügis"  
    else:
        return "Vigane kuu" 

kuu = int(input("Sisestage kuu number (1-12): "))

result = season(kuu)

print(f"Kuu {kuu} kuulub aastaaega: {result}")

#5
def bank(a, years):
    interest_rate = 0.10  
    total_amount = a  

    for year in range(1, years + 1):
        total_amount += total_amount * interest_rate

    return total_amount

algne_hoius = float(input("Sisestage hoiuse suurus eurodes: "))
hoius_aastad = int(input("Sisestage hoiuse periood aastates: "))

tulemus = bank(algne_hoius, hoius_aastad)

print(f"{hoius_aastad} aasta pärast on teie kontol {tulemus:.2f} eurot.")


#6
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num_to_check = int(input("Sisestage number vahemikus 0 kuni 1000: "))

if 0 <= num_to_check <= 1000:
    result = is_prime(num_to_check)
    if result:
        print(f"{num_to_check} - on algarv.")
    else:
        print(f"{num_to_check} - ei ole algarv.")
else:
    print("Sisestage number vahemikus 0 kuni 1000.")
    

#7
def is_valid_date(day, month, year):
    if month < 1 or month > 12:
        return False
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month]:
        return False
    
    if year < 1:
        return False
    
    return True

day_input = int(input("Sisestage päev: "))
month_input = int(input("Sisestage kuu: "))
year_input = int(input("Sisestage aasta: "))

result = is_valid_date(day_input, month_input, year_input)

if result:
    print("Kuupäev on meie kalendris kehtiv.")
else:
    print("Kuupäev ei ole meie kalendris kehtiv.")


#8
def XOR_cipher(text, key):
    return ''.join(chr(ord(char) ^ ord(key)) for char in text)

def XOR_uncipher(encrypted_text, key):
    return XOR_cipher(encrypted_text, key)  

original_text = input("Sisestage tekst šifreerimiseks: ")
encryption_key = input("Sisestage krüptovõti: ")

encrypted_result = XOR_cipher(original_text, encryption_key)
print(f"Šifreeritud tekst: {encrypted_result}")

decrypted_result = XOR_uncipher(encrypted_result, encryption_key)
print(f"Dešifreeritud tekst: {decrypted_result}")







