import random

class halaman:
    def __init__(self, list):
        self.list = list
    def get_nama(self):
        return self.list

print ("")
print ("( BOT_HYDRA_AI )")
print ("()")
print ("{ Ai Dalam Pengembangan }")
print ("()")
print ("{ { Bot Hydra Ai By Neoyxann } }")
print ("()")
print ("")
list_bot = [":::> Program Kalkuator", "::> Panggil Program Kalkulator Dengan Input ( Kalkulator )", ":> Contoh : ( Buka Kalkulator )", "", ":::> Program Angka Perpangkatan", "::> Panggil Program Angka Perpangkatan Dengan Input ( Angka Perpangkatan )", ":> Contoh ( Buka Angka Perpangkatan Atau Buka Pangkat )", "", ":::> Program Game", "::> Panggil Program Game Dengan Input ( Game )", ":> Contoh ( Buka Game )", "", ":::> Lainnya ( Hai, Hallo, Assalammualaikum, Apa Kabar )"]
list_hasil = halaman (list_bot)
list_per = list_hasil.get_nama()
for a in list_per:
    print (a)
print ("")
def get_kalkulator():
    print ("")
    print (":> Masukkan Angka Pertama Atau 0 Untuk Selesai")
    angka1 = int(input ("> "))
    if angka1 == 0:
        print ("")
        print ("( Program Telah Dihentikan )")
        print ("")
        quit()
    print (":> Masukkan Operator ( x : + - ) Atau q Untuk Selesai")
    operator = input ("> ")
    if operator == "q" or operator == "Q":
        print ("")
        print ("Program Telah Dihentikan")
        print ("")
        quit()
    print (":> Masukkan Angka Kedua Atau 0 Untuk Selesai")
    angka2 = int(input ("> "))
    if angka2 == 0:
        print ("")
        print ("( Program Telah Dihentikan )")
        print ("")
        quit()
    print ("")
    if "x" in operator:
        hasil = lambda a, b : a * b
        print (f"::> ( {angka1} {operator} {angka2} = {hasil(angka1, angka2)} )")
    elif ":" in operator:
        hasil = lambda a, b : a / b
        print (f"::> ( {angka1} {operator} {angka2} = {hasil(angka1, angka2)} )")
    elif "+" in operator:
        hasil = lambda a, b : a + b
        print (f"::> ( {angka1} {operator} {angka2} = {hasil(angka1, angka2)} )")
    elif "-" in operator:
        hasil = lambda a, b : a - b
        print (f"::> ( {angka1} {operator} {angka2} = {hasil(angka1, angka2)} )")
    else:
        print ("Masukkan Input Yang Benar")
    print ("")

def get_game():
    print ("")
    angka_random = range (1, 100+1)
    komputer = random.choice(angka_random)
    print (":> Masukkan Angka Dari 1-100 Atau 0 Untuk Selesai")
    pilihanku = int(input ("> "))
    if pilihanku > 100:
        print ("")
        print ("( Masukkan Angka Yang Benar Dari 1-100, Silankan Ulangi Dari Awal )")
        print ("")
        quit()
    elif pilihanku == 0:
        print ("")
        print ("( Program Telah Dihentikan )")
        print ("")
        quit()
    elif pilihanku > komputer:
        print ("")
        print (f"Angka Pilihanmu = {pilihanku}")
        print (f"Angka Pilihan Komputer = {komputer}")
        print ("")
        print (f"( Kamu Menang Didalam Permainan Dengan Angka Terbesar = {pilihanku} ) ")
        print ("")
    elif pilihanku < komputer:
        print ("")
        print (f"Angka Pilihanmu = {pilihanku}")
        print (f"Angka Pilihan Komputer = {komputer}")
        print ("")
        print (f"( Kamu Kalah Didalam Permainan Dengan Angka Terkecil = {pilihanku} ) ")
        print ("")

def get_perpangkatan():
    print ("")
    print ("Angka Perpangkatan")
    print ("")
    print (":> Masukkan Angka Yang Ingin Dipangkatkan Atau 0 Untuk Selesai")
    angka1 = int(input("> "))
    if angka1 == 0:
        print ("")
        print ("( Program Telah Dihentikan )")
        print ("")
        quit()
    print (":> Dipangkatkan Berapa")
    angka2 = int(input("> "))
    if angka1 == 0:
        print ("( Program Telah Dihentikan )")
    print ("")
    print (f"::> ( {angka1} ^ {angka2} = {pow(angka1, angka2)} )")
    print ("")

def bot_hydra_ai():
    bot = input ("> ")
    if "kalkulator"  in bot or "Kalkulator" in bot:
        try:
            get_kalkulator()
        except ValueError:
            print ("")
            print ("( Masukkan Angka Yang Benar, Silahkan Ulangi Dari Awal)")
            print ("")
    elif "pangkat" in bot or "Pangkat" in bot or "Angka Perpangkatan" in bot or "angka perpangkatan" in bot:
        try:
            get_perpangkatan()
        except ValueError:
            print ("")
            print ("( Masukkan Angka Yang Benar, Silahkan Ulangi Dari Awal )")
            print ("")
    elif "Game" in bot or "game" in bot:
         try:
            get_game()
         except ValueError:
             print ("")
             print ("( Masukkan Angka Yang Benar Dari 1-100, Silahkan Ulangi Dari Awal )")
             print ("")
    elif "Hallo" in bot or "hallo" in bot:
        print (":> Hallo User")
    elif "Hai" in bot or "hai" in bot:
        print (":> Hai User")
    elif "Assalammualaikum" in bot or "assalammualaikum" in bot:
        print (":> Waalaikumsalam")
    elif "kabar" in bot or "Kabar" in bot:
        print (":> Alhamdulillah Baik2 Saja")

while True:
    bot_hydra_ai()
    
