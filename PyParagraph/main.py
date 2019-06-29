import os
import csv
import re


csvpath=os.path.join("paragraph_2.txt")



words=0
sentence=0
letter=0
aver_letter=0
aver_sen=0
with open(csvpath, "r") as fh:
    lines=fh.read()
    word=len(re.split(" ",lines))
    #word=len(re.split("[-'\s]+",lines))
    words+=word
    sen=len(re.findall("[.?!]",lines))
    sentence+=sen
    letter+=len([i for i in lines if i.isalpha()])
    #print (re.split("['\s-]",lines))
    print (words)
    print (sentence)
    #print (letter)
    aver_letter=round(letter/words,1)
    aver_sen=round(words/sentence,1)
    print (aver_letter)
    print (aver_sen)

output_path=os.path.join("paragraph2_summary.txt")

with open (output_path, "w",newline="") as file:



    file.write("Paragraph Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Approximate Word Count:{words}\n")
    file.write(f"Approximate Sentence Count: {sentence}\n")
    file.write(f"Average Letter Count:{aver_letter}\n")
    file.write(f"Average Sentence Length: {aver_sen}\n")
