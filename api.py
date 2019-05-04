"""Summary
"""
import json
import requests

import config

from requests.exceptions import HTTPError


class YiPy(object):
    def __init__(self):
        self.endpoint = None
        self.payload = None

    def __make_request(self):
        """Make the request in a controlled environment.

        Returns:
            dict: the json response from the API or json formatted errors
        """
        try:
            for key, value in self.payload.items():
                if isinstance(value, bool):
                    self.payload[key] = json.dumps(value)
            response = requests.get(
                f'{config.YTS_API_URL}{self.endpoint}',
                params=self.payload)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            return {'status': response.status_code, 'status_message': http_err}
        except Exception as err:
            return {'status': response.status_code, 'status_message': err}
        else:
            return response.json()

    def list(self, limit=20, page=1, quality='All', minimum_rating=0,
             query_term='0', genre='All', sort_by='date_added',
             order_by='desc', with_rt_ratings=False):
        """
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
        """

        self.endpoint = 'list_movies.json'
        self.payload = {
            'limit': limit,
            'page': page,
            'quality': quality,
            'minimum_rating': minimum_rating,
            'query_term': query_term,
            'genre': genre,
            'sort_by': sort_by,
            'order_by': order_by,
            'with_rt_ratings': with_rt_ratings}

        return self.__make_request()

    def movie_details(self, movie_id, with_images=False, with_cast=False):
        """Returns the information about a specific movie.

        Args:
            movie_id (int): The ID of the movie

            with_images (bool, optional): When set the data returned will
                include the added image URLs

            with_cast (bool, optional): When set the data returned will
                include the added information about the cast

        Returns:
            dict: the json response from the API
        """

        self.endpoint = 'movie_details.json'
        self.payload = {
            'movie_id': movie_id,
            'with_images': with_images,
            'with_cast': with_cast
        }
        return self.__make_request()

    def movie_suggestions(self, movie_id):
        """Returns 4 related movies as suggestions for the user.

        Args:
            movie_id (int): The ID of the movie

        Returns:
            dict: the json response from the API
        """
        self.endpoint = 'movie_suggestions.json'
        self.payload = {'movie_id': movie_id}
        return self.__make_request()

    def movie_comments(self, movie_id):
        """Returns all the comments for the specified movie.

        Args:
            movie_id (int): The ID of the movie

        Returns:
            dict: the json response from the API
        """
        self.endpoint = 'movie_comments.json'
        self.payload = {'movie_id': movie_id}
        return self.__make_request()

    def movie_reviews(self, movie_id):
        """Returns all the IMDb movie reviews for the specified movie.

        Args:
            movie_id (int): The ID of the movie

        Returns:
            dict: the json response from the API
        """
        self.endpoint = 'movie_reviews.json'
        self.payload = {'movie_id': movie_id}
        return self.__make_request()

    def movie_parental_guides(self, movie_id):
        """Returns all the parental guide ratings for the specified movie.

        Args:
            movie_id (int): The ID of the movie

        Returns:
            dict: the json response from the API
        """
        self.endpoint = 'movie_parental_guides.json'
        self.payload = {'movie_id': movie_id}
        return self.__make_request()

    def list_upcoming_movies(self):
        """Returns the 4 latest upcoming movies.

        Returns:
            dict: the json response from the API
        """
        self.endpoint = 'list_upcoming.json'
        return self.__make_request()

    def user_details(self, user_id, with_recently_downloaded=False):
        """Get a user's details.

        Args:
            user_id (int): The ID of the user

            with_recently_downloaded (bool, optional):
                If set it will add the most recent downloads by the given user

        Returns:
            dict: the json response from the API
        """
        self.endpoint = 'user_details.json'
        self.payload = {
            'user_id': user_id,
            'with_recently_downloaded': with_recently_downloaded
        }
        return self.__make_request()
