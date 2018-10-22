from myTask import add

data = add.delay(4, 3)
print(data.get(propagate=False))