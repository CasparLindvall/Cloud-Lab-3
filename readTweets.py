import tarfile, json
import timeit
import numpy as np

# To ge the run time
start = timeit.default_timer()

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
stopWords = open("stopwords.txt").read().splitlines()

# Format for easier
def formatStr(source):
    source = source.replace('\n\n', '\n' )
    source = source.lower()
    sourceArr = source.splitlines()
    #[word for word in tokenized_words if word not in stop_words]
    return sourceArr

f = None
i = 0

tar = tarfile.open("data.tar.gz", "r:gz")

for member in tar.getmembers():
    f = tar.extractfile(member)
    if f:
        content = f.read()
        contentArr = formatStr(content)
        #i amount of tweets
        for tweetString in contentArr:
            tweetDict = json.loads(tweetString)
            tweetText = tweetDict["text"].encode("utf-8")
            tweetText = removeChar(tweetText)
            #tweetText = [word for word in tweetText if word not in stopWords]
            #print(tweetText+"\n")
            for word in tweetText.split():
                if word in model:
                    model[word] += 1
        tweetCounter += len(contentArr)

        for word, occ in model.items():
            print(word + "\t: " + str(occ) + "\t" + "{0:.2f}".format(occ/float(tweetCounter)*100)+"%"+" of tweets")

    print('Time: ', "{0:.2f}".format(timeit.default_timer() - start) + "\t"+"Tweets counted: "+ str(tweetCounter))