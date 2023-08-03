# สร้างตัวแปรแบบ List
numbers = [-1, 2, 5, 8, 10, 13]
names = ['samit', 'somkid', 'wichai', 'arnut']

# แสดงผลสมาชิก
print(numbers)
print(numbers[1])
print(numbers[5])

print(names)
print(names[1])
print(names[3])

# นับจำนวนสมาชิก
print(len(numbers))
print(len(names))

# เปลี่ยนสมาชิกของ List
names[1] = "Somchai"
print(names[1])

# การสร้าง List ว่าง
numbers2 = [5, 10, 15, 20]

print(numbers2)

# การอ่านสมาชิกทั้งหมดด้วยการ loop
sum = 0
for n in numbers:
    sum += n
    # print(n)

print(sum)
