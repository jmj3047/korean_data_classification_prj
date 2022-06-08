import re
def calculator(textfile):
    with open(textfile,'r',encoding = 'utf-8') as r:
        count_1=0
        count_2=0
        count_3=0
        count_4=0
        count_5=0
        count_6=0
        count_7=0
        result_1=0
        result_2=0
        result_3=0
        result_4=0
        result_5=0
        result_6=0
        result_7=0
        total_list = []
        sum_list=[]
        r_line = r.readlines()
        c_list = [x for x in r_line if x]
        #print(c_list)
        while '\n' in c_list:
            c_list.remove('\n')        
        #print(c_list)
        for i in c_list:
            if i == '1\n':
                count_1 = count_1 + 1
            elif i == '2\n':
                count_2 = count_2 + 1
            elif i == '3\n':
                count_3 = count_3 + 1
            elif i == '4\n':
                count_4 = count_4 + 1
            elif i == '5\n':
                count_5 = count_5 + 1
            elif i == '6\n':
                count_6 = count_6 + 1
            elif i == '7\n':
                count_7 = count_7 + 1
        
        total_list.append(count_1)
        total_list.append(count_2)
        total_list.append(count_3)
        total_list.append(count_4)
        total_list.append(count_5)
        total_list.append(count_6)
        total_list.append(count_7)
        print(total_list)

        
        result_1 = count_1*1
        result_2 = count_2*1.5
        result_3 = count_3*2
        result_4 = count_4*2.5
        result_5 = count_5*3
        result_6 = count_6*3.5
        result_7 = count_7*4

        sum_list.append(result_1)
        sum_list.append(result_2)
        sum_list.append(result_3)    
        sum_list.append(result_4)
        sum_list.append(result_5)
        sum_list.append(result_6)
        sum_list.append(result_7)
        print(sum_list)

        result = sum(sum_list)
        a = textfile + ' 1등급 :'+ str(count_1) + ' 2등급 :'+ str(count_2) + ' 3등급 :'+ str(count_3) + ' 4등급 :'+ str(count_4) + ' 5등급 :'+ str(count_5) + ' 6등급 :'+ str(count_6) + ' 7등급 :'+ str(count_7) + '\n' + ' 난이도 지수 :' + str(result)
    return a
    
with open('어미_calculation.txt','w',encoding = 'utf-8') as c:
    result = calculator('E3102tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E3104tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E3106tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E3202tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E3204tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E3206tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E402tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E404tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E406tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E408tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('E410tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H304tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H308tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H312tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H316tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H320tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H324tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H402tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H408tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H414tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H418tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H420tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('H424tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K302tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K304tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('k306tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K308tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K310tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K402tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K404tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K406tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K408tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('K410tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3A02tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3A04tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3A06tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3A08tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3B02tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3B04tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3B06tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S3B08tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4A02tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4A04tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4A06tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4A08tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4B02tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4B04tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4B06tag-split-result_fin.txt')
    c.write(str(result) + '\n')
    result = calculator('S4B08tag-split-result_fin.txt')
    c.write(str(result) + '\n')