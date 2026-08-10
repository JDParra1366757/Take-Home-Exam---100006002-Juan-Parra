
grades = {
"math":{"anna": 1.7, "ben": 2.3, "clara": 1.0},
"physics": {"ben": 3.0, "clara": 1.3, "david": 2.0},
"art":{"anna": 1.0, "david": 1.7},}

subjects = grades.keys()

def subjects_of(student):
    global subjects
    global grades

    tempst = set()

    for subjects in grades:
        for st in grades[subjects]:
            if st == student:
                tempst.add(subjects)
            else:
                pass

    print(f"{student} takes {tempst}")


def takes_all():
    global subjects
    global grades
    global kids

    kids=set()
    notinclass = set()
    allclass = kids


    for subjects in grades:
        for st in grades[subjects]:
            kids.add(st) 

    for subjects in grades:
        notinclass = kids
        students = grades[subjects].keys()
        notinclass = notinclass - students
        allclass = allclass - notinclass


    if len(allclass) == 0:
        print("No student is in all classes.")
    else:
        print (f"The student in all classes is: {allclass}")


def student_average(student):
    global grades
    global subjects
    
    x = 0
    num = 0
    preavg = 0
    
    for subjects in grades:
        for students in grades [subjects]:
            if students == student:
                temp = grades[subjects][students]
                preavg += temp
                num+=1
            else:
                pass


    if num > 0:
        avg = preavg/num
        print(f"The average for {student} is: {avg:.3}")
    else:
        print("Student not enrolled.")



def honor_roll(grade):
    global grades
    global subjects
    global kids

    num = 0
    reavg = 0
    tempi = 0
    kids=set()
    honorroll = []

    for subjects in grades:
        for st in grades[subjects]:
            kids.add(st) 

    for student in kids:
        for subjects in grades:
            for students in grades[subjects]:
                if students == student:
                    tempi = grades[subjects][student]
                    reavg += tempi
                    num+=1
                else:
                    pass

        avg = reavg/num

        if avg <= grade:
            hr = [student,(round(avg,2))]
            honorroll.append(hr)
        else:
            pass

        avg=0
        reavg = 0
        num=0
        tempi = 0

    honorroll.sort()
    print(honorroll)


            

#subjects_of("anna")
#takes_all()
student_average("anna")
honor_roll(2)