
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




            
            

    

#subjects_of("anna")
takes_all()
