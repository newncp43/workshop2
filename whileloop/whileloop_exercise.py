#1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while
i = 2
while i < 13:
    print("    "+"[",i,"]")
    x = 1
    while x < 13:
        print(i, " * ", x, " : " ,i * x)
        x += 1
    print("")
    print("--------------""\n")
    i += 1