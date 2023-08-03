import pymysql


# สร้างฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล mysql
def connectdb():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='1234',
        db='pythondbs',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )


# print(connectdb())
