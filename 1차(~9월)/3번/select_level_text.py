import csv
import re
import os

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
    
