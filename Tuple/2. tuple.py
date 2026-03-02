def tuple2() :
    stud_data = [(82,'Anurakti',18) , (112,'Datt',18) , (74,'Meswa',18)]
    rollno = []
    stname = []
    ages = []
    for s in stud_data:
        rollno.append(s[0])
        stname.append(s[1])
        ages.append(s[2])
    print(stud_data,rollno,stname,ages,sep="\n")

tuple2()
