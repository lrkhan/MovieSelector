import random

def options():
    print('\n')
    print("Please select and option from below.")
    print("1) Select a Random Movie")
    print("2) View Unwatched Options")
    print("3) View Watched Videos")
    print("4) Add a Movie to List\n")

    usrChoice = int(input("I want to: "))
    print('\n')

    if usrChoice not in [1,2,3,4]:
        print("invalid option chosen")
        options()

    return usrChoice

def SelectRandom(movieList,watchedList):
    randomMovie = random.choice(movieList)
    print("The movie selected is: ", randomMovie)
    ans = input("Select this movie (y/n)?\n")
    
    if ans == 'n':
        print("Rerolling for a new movie")
        SelectRandom(movieList)
    elif ans == 'y':
        print("Added ", randomMovie, " to watched list.")
        watchedList.append(randomMovie)

        print("Removed ", randomMovie," from movie list.")
        movieList.remove(randomMovie)
    else:
        print("Invalid Option, Rerolling movie")
        SelectRandom(movieList)

def unwatched(unwatchedList):
    size = len(unwatchedList)
    print("Here is the list of unwatched movies: ", size, "\n")
    for title in unwatchedList:
        print(title.rstrip('\n'))
    print("\n---End of List---")

def watched(watchedList):
    size = len(watchedList)
    print("Here is the list of watched movies: ", size, "\n")
    for title in watchedList:
        print(title.rstrip('\n'))
    print("---End of List---")

def addList(movieFile):
    print("Add a movie to the list.\n")
    
    title = input("Title of Movie: ")
    year = input("Release Year: ")
    
    movie = "\n" + title + " (" + year +") [N/A]"

    movieFile.write(movie)
    
    print(movie," has been added to movies.txt file")

print("Welcome to the Movie Selector\n")

choice = options()

# get name of movie list and watched lists
fileIN = "movies.txt"
fileOUT = "watched.txt"

# input text files of movie list and watch list
movies = open(fileIN, "a+")
watched = open(fileOUT, "a+")

# inputing movies from file to container
print("Importing movie names from: ", fileIN,"\n")

# movie list container both new and watched
movieList = movies.readlines()
watchedList = watched.readlines()

print("Cross Refrencing with Watched Movies....\n")
# remove watched items from movie list
for title in watchedList:
    for item in movieList:
        if title in item:
            movieList.remove(item)
            break

# list sizes
movieSize = int(len(movieList))

print("Import Complete\n")

if choice == 1:
    SelectRandom(movieList, watchedList)
elif choice == 2:
    unwatched(movieList)
elif choice == 3:
    watched(watchedList)
elif choice == 4:
    addList(movies)

'''for k in movieList:
    print(k.rstrip('\n'))

print("test of writing to file")
writeFile = open("wat.txt", "w+")

movieList[1] = "this is a new line added by the program to the text file\n"

for tit in movieList:
    writeFile.write(tit)

writeFile.close()'''