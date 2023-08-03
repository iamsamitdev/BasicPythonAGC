# การสร้างฟังก์ชันแบบไม่มี return
def hello():
    print('Hello Python')


# เรียกใช้งานฟังก์ชันที่สร้างไว้
hello()


# สร้างฟังก์ชันแบบมีการับค่า
def info(msg):
    print("Welcome to", msg)


# เรียกใช้งานฟังก์ชัน info
info("AGC Team")


# ฟังก์ชันแบบมีการรับค่าและมี return ค่า
def area(width, height):
    return width * height


# เรียกใช้งานฟังก์ชัน area
print("Area is", area(10, 20))


# สร้างฟังก์ชันแบบมีการกำหนดค่าเริ่มต้นให้ argument
def show_info(name="", salary=0, lang=""):
    print('Name:', name)
    print('Salary:', salary)
    print('Language:', lang)


# เรียกใช้ฟังก์ชัน show_info
show_info()
show_info("Samit")
show_info("Samit", 100000, "Java")
