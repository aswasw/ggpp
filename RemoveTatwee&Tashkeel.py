import pyarabic.araby as araby
import pyarabic.number as number

with open('/Users/jodharb/Desktop/preprocessing/removeStopWordFile.txt','r') as f_input, open('RemoveT&T.txt', 'w') as f_output:
    for line in f_input:
        st = line
        # Remove ً
        x=araby.strip_tatweel(st)
        y=araby.strip_tashkeel(x)
        #print(y)
        f_output.write(y)
        #f_output.write('\n')
