class Membuatfile:
    def __init__ (self, namafile):
        self.namafile = namafile
    def get_file(self):
        print ("")
        return "File Berhasil Dibuat Dengan Nama File" + " " + self.namafile

print ("")
print ("Membuat File")
print ("")
print ("Masukkan Nama File")
namafile = input ("> ")
print ("Masukkan Extensi File")
ex = input ("> ")
print ("Masukkan Isi File")
isifile = input ("> ")
file = open(namafile+"."+ex, "w")
file.write(str(isifile))
semuanya = Membuatfile(namafile)
print (semuanya.get_file())
print ("")