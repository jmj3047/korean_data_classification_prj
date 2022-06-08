
#====================등급파일 어휘 고르기================================
#1. 그 txt파일에서 [어휘,품사] 형태로 가져오기

all_grade_word_pos = [] #등급파일의 어휘-품사
exc_word_pos = [] #어휘-품사가 같은데 등급이 다른 거
with open('\\Users\\82107\\Desktop\\p2\\test\\어휘품사.txt','r',encoding='utf-8') as word_pos_file:
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
