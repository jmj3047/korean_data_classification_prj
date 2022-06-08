import re
import os
def calc(textfile):
    with open(textfile, 'r', encoding='utf-8') as f1:
        f1_lines = f1.readlines()
        num_list = []        
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
        for i in f1_lines:
            numbers = re.findall('\d+',i)
            #print(numbers)
            num_list.append(numbers)
            if numbers == ['1']:
                count_1 += 1
            elif numbers == ['2']:
                count_2 += 1
            elif numbers == ['3']:
                count_3 += 1
            elif numbers == ['4']:
                count_4 += 1
            elif numbers == ['5']:
                count_5 += 1
            elif numbers == ['6']:
                count_6 += 1
            elif numbers == ['7']:
                count_7 += 1
        
        total_list.append(count_1)
        total_list.append(count_2)
        total_list.append(count_3)
        total_list.append(count_4)
        total_list.append(count_5)
        total_list.append(count_6)
        total_list.append(count_7)

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
        #print(sum_list)
        result = sum(sum_list)
        a = textfile +'\n' + ' 1등급 :'+ str(count_1) + ' 2등급 :'+ str(count_2) + ' 3등급 :'+ str(count_3) + ' 4등급 :'+ str(count_4) + ' 5등급 :'+ str(count_5) + ' 6등급 :'+ str(count_6) + ' 7등급 :'+ str(count_7) + '\n' + ' 난이도 지수 :' + str(result)
    return a

data_path = os.listdir('C:/Users/jmj30/Dropbox/카메라 업로드/Documentation/2020/2020 2학기/project/NLP프로젝트/2차(~10월)/어휘,어미 난이도지수/어휘/data')
#os.chdir('C:/Users/jmj30/Dropbox/카메라 업로드/Documentation/2020/2020 2학기/project/NLP프로젝트/2차(~10월)/어휘,어미 난이도지수/어휘')
with open('어휘_calculation.txt','w',encoding='utf-8') as c:
    for file in data_path:
        #print(file)
        #print(type(file))
        result = calc(file)
        #print(result)
        c.write(str(result)+'\n')




    
