#import os
def wordNumber(text_file):
    with open(text_file,'r',encoding = 'utf-8') as t:
        t_line = t.readline()
        #print(t_line)
        t_lines = t_line.split(" ")
        result = text_file + " 음절 수 : " + str(len(t_lines))
        return result

with open("word_number.txt", 'w', encoding = 'utf-8') as r:
    result = wordNumber('E3102.txt') 
    r.write(result + '\n')
    result = wordNumber('E3104.txt') 
    r.write(result + '\n')
    result = wordNumber('E3106.txt') 
    r.write(result + '\n')
    result = wordNumber('E3202.txt') 
    r.write(result + '\n')
    result = wordNumber('E3204.txt') 
    r.write(result + '\n')
    result = wordNumber('E3206.txt') 
    r.write(result + '\n')
    result = wordNumber('E402.txt') 
    r.write(result + '\n')
    result = wordNumber('E404.txt') 
    r.write(result + '\n')
    result = wordNumber('E406.txt') 
    r.write(result + '\n')
    result = wordNumber('E408.txt') 
    r.write(result + '\n')
    result = wordNumber('E410.txt') 
    r.write(result + '\n')
    result = wordNumber('H304.txt') 
    r.write(result + '\n')
    result = wordNumber('H308.txt') 
    r.write(result + '\n')
    result = wordNumber('H312.txt') 
    r.write(result + '\n')
    result = wordNumber('H316.txt') 
    r.write(result + '\n')
    result = wordNumber('H320.txt') 
    r.write(result + '\n')
    result = wordNumber('H324.txt') 
    r.write(result + '\n')
    result = wordNumber('H402.txt') 
    r.write(result + '\n')
    result = wordNumber('H408.txt') 
    r.write(result + '\n')
    result = wordNumber('H414.txt') 
    r.write(result + '\n')
    result = wordNumber('H418.txt') 
    r.write(result + '\n')
    result = wordNumber('H420.txt') 
    r.write(result + '\n')
    result = wordNumber('H424.txt') 
    r.write(result + '\n')
    result = wordNumber('K302.txt') 
    r.write(result + '\n')
    result = wordNumber('K304.txt') 
    r.write(result + '\n')
    result = wordNumber('k306.txt') 
    r.write(result + '\n')
    result = wordNumber('K308.txt') 
    r.write(result + '\n')
    result = wordNumber('K310.txt') 
    r.write(result + '\n')
    result = wordNumber('K402.txt')
    r.write(result + '\n')
    result = wordNumber('K404.txt') 
    r.write(result + '\n')
    result = wordNumber('K406.txt')
    r.write(result + '\n')
    result = wordNumber('K408.txt') 
    r.write(result + '\n')
    result = wordNumber('K410.txt')
    r.write(result + '\n')
    result = wordNumber('S3A02.txt') 
    r.write(result + '\n')
    result = wordNumber('S3A04.txt') 
    r.write(result + '\n')
    result = wordNumber('S3A06.txt') 
    r.write(result + '\n')
    result = wordNumber('S3A08.txt') 
    r.write(result + '\n')
    result = wordNumber('S3B02.txt') 
    r.write(result + '\n')
    result = wordNumber('S3B04.txt') 
    r.write(result + '\n')
    result = wordNumber('S3B06.txt') 
    r.write(result + '\n')
    result = wordNumber('S3B08.txt') 
    r.write(result + '\n')
    result = wordNumber('S4A02.txt') 
    r.write(result + '\n')
    result = wordNumber('S4A04.txt') 
    r.write(result + '\n')
    result = wordNumber('S4A06.txt') 
    r.write(result + '\n')
    result = wordNumber('S4A08.txt') 
    r.write(result + '\n')
    result = wordNumber('S4B02.txt') 
    r.write(result + '\n')
    result = wordNumber('S4B04.txt') 
    r.write(result + '\n')
    result = wordNumber('S4B06.txt') 
    r.write(result + '\n')
    result = wordNumber('S4B08.txt') 
    r.write(result + '\n')
