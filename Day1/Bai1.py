# CÂU LỆNH PRINT TRONG PYTHONG
# cú pháp  printf(object, sep = seperator, end = end ) 

"""
sep là phân cách các đối tượng khi in, nếu không có thì  mặc định là dấu cách
end là kí tự khi được in ra khi ở cuối dòng nếu không có thì mặc định là xuống dòng 
"""
print("python","java","javascript",end="!\n")


#CHÚ THÍCH TRONG PYTHON
#đây là chú thích 1 dòng 
"""
đây là chú thích nhiều dòng
"""

#BIẾN VÀ KIỂU DỮ LIỆU TRONG PYTHON
#biến
""" 
không được đặt tên biến có chứa dấu cách,kí tự đặc biệt ,bắt đầu bằng chữ số
biến trong python có phân biệt chữ hoa chữ thường
"""


#kiểu dữ liệu 

"""
Kiểu dữ liệu số 
Trong python có 3 kiểu dữ liệu số :số nguyên (interger), số thực dấu phẩy động (float), số phức (complex)
a=100(int)
b=5.2(float)
c=5 + 3j(complex)


Số thực
Trong python thường thì các số nguyên được in ra  dưới dạng cơ số 10 nhưng bạn cũng có thể in ra  các số ở hệ 2,8,16
In số thực với số lượng chữ sau dấu phẩy xác định


Số phức 
Trong python có thể trích xuất số thực và số ảo của biến số phức x theo cách sau : số thực =x.real , số ảo=x.imag 


Kiểu dữ liệu đúng sai 
print(bool(values)) => output:true or false , false là chuỗi rỗng hoặc là số 0


Kiểu dữ liệu xâu kí tự:
Trong Python xâu kí tự được đặt trong nháy đơn hoặc nháy kép trên 1 dòng, trong trường hợp xâu có nhiều dòng ta đặt trong 3 nháy kép


Ép kiểu dữ liệu :
int()
float()
str()
"""
a=28.0412323
print("%.2f" % a)
print(round(a,2))
print("{:.2f}".format(a))
#lấy 2 chữ số sau dấu phẩy

#số phức
x= 5+3j
print(x.imag)
print(x.real)


print(bool("")) #false
print(bool("phuc"))#true

a="123"
b=int(a)
print(type(b)) #int


