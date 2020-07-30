# get name of movie list
fileIN = "movies.txt"#input("Movie List File: ") + ".txt"
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