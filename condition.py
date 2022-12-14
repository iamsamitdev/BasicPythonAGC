# การเขียนเงื่อนไข if esle elif
print("Please select game level")

# ค่าที่รับมาจากฟังก์ชัน input จะเป็น string ทั้งหมด
level = input("Enter level 1-4: ")

if (level == '1'):
    print("Easy Level")
elif (level == '2'):
    print("Medium Level")
elif (level == '3'):
    print("Hard Level")
elif (level == '4'):
    print("Expert Level")
else:
    print("Invalid Level Selected")


# เงื่อนแบบ ternary
x, y = 50, 25

small = x if x < y else y

print(small)
