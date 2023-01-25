# Milestone project 1 - The complete python course by teclado
*A simple (temporary store) movie collection app, where users can add, list and search for movies.*

Code was refactored like suggested in lecture 57.

Search function has 2 more features :innocent:.

1. Making search not case sensitive:
   
   When transforming "search input" and "movie title" with `.lower()` to lowercase, case sensitivity is eliminated.
   
2. Display message if search can't find the movie:
   
   For this I set a boolean of `found` which is set to `True` when the loop matches a movie. If not, message is displayed.

```python
def movie_search():
    search = input("Search movies by title: ")
    found = False
    for movie in movies:
        if search.lower() == movie['title'].lower():
            found = True
            print_movie(movie)
    if not found:
        print(f"Movie not found. Try another title!")
```
