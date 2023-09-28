import time

for i in range(100):
    if i % 2 == 0:
        print("foo")
    else:
        print("bar")

for i in range(100):
    if i % 2 == 0:
        print("bar")
    else:
        print("foo")

while True:
    print("hello world")
    time.sleep(10)