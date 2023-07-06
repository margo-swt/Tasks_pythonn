def nested_loop():
    for i in range(1, 11):
        for j in range(10):
            num = (i - 1) * 10 + (j + 1)
            print(num)


nested_loop()
