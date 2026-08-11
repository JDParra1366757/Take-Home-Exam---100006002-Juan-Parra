import math

def scale_recipe(name,servings,*ingredients,unit="g",**options):
    listy = []
    num1 = 0
    x = 0
    y=0

    if servings < 1:
        print ("Minimum servings: 1.")
    else:
        print(f"\n\n\nFor {servings} unit(s) of {name}(s) you'll need:")
        while num1 < len(ingredients):
            temp1= ingredients[num1][0]
            temp2= (ingredients[num1][1]) * servings
            listy.append((temp1,temp2))
            num1 +=1

        while x < len(listy):
            print(f"-{listy[x][0]}: {listy[x][1]}{unit}")
            x+=1

        if len(options)!= 0:
            print("\nConsider the following:")
            for key in options:
                temp3 = options[key]
                print(f"{key}: {temp3}")

        else:
            pass


scale_recipe("Toast",1,("Bread",25))
scale_recipe("Pizza",3,("Dough",100),("Tomato Sauce",50),("Cheese",30),unit="oz")
scale_recipe("Marble Cake",10,("Flour",100),("Eggs",25),("Chocolate Powder",50),("Vanilla Extract",5),("Milk",200),unit="g",bakefor="60 minutes",bakeat="175 C")