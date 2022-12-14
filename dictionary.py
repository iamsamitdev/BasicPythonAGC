# สร้างตัวแปรแบบ Dictionary
scroes = {
    'jame': 1500,
    'jany': 2200,
    'danny': 3500,
}

print(scroes)
print(scroes['jany'])

# เพิ่มสมาชิกใหม่เข้าไปใน dictionary
scroes['thomas'] = 1100
print(scroes)

# เปลี่ยน value ของสมาชิก
scroes['jany'] = 1800
print(scroes)

print("----------------------------")

countries = {
    'de': 'Germany',
    'ua': 'Ukraine',
    'th': 'Thailand',
    'nl': 'Netherlands'
}

print(countries)

print("----------------------------")

# การ loop อ่านสมาชิกทั้งหมดใน dictionary
for k in countries.keys():
    print(k)

print("----------------------------")

for v in countries.values():
    print(v)

print("----------------------------")

for k, v in countries.items():
    print(k, v)
