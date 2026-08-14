

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a = b
    b = a + b


# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

new_list=[]
for i in range(5):
    new_list.append(i)
print(new_list)

print(list(range(5,10)))

print(list(range(0,30,3)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(sum(range(4)))  # 0 + 1 + 2 + 3

print("--------------------------")

def http_error(status):
    match status:
        case 400:
            return print("Bad request")
        case 404:
            return print("Not found")
        case 418:
            return print("I'm a teapot")
        case _:
            return print("Something's wrong with the internet")

http_error(500)



class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [Point(2, 4), Point(3, 7)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case[Point(x1, 0), Point(x2, 0)]:
        print(f"Two points on the X axis at {x1}, {x2}")
    case[Point(x1, y1), Point(x2, y2)]:
        print(f"Two arbitrary points: {x1}, {y1} and {x2}, {y2}")
        print(f"This is the distance betwween the two points: {((x2-x1)**2 + (y2-y1)**2)**0.5}")
    case _:
        print("Something else")



class Araba:
    def __init__(self, marka, renk, tramer, hiz):
        self.marka = marka
        self.renk = renk
        self.tramer = tramer
        self.hiz = hiz

    def bilgileri_goster(self):
        print(f"Marka: {self.marka}, Renk: {self.renk}, Tramer: {self.tramer}")

    def hızlan(self, miktar):
        self.hiz = self.hiz + miktar
        print(f"{self.marka} hızlandı. Yeni hız: {self.hiz}")

    def fren_yap(self, miktar):
        self.hiz = self.hiz - miktar
        if self.hiz < 0:
            self.hiz = 0
        print(f"{self.marka} fren yaptı. Yeni hız: {self.hiz}")


              


araba1 = Araba("Toyota", "Beyaz", 2, 0)
araba2 = Araba("Honda", "Siyah", 3, 0)
araba3 = Araba("Bentley", "Mat Siyah", 0, 0)

araba1.hızlan(50)
araba2.hızlan(60)
araba2.fren_yap(20)
araba1.fren_yap(60)

print(araba1.marka, araba1.renk)
print(araba2.marka, araba2.renk)
print(araba3.renk, araba3.marka)

print("Toyota'nın", araba1.tramer,"tramer puanı vardır.")

araba1.bilgileri_goster()

araba2.bilgileri_goster()

araba3.bilgileri_goster()

print(araba1.hiz)
print(araba2.hiz)



class Ogrenci:

    ogrenci_sayisi = 0

    def __init__(self, ad, puan):
        self.ad = ad
        self.puan = puan
        Ogrenci.ogrenci_sayisi += 1
ogrenci1 = Ogrenci("Ali", 90)
ogrenci2 = Ogrenci("Ayşe", 85)
ogrenci3 = Ogrenci("Engin", 25)
ogreci4 = Ogrenci("Ahmet", 100)
ogrenci5 = Ogrenci("Mehmet", 75)

print(Ogrenci.ogrenci_sayisi)

class Kitap:
    def __init__(self, isim, yazar):
        self.isim = isim
        self.yazar = yazar

    def __str__(self):
        return f"{self.isim} - {self.yazar}"

kitap = Kitap( "Falci","Stephen King")

print(kitap.isim)
print(kitap.yazar)

print(kitap)

class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self._bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar <= 0:
            print("Yatırılan para pozitif olmalıdır.")
            return

        self._bakiye += miktar

    def para_cek(self, miktar):
        if miktar <= 0:
            print("Çekilecek para pozitif olmalıdır.")
        elif miktar > self._bakiye:
            print("Yetersiz bakiye.")
        else:
            self._bakiye -= miktar

    def bakiye(self):
        return self._bakiye

hesap = BankaHesabi("Ayşe", 1000)

hesap.para_yatir(500)
hesap.para_cek(200)

print(hesap.bakiye())

class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    def bilgi_ver(self):
        print(f"Hayvanın ismi: {self.isim}, Yaşı: {self.yas}")

class Kedi(Hayvan):
    def __init__(self, isim, yas, renk):
        super().__init__(isim, yas)
        self.renk = renk

    def bilgi_ver(self):
        print(
              f"İsim: {self.isim},"
              f"Yaş: {self.yas},"
              f"Renk: {self.renk}"
        )

kedi = Kedi("Misket", 3, "Gri")
kedi.bilgi_ver()

class Hayvan:
    def ses_cikar(self):
        print("Hayvan ses çıkardı.")

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav!")


class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav hav!")

kedi = Kedi()
kopek = Kopek()

kedi.ses_cikar()
kopek.ses_cikar()


class Kullanici:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    @classmethod
    def metinden_olustur(cls, metin):
        isim, yas = metin.split(",")
        return cls(isim, int(yas))

kullanici = Kullanici.metinden_olustur("Emir,23")

print(kullanici.isim)
print(kullanici.yas)

class Motor:
    def calistir(self):
        print("Motor calisti.")


class Araba:
    def __init__(self, marka):
        self.marka = marka
        self.motor = Motor()

    def calistir(self):
        print(f"{self.marka} calistiriliyor...")
        self.motor.calistir()

araba= Araba("Nissan")
araba.calistir()


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name= name
    def __str__(self):
        return f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"

vehicle1 = Vehicle("Tesla Model S", 250, 18)

print(vehicle1)

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name= name

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Area = {self.area()}, Perimeter = {self.perimeter()}"

rect = Rectangle(10, 4)

print(rect)

print(f"Area : {rect.area()}, Perimeter = {rect.perimeter()}")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  
    def average(self):
        return sum(self.marks) / len(self.marks)
    def __str__(self):
        return f" {self.name}'s Average Grade: {self.average()}"

s1 = Student("Alice", [85, 90, 78, 92, 88])
print(s1)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Total stock value of {self.name}: ${self.total_value()}"
p1 = Product("Laptop", 899.99, 5)
print(p1)

class Light:

    def __init__(self):
        self.light = False

    def turn_on(self):
        self.light == True
        print("Light is ON")

    def turn_off(self):
        self.light == False
        print("Light is OFF")

    def status(self):
        if self.light:
            print("Current status: ON")
        else:
            print("Current status: OFF")

light = Light()

light.turn_on()
light.status()

light.turn_off()
light.status()


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


with open("notes.txt", "w") as f:
    f.write("Week1 G1 is completed. \n")
    f.write("I got the Python basics.\n") 

with open("notes.txt", "a") as f:
    f.write("I added this with append mode.")

with open("notes.txt", "r") as f:
    icerik = f.read()
    print(icerik)


