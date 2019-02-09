import pyarabic.araby as araby
import pyarabic.number as number

with open('/Users/jodharb/Desktop/steaming/outfile','r') as f_input, open('Toknize.txt', 'w') as f_output:
    for line in f_input:
        st = line
        x=araby.tokenize(st)

       # print(x)
        f_output.write(str(x))
        f_output.write('\n')
