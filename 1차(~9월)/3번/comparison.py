import csv
import re
import os

#====================등급파일 어휘 고르기================================
#1. 그 txt파일에서 [어휘,품사] 형태로 가져오기

all_grade_word_pos = [] #등급파일의 어휘-품사
exc_word_pos = [] #어휘-품사가 같은데 등급이 다른 거
with open('어휘품사.txt','r',encoding='utf-8') as word_pos_file:
    word_pos_lines = word_pos_file.readlines()
    for word_pos_line in word_pos_lines:
        if word_pos_line.split() in all_grade_word_pos:
            exc_word_pos.append(word_pos_line.split())
        all_grade_word_pos.append(word_pos_line.split())
        
grade_word_pos = [] #exc_word_pos 제외하고 (중복 제거한)->엑셀 자체 등급파일의 어휘-품사(동형명등)
for word_pos in all_grade_word_pos:
    if word_pos not in exc_word_pos:
        if word_pos[1] in ['EP','EF','EC','ETN','ETM']:
            grade_word_pos.append(word_pos)

#====================교재파일 어휘 고르기================================
#2. 태깅된 교재 파일에서 특징만 태그 되어 있는(이 경우에는 어미) 단어들 가져오기

directory = os.listdir('\\Users\\82107\\Desktop\\p2\\test\\book_split')
os.chdir('\\Users\\82107\\Desktop\\p2\\test\\book_split')
for file in directory:
    all_book_word_pos = [] #중복 제거한 교재의 모든 어휘-품사
    with open(file,'r',encoding='utf-8') as book_word_pos_file:
        lines = book_word_pos_file.readlines()
        all_word_pos_lines = []# 중복 포함
        for i in lines: all_word_pos_lines.append(i.strip())
        word_pos_lines = []
        count_list = [] #교재의 어휘-품사 숫자
        for word_pos_line in all_word_pos_lines:
            if word_pos_line not in word_pos_lines:
                word_pos_lines.append(word_pos_line)
                count_list.append(all_word_pos_lines.count(word_pos_line))
        for word_pos_line in word_pos_lines:
            all_book_word_pos.append(word_pos_line.split('/'))
    
    book_word_pos = [] #교재의 어휘-품사(동형명등)
    for word_pos in all_book_word_pos:
        if word_pos[1] in ['EP','EF','EC','ETN','ETM']:
            book_word_pos.append(word_pos)
    

#3. 1번과 2번 리스트 확인해서 등급가져오기
    
grade_csv = open('\\Users\\82107\\Desktop\\p2\\test\\word_grade.csv','r',encoding='utf-8')
rdr = csv.reader(grade_csv)
lines = [] #어휘 등급표 전체 line들
for line in rdr:
    lines.append(line)

with open('\\Users\\82107\\Desktop\\p2\\test\\except\\'+file[:-4]+'-except.txt','w',encoding='utf-8') as except_file: #교재에 포함된 어휘-품사가 같은데 등급이 다른 거
    for word_pos in book_word_pos:
        if word_pos in exc_word_pos:
            except_file.write(str(word_pos[0])+'\t'+str(word_pos[1])+'\n')
            
print(len(book_word_pos))         
final_file = open('\\Users\\82107\\Desktop\\p2\\test\\result\\'+file[:-4]+'-result.txt','w',encoding='utf-8')
finished_word = []
for g_word_pos in grade_word_pos:
    grade_pos, grade_word = g_word_pos[1], g_word_pos[0]
    pos_reg = re.compile(grade_pos)
    for word_pos in book_word_pos:
        book_pos, book_word = word_pos[1],word_pos[0]
        if grade_pos == book_pos and grade_word == book_word:
            if word_pos not in finished_word and word_pos not in exc_word_pos:
                final_file.write(book_word+'/'+book_pos)
                for i in lines[all_grade_word_pos.index([grade_word,grade_pos])]:
                    final_file.write('\t'+i)
                final_file.write('\n')
                finished_word.append(word_pos)
        elif grade_pos == 'ET' and book_pos in ['ETN','ETM']:
            if grade_word == book_word:      
                if word_pos not in finished_word and word_pos not in exc_word_pos:
                    final_file.write(book_word+'/'+book_pos)
                    for i in lines[all_grade_word_pos.index([grade_word,grade_pos])]:
                        final_file.write('\t'+i)
                    final_file.write('\n')
                    finished_word.append(word_pos)
final_file.close()

print(len(finished_word))

i = 0  
with open('\\Users\\82107\\Desktop\\p2\\test\\else\\'+file[:-4]+'-else.txt','w',encoding='utf-8') as else_file: #노가다 검수
    for word_pos in book_word_pos:
        if word_pos not in finished_word:
            else_file.write(str(word_pos[0])+'\t'+str(word_pos[1])+'\n')
            i += 1
print(i)
