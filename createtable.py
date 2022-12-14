import pymysql
from dbpackage import connectmysql as con


# สร้างฟังก์ชันสำหรับการสร้างตารางเข้าไปในฐานข้อมูล
def create_table():
    connection = con.connectdb()
    cursor = connection.cursor()

    # เขียนคำสั่ง sql สำหรับสร้างตารางใหม่
    sql = """
        CREATE TABLE person(
            id int PRIMARY KEY AUTO_INCREMENT,
            fullname varchar(255),
            weight float,
            height float
        )
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print('Create table person success')
    except pymysql.error:
        print(pymysql.error)


# เรียกใช้งาน
create_table()
