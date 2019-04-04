from __future__ import unicode_literals
import re
import nltk
from nltk.corpus import stopwords
import pyarabic.araby as araby
from snowballstemmer import stemmer
ar_stemmer = stemmer("arabic")


#convert json format to text , to deal with it

with open('tweets.json', 'r') as f:
    txt = f.read()
with open('tweets.txt', 'w') as f:
    # write to file
    f.write(txt)


with open('tweets.txt','r') as f_input, open('tweetjsonformat.txt', 'w') as f_output:
 for line in f_input:

        text = re.sub("\'", "\"",line) #conver ' to "
        text = re.sub('"}',' "}', text)#make space between " and }

        # write to file
        f_output.write(text)
f_input.close()
f_output.close()

# clean tweet from http ,@, # , english letter and number ,
with open('tweetjsonformat.txt','r') as f_input, open('clean_tweet.txt', 'w') as f_output:

   for line in f_input:

        st= line
        searchStr = 'text'
        searchStr2 = 'text":'
        created_at= st[:st.find(searchStr)] # From created_at filed until Text
        text = st[st.find(searchStr2) + len(searchStr2):]# From text filed until the end

# Remove @ ,http , #
        text = re.sub(r"(?:\@|https?\://)\S+", "", text)
        text=re.sub(r"(?:\#)\S+", "", text)

 #remove english text and numbers
        text=re.sub(r'[a-zA-Z0-9]+'," ",text)

 # remove english , and :
        text = re.sub(r'[,]+', " ", text)
        text = re.sub(r'[:]+', " ", text)

 #remove dublicate letters like : مبروووووك= مبرووك
        #text = re.sub(r'(.)\1+', r'\1', text)
        fainaltext = re.sub(r'(.)\1+', r'\1\1',text)

 #write to file
        f_output.write(created_at+searchStr2+fainaltext)

f_input.close()
f_output.close()



# remove stop word
with open('clean_tweet.txt', 'r') as inFile, open('removeStopWordFile.txt', 'w') as outFile:
    for line in inFile.readlines():
        print(" ".join([word for word in line.split()
                        # if the word not in stop word write to file
                        if word not in stopwords.words('arabic', 'UTF-8')]), file=outFile)
inFile.close()
outFile.close()

with open('removeStopWordFile.txt', 'r') as f_input, open('RemoveT&T.txt', 'w') as f_output:
    for line in f_input:
        st = line
#مكه become مكــــــــــــــه
        x = araby.strip_tatweel(st)
#ٍRemove َ ً ُِ ٌ
        y = araby.strip_tashkeel(x)
 # write to file
        f_output.write(y)

f_input.close()
f_output.close()

# steaming the word
with open('RemoveT&T.txt', 'r') as f_input, open('steam.txt', 'w') as f_output:
    for line in f_input.read().split("\n"):

        sentence = u"" + line
        for word in sentence.split(" "):
            if word[-1:] == 'ة':
                word = word[:-1] + 'ه'
                print(word)
                stem = ar_stemmer.stemWord(word)
                print(stem)
                f_output.write(str(stem) + " ")
                # f_output.write("\n")
            else:
                stem = ar_stemmer.stemWord(word)
                print(stem)
                f_output.write(str(stem) + " ")
# write to file
        f_output.write("\n")
f_input.close()
f_output.close()


# re conver txt file to json
with open("steam.txt", 'r') as f_input:
    data = f_input.readlines()


f_output = open("stringJson.json", "w")
for lines in data:
    f_output.write(lines)

f_output.close()


