import re

with open('except_number.txt', 'w', encoding='utf-8') as total:
    with open("total.txt","r", encoding='utf-8') as f1:
        f1lines = f1.readlines()
        #print(f1lines)
        for i in f1lines:
            f1line = i.split(' ')
            print(f1line)
            for j in f1line:
                #정규표현식 코드 작성(넘버링 제외하는 것)
                re.compile()
