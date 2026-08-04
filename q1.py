
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
    global parseddata
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

    return

movie = "Dune"
def average_rating(movie):
    global data
    global singledata
    global ratinglist
    global movienames
    global grades
    global parseddata
    y = 0
    num = 0
    preavg = 0
    avg = 0
    while y < len(movienames):
        if movie == movienames[y]:
            num +=1
            preavg += grades[y]
            y +=1
        else:
            y+=1 

    avg = preavg/num

    print(f"The average for {movie} ist: {avg:.2}")


       
parse_ratings()
#print(movienames)
#print(grades)

print(parseddata)
average_rating("Oppenheimer")