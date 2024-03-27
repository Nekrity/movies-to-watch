import json

movies = []

# read movies file into variable
with open('movies.json', 'r') as openfile:
    # Reading from json file
    movies = json.load(openfile)

def sort_movies(movies_rating):
    return int(movies_rating["rating"])

while True:
    print("\nMovie Tracker Menu:")
    print("1. Pievienot filmu")
    print("2. Rādīt visas pievienotas filmas sakartotas pēc reitinga")
    print("3. Rādīt vēl neskatītās filmas")
    print("4. Atzimēt filmu kā skatītu")
    print("5. Dzēst filmu no saraksta")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        movies_add={}
        # https://www.w3schools.com/python/python_dictionaries.asp
        # https://www.w3schools.com/python/python_lists_add.asp
        movies_add["title"] = input("Enter movie title: ")
        movies_add["rating"] = float(input("Enter movie rating: "))
        movies_add["watched"] = False
        movies.append(movies_add)
        pass
    elif choice == "2":
        movies_rating=movies.copy()
        movies_rating.sort(key=sort_movies, reverse=True)
        print(movies_rating)
        # https://www.w3schools.com/python/python_lists_sort.asp
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    elif choice == "3":
        movies_notwatched = [x for x in movies if x["watched"]==False]
        print(movies_notwatched)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    elif choice == "4":
        # https://www.w3schools.com/python/python_lists_change.asp
        # https://www.w3schools.com/python/python_dictionaries_change.asp
        id = int(input("Enter the index of the movie to mark: "))
        movies[id]["watched"]=True
    elif choice == "5":
        # https://www.w3schools.com/python/python_lists_remove.asp
        id = int(input("Enter the index of the movie to remove: "))
        movies.pop(id)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# writing movies to file
with open("movies.json", "w") as movies_file:
    json.dump(movies, movies_file)