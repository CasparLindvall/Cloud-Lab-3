from celery import Celery
import tarfile, json
import timeit

# To ge the run time
start = timeit.default_timer()

app = Celery('tasks', backend='rpc://', broker='amqp://localhost//')

def getVals():
    #total tweets searched
    tweetCounter = 0

    # Words to count
    model = {
        "han": 0,
        "hon": 0,
        "den": 0,
        "det": 0,
        "hen": 0,
        "denna": 0,
        "denne": 0
    }
    return tweetCounter, model

# Characters to potentially remove, though inefficient method
def removeChar( source ):
    source = source.replace( '?', ' ' )
    source = source.replace( '!', ' ' )
    source = source.replace( ";", ' ' )
    source = source.replace( " '", ' ' )
    source = source.replace( "' ", ' ' )
    source = source.replace( ".", ' ' )
    source = source.replace( ",", ' ' )
    source = source.replace( "\"", ' ' )
    source = source.replace( "(", ' ( ' )
    source = source.replace( ")", ' ) ' )
    source = source.replace( '\r', ' ' )
    source = source.replace( '\t', ' ' )
    source = source.replace( '\n', ' ' )
    return source

# Words to potentially remove
#stopWords = open("stopwords.txt").read().splitlines()

# Format for easier
def formatStr(source):
    source = source.replace('\n\n', '\n' )
    source = source.lower()
    sourceArr = source.splitlines()
    #[word for word in tokenized_words if word not in stop_words]
    return sourceArr

@app.task
def countTweets(time=0):
    f = None
    tweetCounter, model = getVals()
    timeStart = timeit.default_timer()
    tar = tarfile.open("data.tar.gz", "r:gz")
    for member in tar.getmembers():
        f = tar.extractfile(member)
        if f:
            content = f.read()
            contentArr = formatStr(content)
            for tweetString in contentArr:
                tweetDict = json.loads(tweetString)
                tweetText = tweetDict["text"].encode("utf-8")
                tweetText = removeChar(tweetText)
                #tweetText = [word for word in tweetText if word not in stopWords]
                for word in tweetText.split():
                    if word in model:
                        model[word] += 1
            tweetCounter += len(contentArr)

            for word, occ in model.items():
                print(word + "\t: " + str(occ)+ "\t" + "{0:.2f}".format(occ/float(tweetCounter)*100)+"%"+" of tweets")
        
        currTime = timeit.default_timer()
        print('Time: ' + "\t{0:.2f}".format(currTime - start) +"\tTweets counted: "+ str(tweetCounter))
        print("")
        if(time and (time - (currTime - timeStart)) < 0):
            print("max time transpired, exiting")
            break
    return tweetCounter, model

tweetCounter, model = countTweets()

# For printing values
y = []
x_label = []
for word, occ in model.items():
    y.append(occ)
    x_label.append(word)

print("Collected data. May be used for plotting in plotData.py")
print("y = ", y)
print("x_label", x_label)
print("count = ", tweetCounter)