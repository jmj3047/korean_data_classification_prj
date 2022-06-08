import re
def preprocessing(textfile, fin_textfile):
    with open('prac.txt','w', encoding='utf-8') as p:
        with open(textfile,'r',encoding = 'utf-8') as t:
            t_line = t.readlines()
            #print(t_line)
            for i in t_line:
                #i.split("\t")
                j = i.replace('\t',"\n")
                #print(j)        
                p.write(j)
    
    with open("prac.txt",'r',encoding = 'utf-8') as s:
        s_line = s.readlines()
        #print(s_line)
        fin = []
        for i in range(len(s_line)):
            if i == 0:
                continue        
            elif i == 3:
                first = s_line[3]
                #print(s_line[i])
            elif ((i*2+1)*4) < len(s_line):
                result = s_line[((i*2+1)*4)-1]
                #print(result)
                fin.append(result)
        fin.append(first)
        #print(fin)
        with open(fin_textfile,'w',encoding = 'utf-8') as f:
            for i in fin:
                korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                parseText= re.sub(korean, '', i)
                f.write(parseText)
                #print(parseText)


middle = preprocessing('E3102tag-split-result.txt','E3102tag-split-result_fin.txt')
middle = preprocessing('E3104tag-split-result.txt','E3104tag-split-result_fin.txt')
middle = preprocessing('E3106tag-split-result.txt','E3106tag-split-result_fin.txt')
middle = preprocessing('E3202tag-split-result.txt','E3202tag-split-result_fin.txt')
middle = preprocessing('E3204tag-split-result.txt','E3204tag-split-result_fin.txt')
middle = preprocessing('E3206tag-split-result.txt','E3206tag-split-result_fin.txt')
middle = preprocessing('E402tag-split-result.txt','E402tag-split-result_fin.txt')
middle = preprocessing('E404tag-split-result.txt','E404tag-split-result_fin.txt')
middle = preprocessing('E406tag-split-result.txt','E406tag-split-result_fin.txt')
middle = preprocessing('E408tag-split-result.txt','E408tag-split-result_fin.txt')
middle = preprocessing('E410tag-split-result.txt','E410tag-split-result_fin.txt')
middle = preprocessing('H304tag-split-result.txt','H304tag-split-result_fin.txt')
middle = preprocessing('H308tag-split-result.txt','H308tag-split-result_fin.txt')
middle = preprocessing('H312tag-split-result.txt','H312tag-split-result_fin.txt')
middle = preprocessing('H316tag-split-result.txt','H316tag-split-result_fin.txt')
middle = preprocessing('H320tag-split-result.txt','H320tag-split-result_fin.txt')
middle = preprocessing('H324tag-split-result.txt','H324tag-split-result_fin.txt')
middle = preprocessing('H402tag-split-result.txt','H402tag-split-result_fin.txt')
middle = preprocessing('H408tag-split-result.txt','H408tag-split-result_fin.txt')
middle = preprocessing('H414tag-split-result.txt','H414tag-split-result_fin.txt')
middle = preprocessing('H418tag-split-result.txt','H418tag-split-result_fin.txt')
middle = preprocessing('H420tag-split-result.txt','H420tag-split-result_fin.txt')
middle = preprocessing('H424tag-split-result.txt','H424tag-split-result_fin.txt')
middle = preprocessing('K302tag-split-result.txt','K302tag-split-result_fin.txt')
middle = preprocessing('K304tag-split-result.txt','K304tag-split-result_fin.txt')
middle = preprocessing('k306tag-split-result.txt','k306tag-split-result_fin.txt')
middle = preprocessing('K308tag-split-result.txt','K308tag-split-result_fin.txt')
middle = preprocessing('K310tag-split-result.txt','K310tag-split-result_fin.txt')
middle = preprocessing('K402tag-split-result.txt','K402tag-split-result_fin.txt')
middle = preprocessing('K404tag-split-result.txt','K404tag-split-result_fin.txt')
middle = preprocessing('K406tag-split-result.txt','K406tag-split-result_fin.txt')
middle = preprocessing('K408tag-split-result.txt','K408tag-split-result_fin.txt')
middle = preprocessing('K410tag-split-result.txt','K410tag-split-result_fin.txt')
middle = preprocessing('S3A02tag-split-result.txt','S3A02tag-split-result_fin.txt')
middle = preprocessing('S3A04tag-split-result.txt','S3A04tag-split-result_fin.txt')
middle = preprocessing('S3A06tag-split-result.txt','S3A06tag-split-result_fin.txt')
middle = preprocessing('S3A08tag-split-result.txt','S3A08tag-split-result_fin.txt')
middle = preprocessing('S3B02tag-split-result.txt','S3B02tag-split-result_fin.txt')
middle = preprocessing('S3B04tag-split-result.txt','S3B04tag-split-result_fin.txt')
middle = preprocessing('S3B06tag-split-result.txt','S3B06tag-split-result_fin.txt')
middle = preprocessing('S3B08tag-split-result.txt','S3B08tag-split-result_fin.txt')
middle = preprocessing('S4A02tag-split-result.txt','S4A02tag-split-result_fin.txt')
middle = preprocessing('S4A04tag-split-result.txt','S4A04tag-split-result_fin.txt')
middle = preprocessing('S4A06tag-split-result.txt','S4A06tag-split-result_fin.txt')
middle = preprocessing('S4A08tag-split-result.txt','S4A08tag-split-result_fin.txt')
middle = preprocessing('S4B02tag-split-result.txt','S4B02tag-split-result_fin.txt')
middle = preprocessing('S4B04tag-split-result.txt','S4B04tag-split-result_fin.txt')
middle = preprocessing('S4B06tag-split-result.txt','S4B06tag-split-result_fin.txt')
middle = preprocessing('S4B08tag-split-result.txt','S4B08tag-split-result_fin.txt')
