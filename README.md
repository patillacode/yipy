# YiPy
A Python wrapper for [Yify API](https://yts.am/api)

_Only public methods are implemented, no authorization required._

## Install
Plug & Play:

	$ pip install yipy

If you want to play around with the code I'd recommend creating a virtual environment first (with python3):

    $ mkvirtualenv --python=/usr/local/bin/python3 yipy


And then:

    $ git clone https://github.com/patillacode/yipy.git

    $ cd yipy

    $ pip install -r requirements.txt

    $ python setup.py develop


## Examples

```python
from yipy.api import Yipy

api = Yipy()

# Get movies list
movie_list = api.list()

# Get movie details
movie_details = api.movie_details(movie_id=5496)

# Get movie suggestions
movie_suggestions = api.movie_suggestions(movie_id=5496)

# Get movie comments
movie_comments = api.movie_comments(movie_id=5496)

# Get movie reviews
movie_reviews = api.movie_reviews(movie_id=5496)

# Get movie parental guides
movie_parental_guides = api.movie_parental_guides(movie_id=5496)

# Get list upcoming movies
list_upcoming_movies = api.list_upcoming_movies()

# Get user details
user_details = api.user_details(user_id=16)
```


## Available methods

#### list ####

>Used to list and search through out all the available movies.
>Can sort, filter, search and order the results.


Parameters:


  - `limit` _(int, optional)_: between 1 - 50 (inclusive)
	    - The limit of results per page that has been set

  - `page` _(int, optional)_: Used to see the next page of movies
	    - eg: limit=15 and page=2 will show you movies 15-30

  - `quality` _(str, optional)_: Used to filter by quality.
	  - `720p`
	  - `1080p`
	  - `3D`

  - `minimum_rating` _(int, optional)_: between 0 - 9 (inclusive)
	  - Used to filter movie by a given minimum IMDb rating

  - `query_term` _(str, optional)_: Used for movie search, matching on:
	  - Movie Title/IMDb Code
	  - Actor Name/IMDb Code
	  - Director Name/IMDb Code

  - `genre` _(str, optional)_: Used to filter by a given genre
	  - See [here](http://www.imdb.com/genre/) for full list

  - `sort_by` _(str, optional)_: Sorts the results by choosen value:
	  - `title`
	  - `year`
	  - `rating`
	  - `peers`
	  - `seeds`
	  - `download_count`
	  - `like_count`
	  - `date_added`

  - `order_by` _(str, optional)_: `asc` or `desc`
	    Orders the results by either Ascending or Descending order

  - `with_rt_ratings` _(bool, optional)_:
		- Returns the list with the Rotten Tomatoes rating included

---------------------------
#### movie_details ####

>Returns the information about a specific movie.


Parameters:

  - `movie_id` _(int)_: The ID of the movie

  - `with_images` _(bool, optional)_: When set the data returned will
	    include the added image URLs

  - `with_cast` _(bool, optional)_: When set the data returned will
	    include the added information about the cast


---------------------------
#### movie_suggestions ####

>Returns 4 related movies as suggestions for the user.

Parameters:

  - `movie_id` _(int)_: The ID of the movie

---------------------------
#### movie_comments ####

>Returns all the comments for the specified movie.

Parameters:

  - `movie_id` _(int)_: The ID of the movie

---------------------------
#### movie_reviews ####

>Returns all the IMDb movie reviews for the specified movie.

Parameters:

  - `movie_id` _(int)_: The ID of the movie

---------------------------
#### movie_parental_guides ####

>Returns all the parental guide ratings for the specified movie.

Parameters:

  - `movie_id` _(int)_: The ID of the movie

---------------------------
#### list_upcoming_movies ####

>Returns the 4 latest upcoming movies.

---------------------------
#### user_details ####

>Get a user's details.

Parameters:

  - `user_id` _(int)_: The ID of the user

  - `with_recently_downloaded` _(bool, optional)_:
	        If set it will add the most recent downloads by the given user

