import re
with open("합계.txt",'w',encoding='utf-8') as s:
    with open("어미_calculation.txt",'r',encoding='utf-8') as calc1:
        calc1_lines = calc1.readlines()
        calc1_odd = calc1_lines[::2]
        calc1_even = calc1_lines[1::2]
        #print(calc1_even)
        #print(calc1_lines[::2])
    with open("표현_calculation.txt",'r',encoding='utf-8') as calc2:
        calc2_lines = calc2.readlines()
        calc2_odd = calc2_lines[::2]
        calc2_even = calc2_lines[1::2]
        #print(calc2_lines[::2])
    
    total = calc1_even + calc2_even
    #print(total)
    plus = []
    for i in total:
        #print(i)
        parseText = re.findall('\d*\.?\d+', i)
        #parseText= re.sub([^0-9], '', total)
        plus.append(parseText)

    for i in range(49):
        s.write(calc1_odd[i])
        s.write(calc2_odd[i])
        s.write('어미'+ calc1_even[i])
        s.write('표현'+ calc2_even[i])
        #parseText= re.sub([^0-9], '', i)
        p1 = re.findall('\d*\.?\d+',calc1_even[i])
        p2 = re.findall('\d*\.?\d+',calc2_even[i])
        for i in p1:
            for j in p2:
                result = float(i)+float(j)
                s.write("총 난이도 지수 : " + str(result)+'\n')
    

    
        
    