with open ('./log_files/201811113020.log ',encoding='utf_8') as f:
    i=0
    for line in f:
        student_id1=line.split(',')[1]
        student_id2=student_id1.split('：')[1]
        if student_id2=='201811113020':
            i+=1
    print(i)