from myTask import add

data = countTweets.delay(time=30)
print(data.get(propagate=False))