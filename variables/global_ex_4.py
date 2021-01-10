x = "awesome"


def myFunc():
    global x # x เท่า awesome
    print("Python is " + x)
    x = "fantastic" # x เปลี่ยนค่า

myFunc()
print("Python is "+ x)