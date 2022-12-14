import pymysql
from dbpackage import connectmysql as con


# สร้างฟังก์ชันสำหรับการสร้างตารางเข้าไปในฐานข้อมูล
def add_person(name, weight, height):
    connection = con.connectdb()
    cursor = connection.cursor()

    # เขียนคำสั่ง sql สำหรับสร้างตารางใหม่
    sql = f"INSERT INTO person(fullname,weight,height) VALUES('{name}','{weight}','{height}')"

    try:
        cursor.execute(sql)
        connection.commit()
        print('Add person success')
    except pymysql.error:
        print(pymysql.error)


# เรียกใช้งาน
name = input('What is your name ?:')
weight = input('Weight ?:')
height = input('Height ?:')

add_person(name, weight, height)
