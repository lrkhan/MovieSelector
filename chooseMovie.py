def options():
    print('\n')
    print("Please select and option from below.")
    print("1) Select a Random Movie")
    print("2) View Unwatched Options")
    print("3) View Watched Videos")
    print("4) Add a Movie\n")

    usrChoice = int(input("I want to: "))
    print('\n')

    if usrChoice not in [1,2,3,4]:
        print("invalid option chosen")
        options()

    return usrChoice

def SelectRandom(movieList):
    pass

def unwatched(unwatchedList):
    pass

def watched(watchedList):
    pass

def addList(movieList):
    pass

print("Welcome to the Movie Selector\n")

choice = options()

# get name of movie list and watched listssswwdda
fileIN = "movies.txt"
fileOUT = "watched.txt"

# input text files of movie list and watch list
movies = open(fileIN, "r")
watched = open(fileOUT, "r+")

# inputing movies from file to container
print("Importing movie names from: ", fileIN," \n")

# movie list container both new and watched
movieList = movies.readlines()
watchedList = watched.readlines()
movies.close()

if choice == 1:
    SelectRandom()
elif choice == 2:
    unwatched()
elif choice == 3:
    watched()
elif choice == 4:
    addList()

# remove watched items from movie list
for title in watchedList:
    for item in movieList:
        if title in item:
            movieList.remove(item)
            break

# list sizes
movieSize = int(len(movieList))

print("Import Complete\n")
print(movieSize, "unwatched movie(s) have been imported into the program\n")

'''for k in movieList:
    print(k.rstrip('\n'))

print("test of writing to file")
writeFile = open("wat.txt", "w+")

movieList[1] = "this is a new line added by the program to the text file\n"

for tit in movieList:
    writeFile.write(tit)

writeFile.close()'''