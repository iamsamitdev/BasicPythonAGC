# ตัวอย่างการเขียน loop ด้วยคำสั่ง while

for i in range(1, 101):
    if i % 10 == 0:
        print(f"{i:03}")
    else:
        print(f"{i:03}", end=" ")
# Infinity Loop
while True:
    print("OK")
