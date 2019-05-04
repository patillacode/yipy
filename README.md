# YiPy
A Python wrapper for [Yify API](https://yts.am/api)

_Only public methods are implemented, no authorization required._

# Examples

```python
from yipy import YiPy

api = YiPy()

# Get movies list
movie_list = api.list(limit=10)

# Get movie details
movie_details = api.movie_details(movie_id=5496)

# Get movie suggestions
movie_suggestions = api.movie_suggestions(movie_id=5496)

# Get movie comments
movie_comments = api.movie_comments(movie_id=5496)

# Get movie reviews
movie_reviews = api.movie_reviews(movie_id=5496)

# Get movie parental_guides
movie_parental_guides = api.movie_parental_guides(movie_id=5496)

# Get list_ pcoming_movies
list_upcoming_movies = api.list_upcoming_movies()

# Get user details
user_details = api.user_details(user_id=16)
```


# Available methods

**`list`**

```
Used to list and search through out all the available movies.

Can sort, filter, search and order the results.

Args:
    limit (int, optional): between 1 - 50 (inclusive)
        The limit of results per page that has been set

    page (int, optional): Used to see the next page of movies
        eg limit=15 and page=2 will show you movies 15-30

    quality (str, optional): 720p, 1080p, 3D Used to filter by quality

    minimum_rating (int, optional): between 0 - 9 (inclusive)
        Used to filter movie by a given minimum IMDb rating

    query_term (str, optional): Used for movie search, matching on:
        Movie Title/IMDb Code
        Actor Name/IMDb Code
        Director Name/IMDb Code

    genre (str, optional): Used to filter by a given genre
        See http://www.imdb.com/genre/ for full list

    sort_by (str, optional): Sorts the results by choosen value:
        title, year, rating, peers, seeds, download_count,
        like_count, date_added

    order_by (str, optional): asc, desc
        Orders the results by either Ascending or Descending order

    with_rt_ratings (bool, optional): Returns the list with the
        Rotten Tomatoes rating included

Returns:
    dict: the json response from the API
```

**`movie_details`**
```
Returns the information about a specific movie.

Args:
    movie_id (int): The ID of the movie

    with_images (bool, optional): When set the data returned will
        include the added image URLs

    with_cast (bool, optional): When set the data returned will
        include the added information about the cast

Returns:
    dict: the json response from the API
```

**`movie_suggestions`**
```
Returns 4 related movies as suggestions for the user.

Args:
    movie_id (int): The ID of the movie

Returns:
    dict: the json response from the API
```

**`movie_comments`**
```
Returns all the comments for the specified movie.

Args:
    movie_id (int): The ID of the movie

Returns:
    dict: the json response from the API
```

**`movie_reviews`**
```
Returns all the IMDb movie reviews for the specified movie.

Args:
    movie_id (int): The ID of the movie

Returns:
    dict: the json response from the API
```

**`movie_parental_guides`**
```
Returns all the parental guide ratings for the specified movie.

Args:
    movie_id (int): The ID of the movie

Returns:
    dict: the json response from the API
```

**`list_upcoming_movies`**
```
Returns the 4 latest upcoming movies.

Returns:
    dict: the json response from the API
```

**`user_details`**
```
Get a user's details.

Args:
    user_id (int): The ID of the user

    with_recently_downloaded (bool, optional):
        If set it will add the most recent downloads by the given user

Returns:
    dict: the json response from the API
```
