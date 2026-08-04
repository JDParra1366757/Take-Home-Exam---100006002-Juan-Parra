
data = "Dune:8, Dune:9, Barbie:7, Dune:10, Barbie:9, Oppenheimer:9, Barbie:6"

singledata = []
ratinglist = []
movienames = []
grades = []
parseddata = []
avg = 0

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
    global movienames
    global grades
    global avg
    
    y = 0
    num = 0
    preavg = 0
    
    while y < len(movienames):
        if movie == movienames[y]:
            num +=1
            preavg += grades[y]
            y +=1
        else:
            y+=1 

    if num > 0:
        avg = preavg/num
        print(f"The average for {movie} ist: {avg:.2}")
    else:
        print("Movie not on list. 0.0")

    return avg

def inner_average_rating(movie):
    global movienames
    global grades
    global avge
    
    y = 0
    num = 0
    preavg = 0
    
    while y < len(movienames):
        if movie == movienames[y]:
            num +=1
            preavg += grades[y]
            y +=1
        else:
            y+=1 

    if num > 0:
        avge = preavg/num
    else:
        pass

    return avge




def max_rating():
    global movienames
    global grades
    global avg 
    global vally

    vally = 0
    maxi = 0
    z = 0
    moviemax=[]
    donemovies = []
    while z < len(movienames):
        if movienames[z] in donemovies:
            pass
            z += 1
        else:
            inner_average_rating(movienames[z])
            temp = avge
            if avge>maxi:
                maxi = avge
                moviemax = [movienames[z],avge]
            else:
                if avge == maxi:
                    moviemax[0]=[moviemax[0],movienames[z]]
                    vally = 1
                else:
                    pass
            donemovies.append(movienames[z])
            z+=1

    if vally != 1:
        print(f"The highest rated movie is {moviemax[0]} with {moviemax[1]}")
    else: 
        print(f"The highest rated movies are {moviemax[0][0]} and {moviemax[0][1]} with {moviemax[1]}")



def ratings_count():
    global movienames

    m=0
    number = 0
    count= []
    for movienames in movienames:
        number = movienames.count(movienames[m])
        

    print(count)

       
parse_ratings()
print(parseddata)
#print(movienames)
#print(grades)
average_rating("Barbie")
max_rating()
ratings_count()