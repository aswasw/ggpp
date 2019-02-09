with open('/Users/jodharb/Downloads/tweettss/tweetsoutput.txt','r') as f_input, open('clean_tweet1.txt', 'w') as f_output:

 for line in f_input:
        st= line
        import re

     # Remove @ ,http , #
        text = re.sub(r"(?:\@|https?\://)\S+", "", st)
        text=re.sub(r"(?:\#)\S+", "", text)
     #remove english text and numbers
        text=re.sub(r'[a-zA-Z0-9]+'," ",text)

        text = re.sub(r'[,]+', " ", text)
        text = re.sub(r'[:]+', " ", text)
        print(text)
        #write to file
        f_output.write(text)
        #f_output.write('\n')

