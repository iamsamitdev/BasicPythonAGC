import time

num = 0
count = 1

while True:
    print(f"Round {count} = {num}")
    num = 0 if num == 1 else 1
    # เมื่อครบ 20 รอบให้หยุดออกจาก loop
    if count == 20:
        break
    # ครบ 1 รอบทำการ sleep 1 วินาที
    time.sleep(1)
    # เพิ่มรอบ
    count = count + 1
