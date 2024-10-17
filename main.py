def Title():
    "Welcome to a personalitly test. Today you will be creating your own creatures. Depending on your creature depends on if we will be freinds! PS This whole program a joke teacher."

def Question_1():
    """    
    How many fingers does your creature have?
    A. 0 to 4 fingers 
    B. 5 to 9 fingers 
    C. 10 Fingers 
    D. 11 to 15 Fingers
    E. 16+ fingers"""

def Question_2():
    """ 
    How many eyes does your creature have?   
    A. No Eyes
    B. 1 Eye
    C. 2 Eyes
    D. 3 Eyes 
    E. 4+ Eyes"""

def Question_3():
    """
    How many feet does your creature have?    
    A. No Feet
    B. 1 Foot
    C. 2 Feet
    D. 3 Feet
    E. 4+ feet"""

def Question_4():
    """   
    What food does your creature like? 
    A. Grass
    B. Leaves
    C. Fish
    D. Cow
    E. Hummans """

def Question_5():
    """    
    Whats your creature favorite color?
    A. Red 
    B. Green
    C. Blue
    D. Orange
    E. Purple"""
   
answerlist = []
def questionnum(userinput):
    inputbool = False
    while inputbool == False:
        userinput = input("Enter Letter Please: ")
        if userinput.isalpha():
          userinput = userinput.upper()
          if userinput == 'A' or userinput == 'B' or userinput == 'C' or userinput == 'D' or userinput == 'E':
               userinput = ord(userinput) - 64
               answerlist.append(userinput)
               inputbool = True
          else:
               print("I gacve you the options A, B, C, D, or E bro not " + userinput)
        else:
          print("Your dumb. I ask for a Letter. Just to prove you're dumb here your input: " + userinput)

def qsum():
     total = sum(answerlist)
     match total:
          case(total) if total == 5:
               print("Wow. really weird creature to make. I guess we can be weirdo freinds?")
          case(total) if total > 5 and total <=10:
               print("You are alright. I'll think about it if we can be freinds.")               
          case(total) if total > 10 and total <= 15:
               print("You are basic. I don't like basic people.")
          case(total) if total > 15 and total <= 20:
               print("You are kinda intresting. So want to be freinds?")
          case(total) if total > 20 and total <= 25:
               print("Wow you are really intresting. I demand you to be freinds with me! ")

print(Title.__doc__)


print(Question_1.__doc__)
questionnum(input)

print(Question_2.__doc__)
questionnum(input)

print(Question_3.__doc__)
questionnum(input)

print(Question_4.__doc__)
questionnum(input)

print(Question_5.__doc__)
questionnum(input)

qsum()