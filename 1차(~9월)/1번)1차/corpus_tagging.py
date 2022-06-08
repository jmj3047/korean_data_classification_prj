with open('corpus_tagging.txt', 'w', encoding='utf-8') as total:
    with open("rawdata(corpus).txt","r", encoding='utf-8') as f1:
        f1lines = f1.readline()
        f1lines = f1lines.split('+')
        #print(f1lines)
        for i in f1lines:
            f1line = i.split(' ')
            #print(f1line)
            for j in f1line:
                    j.split(',')
                    total.write(j+'\n')
'''
with open("rawdata(corpus).txt","r", encoding='utf-8-sig') as f1:
        f1lines = f1.readline()
        f1lines = f1lines.split('+')
        print(f1lines)
        for i in f1lines:
            f1line = i.split(' ')
            print(f1line)
            for j in f1line:
                    j.split(',')
'''