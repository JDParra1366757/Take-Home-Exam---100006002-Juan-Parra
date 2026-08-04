
data = "Dune:8, Dune:9, Barbie:7, Dune:10, Barbie:9, Oppenheimer:9, Barbie:6"

singledata = []
ratinglist = []
movienames = []
grades = []
parseddata = []

def parse_ratings():
    global data
    global singledata
    global ratinglist
    global movienames
    global grades
    x = 0

    for data in data.split(", "):
        singledata.append(data)

    for singledata in singledata:
        for minidat in singledata.split(":"):
            if len(minidat) > 3:
                movienames.append(minidat)
            else:
                minidat = int(minidat)
                grades.append(minidat)

    while x < len(movienames):
        temp1 = movienames[x]
        temp2 = grades[x]
        temp = tuple((temp1,temp2))
        parseddata.append(temp)
        x += 1

       
parse_ratings()
#print(movienames)
#print(grades)
print(parseddata)
