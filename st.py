from snowballstemmer import stemmer
ar_stemmer = stemmer("arabic")

with open('infile','r') as f_input, open('outfile.txt', 'w') as f_output:

 for line in f_input:

        sentence =u""+line
        for word in sentence.split(" "):
          stem = ar_stemmer.stemWord(word)
          print(stem)
