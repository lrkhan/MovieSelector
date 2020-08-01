import random

global run
run = True

def options():
    print('\n')
    print("Please select and option from below.")
    print("1) Select a Random Movie")
    print("2) View Unwatched Options")
    print("3) View Watched Videos")
    print("4) Add a Movie to List")
    print("5) Exit\n")

    usrChoice = int(input("I want to: "))
    print('\n')

    if usrChoice not in [1,2,3,4,5]:
        print("invalid option chosen")
        options()

    return usrChoice

def SelectRandom(movieList, watchedList):
    randomMovie = random.choice(movieList)
    print("The movie selected is: ", randomMovie)
    ans = input("Select this movie (y/n)?\n")
    chosenMovie = randomMovie.rstrip('\n')

    if ans == 'n':
        print("Rerolling for a new movie")
        SelectRandom(movieList, watchedList)
    elif ans == 'y':
        print("Added", chosenMovie, " to watched list.")
        watchedList.append(randomMovie)

        print("Removed ", chosenMovie," from movie list.")
        movieList.remove(randomMovie)
    else:
        print("Invalid Option, Rerolling movie")
        SelectRandom(movieList, watchedList)

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

def main(): 
    print("Welcome to the Movie Selector\n")

    choice = options()

    # get name of movie list and watched lists
    fileIN = "movies.txt"
    fileOUT = "watched.txt"

    # input text files of movie list and watch list
    movies = open(fileIN, "r+")
    watched = open(fileOUT, "r+")

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
        SelectRandom(movieList,watchedList)
        
        print("Saving progress and writing to files.\n")
        
        # closing open file streams
        movies.close()
        watched.close()
        
        # open write up files
        movie = open(fileIN, "w+")
        watch = open(fileOUT, "w+")

        # write out list into files
        for title in movieList:
            movie.write(title)

        for title in watchedList:
            watch.write(title) 

        # close files streams
        movie.close()
        watch.close()

    elif choice == 2:
        unwatched(movieList)

        # closing open file streams
        movies.close()
        watched.close()
    elif choice == 3:
        watched(watchedList)

        # closing open file streams
        movies.close()
        watched.close()
    elif choice == 4:
        addList(movies)

        # closing open file streams
        movies.close()
        watched.close()
    elif choice == 5:
        # closing open file streams
        movies.close()
        watched.close()
        
        # open write up files
        movie = open(fileIN, "w+")
        watch = open(fileOUT, "w+")

        # changing bool value for run for the while loop
        global run
        run = False

        # display closing messages
        endGame()

        # write out list into files
        for title in movieList:
            movie.write(title)

        for title in watchedList:
            watch.write(title) 

        # close files streams
        movie.close()
        watch.close()

def endGame():
    print("Saving changes to associated files.")
    print("Exiting Program.\n")

while run:
    main()