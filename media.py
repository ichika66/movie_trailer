# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

import webbrowser

class Movie():
    ''' This class provides a way to store movie related information '''

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_director, release_year, main_cast):
    	self.title = movie_title
    	self.storyline = movie_storyline
    	self.poster_image_url = poster_image
    	self.trailer_youtube_url = trailer_youtube
    	self.director = movie_director
    	self.year = release_year
    	self.cast = main_cast

    ''' initialize instance of class Movie '''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
