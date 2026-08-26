line_count=0
word_count=0
number_of_char=0
try:
    with open('sample.txt','r') as file:
        for line in file:
            line_count+=1
            words=line.split()
            for word in words:
                word_count+=1
                number_of_char+=len(word)
except:
    print("Sorry.... file not found")

print("Number of line : ",line_count)
print("Word Count : ",word_count)
print("Character Count : ",number_of_char)

'''
Out Put:

Number of line :  17
Word Count :  132
Character Count :  770
'''