import string
import nltk
from nltk.corpus import stopwords

#with open('/Users/jodharb/Desktop/newp/clean_tweet1-1.txt', 'r') as inFile, open('final_tweettt.txt', 'w') as outFile:

# remove stop word and punctuation ٍ ُ ٌ ِ ًَ ّْ
with open('/Users/jodharb/Desktop/preprocessing/clean_tweet1.txt', 'r') as inFile, open('removeStopWordFile.txt', 'w') as outFile:
    for line in inFile.readlines():
        print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                        if len(word) >= 4 and word not in stopwords.words('arabic','UTF-8')]), file=outFile)


