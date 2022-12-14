# ลองเขียนโปรแกรมรับค่า username และ password

print("Please Enter Username and Password")

# การรับค่าด้วยฟังก์ชัน input()
username = input("Username:")
password = input("Password:")

# print(username)
# print(password)

# เขียนเงื่อนไขตรวจสอบว่าป้อน username และ password ถูกต้องหรือไม่
if (username == "admin" and password == "1234"):
    print("Login Success")
else:
    print("Login Fail")
