''' Hai I'm Bharath kumar and this is my first own program in python without having any note or help '''


#i'm defining a function instead of print and some place function not is working so i use print
def prt(x):
    print(x)


prt('Hi this is my 1st game which is like guessing')
print()
prt("i'm noob here so don't bother about silly mistake ")
print()
print()
prt("let's start the game....")
print()

#prt("Please enter your name:");
name = input("Please enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print()
    print('You are good to go..')
    print()
    print("Hello", name, "Lets play....")
    print()
    print('SO choose , which way you want to go ?')
    path = input('(left/right) ').lower()

    if path == 'right':
        print('you choose', path, 'keep going...you are still alive')
        print()
        print('Now you reach the river, their is two option ')
        print()
        print('Either you go around with wild animals')
        print("or")
        print('you can cross the river ')
        print()
        way = input('across / around : ').lower()
        if way == 'across':
            print(
                "good you sucessfully cross the river ' you might feel cold'")
            print()
            print('keep walking, now you seeing two similar house')
            home = input('house 1 / house 2 ').upper()
            if home == 'HOUSE 1':
                print('you choose safe house and you survied ')
                print()
                print('congrulation you this game ')
                print()
                print('If you Like this Share, ping me "thank you" ')
            else:
                print(' Opps you choose worng and killed by trap')
        else:
            print('you become a food for animals...:(')
    else:
        print('you choose the wrong way')
else:
    print('you need to grow...')
