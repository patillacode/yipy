from api import YiPy

api = YiPy()
movie_list = api.list()
# print(movie_list)

# print('#' * 30)

movie_details = api.movie_details(5496)
# print(movie_details)
movie_details_with_cast = api.movie_details(5496, with_cast=True)
# print(movie_details_with_cast['data']['movie']['cast'])

movie_suggestions = api.movie_suggestions(5496)
print('movie_suggestions', movie_suggestions)

movie_comments = api.movie_comments(5496)
print('movie_comments', movie_comments)

movie_reviews = api.movie_reviews(5496)
print('movie_reviews', movie_reviews)

movie_parental_guides = api.movie_parental_guides(5496)
print('movie_parental_guides', movie_parental_guides)

list_upcoming_movies = api.list_upcoming_movies()
print('list_upcoming_movies', list_upcoming_movies)

user_details = api.user_details(16)
print('user_details', user_details)
