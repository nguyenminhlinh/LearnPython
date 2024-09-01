import sys
try:
    a = 1 / 0
except:
    print("Ngoại lệ xảy ra là:", sys.exc_info()[0])
try:
    a = 1 / 0
except Exception as e:
    print("Ngoại lệ xảy ra là:", e.__class__)

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Lỗi 1 xảy ra")
except (IndentationError, UnicodeError):
    print("Lỗi 2 xảy ra")
except:
    print("Các lỗi còn lại xảy ra")

try:
    a = 1 / 3
except:
    print("Sai!")
else:
    b = 1 / 0
    print(b)

try:
   file = open("tek4.txt",encoding = 'utf-8')
finally:
   file.close()

   class MyErr(Exception):     
    pass 
while True:     
    try:         
        a = int(input("Nhập điểm sinh viên: "))         
        if a < 0 :             
            raise MyErr         
        else:             
            break     
    except MyErr:         
        print("Điểm số vừa nhập là giá trị âm! Mời nhập lại.") 
                
print("Nhập thành công")

class MyErr(Exception):
    def __init__(self, diem_so, thong_bao="Nhập số điểm sai"):
        self.diem_so = diem_so
        self.thong_bao = thong_bao
        super().__init__(self.thong_bao)

diem_so = int(input("Nhập điểm cho sinh viên: "))
if diem_so < 0:
    raise MyErr(diem_so)