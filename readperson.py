import pymysql
from dbpackage import connectmysql as con


# สร้างฟังก์ชันสำหรับการอ่านข้อมูลจากตาราง person
def read_person():
    connection = con.connectdb()
    cursor = connection.cursor()

    # เขียนคำสั่ง sql สำหรับสร้างตารางใหม่
    sql = "SELECT * FROM person ORDER BY id DESC"

    try:
        cursor.execute(sql)
        connection.commit()

        for row in cursor:
            print("ID:", row['id'])
            print("Fullname:", row['fullname'])
            print("Weight:", row['weight'])
            print("Height:", row['height'])
            print("------------------------")
    except pymysql.error:
        print(pymysql.error)


# เรียกใช้งาน
read_person()
