MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []


def print_movie(movie):
      print(f"movie: {movie['title']}")
      print(f"directed by: {movie['director']}")
      print(f"released: {movie['year']}")


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies():
    for movie in movies:
        print_movie(movie)


def movie_search():
    search = input("Search movies by title: ")
    found = False
    for movie in movies:
        if search.lower() == movie['title'].lower():
            found = True
            print_movie(movie)
    if not found:
        print(f"Movie not found. Try another title!")

user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": movie_search
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')
        
        selection = input(MENU_PROMPT)


menu()