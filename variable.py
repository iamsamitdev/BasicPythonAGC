# การสร้างตัวแปรใน python ไม่ต้องระบุชนิดข้อมูล
a = 3
b = 4.9572
c = "Python Programming"

print(a)
print(b+20)
print(c)

print(a, b, c)

# สามารถสร้างหลายตัวแปรในบรรทัดเดียว
x = y = z = 10
j, k, m = 5, 10, 15

print(x, y, z)
print(j, k, m)

# Boolean
status = True  # 1
msg = False  # 0

print(status, msg)

print(status == 1)
print(msg == 0)

# การแสดงข้อความร่วมตัวแปร
# วิธีที่ 1
print("Product price", "{:.2f}".format(b), "Bath")

# วิธีที่ 2
print("Product price %.2f Bath" % b)

# วิธีที่ 3
print(f"Product price {b:.2f} Bath")
