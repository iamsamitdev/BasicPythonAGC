# การ import ฟังก์ชันจากภายนอกมาใช้
# การ import ทั้งหมด
import numberx

# การ import มาบางฟังก์ชัน
from numberx import factorial, fibonacci
# from numbers import *

# การ import และเปลี่ยนชื่อ
from numberx import factorial as ft, fibonacci as fb

# การ import จาก package numberpackage
from numberpackage import calculate as cl, number as nb

print(cl.plus(5, 10))
print(nb.factorial(5))
print(nb.fibonacci(100))

print('-----------------------------------------')

print(numberx.factorial(5))
print(numberx.fibonacci(100))

print('-----------------------------------------')

print(factorial(5))
print(fibonacci(100))

print('-----------------------------------------')

print(ft(5))
print(fb(100))
