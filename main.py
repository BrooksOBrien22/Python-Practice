#define topFiveFoods
def topFiveFoods():
    #print first food
    print("Orange Chicken")   

    #print second food
    print("Wings")

    #print third food
    print("Burgers")

    #print fourth food
    print("Noodles")

    #print fifth food
    print("steak")
def topThreeSports():
    print("Football")
    print("Basketball")
    print("Trapshooting")
def topThreeDays():
    print("Friday")
    print("Saturday")
    print("Sunday")
def topThreeClasses():
    print("Programming")
    print("Gym")
    print("Math")
def topThreeMeals():
    print("Dinner")
    print("Lunch")
    print("Breakfast")
def myNameIs(banana):
    print(banana + " is my name")

def timesTen(num):
    print(num * 10)

def plusFive(plus):
    print(plus + 5)

def divideByTwo(div):
    print(div / 2)

def addTwoNumbas(x,y):
    print(x + y)

def madLib(instrument, hours, day, letter, majomin, flats, sharps, adjectone, adjecttwo, fract, adjectthree, instrumenttwo, adjectfour, noun, family, song, adjectfive, artist):
    print("While I've stayed at home, I've practiced the " + instrument + " for " + hours + " hours every " + day + ". My favorite key signature to play and practice in is " + letter + majomin + ". It has " + flats + sharps + ". I like this key signature because it is " + adjectone + " and " + adjecttwo + ". I've also gotten awesome at counting time signatures. The time signature I love is " + fract + " because it is " + adjectthree + " to count. One instrument I want to learn how to play while I'm at home is " + instrumenttwo + ", because it is " + adjectfour + " and sounds like a " + noun + ". My " + family + " likes it when I play " + song + ", and always gives me a round of applause after my performances! When I return to school, my teacher will be " + adjectfive + " of how great I am at playing my insturment. My teacher might even think I sound like " + artist + "!")

def color():
    return "blue"

def greaterThan10(x):
    if x > 10:
        return "x is greater than 10"
    elif x == 10:
        return "x equals 10"
    else:
        return "x is not greater than 10"

def potato(x, y):
    if x + y > 10:
        return "potato"
    elif x + y == 10:
        return "tomato"
    else:
        return "Alfredo"

def catDog():
    if "cat" > "dog":
        print("wow I can't believe this worked")
   
    else:
        print("wow I still can't believe this worked")

def login(password):
    if password == "Osowskiroolz":
        return "ACCESS GRANTED"
   
    else:
        return "ACCESS DENIED"

def trivia(answer):
    if answer.lower() == "gerald":
        return "Bingo!!"
    
    else:
        return "git gud lol"

def define(word):
   
    word = word.lower()
  
    word = word.upper()
  
    if word == "cheesecake":
        return "a cake having a firm custardlike texture, made with cream cheese, cottage cheese, or both, and sometimes topped with a jamlike fruit mixture."
   
    elif word == "hot dog":
        return "a sandwich consisting of a frankfurter in a split roll, usually eaten with mustard, sauerkraut, or relish."
  
    elif word == "pizza":
        return "a flat, open-faced baked pie of Italian origin, consisting of a thin layer of bread dough topped with spiced tomato sauce and cheese, often garnished with anchovies, sausage slices, mushrooms, etc."
   
    elif word == "close":
        return "to stop or obstruct (a gap, entrance, aperture, etc.):"
   
    elif word == "slot":
        return "a narrow, elongated depression, groove, notch, slit, or aperture, especially a narrow opening for receiving or admitting something, as a coin or a letter."
   
    elif word == "outfit":
        return "an assemblage of articles that equip a person for a particular task, role, trade, etc."
  
    elif word =="cover":
        return "to be or serve as a covering for; extend over; rest on the surface of"
   
    elif word == "moon":
        return "the earth's natural satellite, orbiting the earth at a mean distance of 238,857 miles (384,393 km) and having a diameter of 2,160 miles (3,476 km)."
   
    elif word == "horoscope":
        return "a diagram of the heavens, showing the relative position of planets and the signs of the zodiac, for use in calculating births, foretelling events in a person's life, etc."
   
    elif word == "drown":
        return "to die under water or other liquid of suffocation."
  
    else:
        return "This word is not in our dicitonary"


def function(x):
    if x % 10 == 0:
        return True
    else:
        return False

def functionOne(x, y, z):
    if x > 10 and not (y > 10 or z == 5):
        return True
    else:
        return False

def countTen():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)



def tenCount():
    x = 1
    y = 1
    while x <= 10:
        while y <= 10:
            print(y)
            y = y + 1
        y = 1
        x = x + 1

def countEvOd():
    x = 1
    while x <= 20:
    
        if x % 2 == 0:
            print(x)
            print("Even")
        else:
            print(x)
            print("Odd")
        x = x + 1

def firstLetter(w):
    print(len(w))

print(firstLetter("dog"))