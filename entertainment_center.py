# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!
import fresh_tomatoes
import media

# Stardust movie: movie title, storyline, poster image, movie trailer,
# director, year, actors
stardust = media.Movie(
    "Stardust",
    "A fantasy about magical land in UK",
    "https://upload.wikimedia.org/wikipedia/en/6/6f/Stardust_promo_poster.jpg",  # NOQA
    "https://youtu.be/VfYBKDyF-Dk",
    "Matthew Vaughn",
    "2007",
    "Claire Danes, Charlie Cox, Sienna Miller, "
    "Robert De Niro, Michelle Pfeiffer"
    )

# V for vendetta movie: movie title, storyline, poster image, movie trailer,
# director, year, actors
v_for_vendetta = media.Movie(
    "V for Vendetta",
    "A story about revolution in the future UK",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",  # NOQA
    "https://youtu.be/k_13fFIrhPk",
    "James McTeigue",
    "2006",
    "Natalie Portman, Hugo Weaving, Stephen Rea, John Hurt"
    )

# The Mummy movie: movie title, storyline, poster image, movie trailer,
# director, year, actors
the_mummy = media.Movie(
    "The Mummy",
    "An ancient Egyptian mummy come back alive",
    "https://upload.wikimedia.org/wikipedia/en/6/68/The_mummy.jpg",  # NOQA
    "https://youtu.be/h3ptPtxWJRs",
    "Stephen Sommers",
    "1999",
    "Brendan Fraser, Rachel Weisz, John Hannah, "
    "Arnold Vosloo, Kevin J. O'Connor, Jonathan Hyde"
    )

# Inception movie: movie title, storyline, poster image, movie trailer,
# director, year, actors
inception = media.Movie(
    "Inception",
    "A thief tries to steal information from dreams of a rick guy",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
    "https://youtu.be/8hP9D6kZseM",
    "Christopher Nolan",
    "2010",
    "Leonardo DiCaprio, Ken Watanabe, Joseph Gordon-Levitt, "
    "Marion Cotillard, Ellen Page, Tom Hardy, Cillian Murphy, "
    "Tom Berenger, Michael Caine"
    )

# Ingrorious Basterds: movie title, storyline, poster image, movie trailer,
# director, year, actors
inglorious_basterds = media.Movie(
    "Inglorious Basterds",
    "The fictional alternate history story of two plots "
    "to assassinate Nazi Germany's political leadership",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",  # NOQA
    "https://youtu.be/KnrRy6kSFF0",
    "Quentin Tarantino, Eli Roth",
    "2009",
    "Brad Pitt, Christoph Waltz, Michael Fassbender, "
    "Eli Roth, Diane Kruger, Daniel Bruhl, "
    "Til Schweiger, Melanie Laurent"
    )

# The Age of Adaline: movie title, storyline, poster image, movie trailer,
# director, year, actors
the_age_of_adaline = media.Movie(
    "The Age of Adaline",
    "A story about the girl who does not age",
    "https://upload.wikimedia.org/wikipedia/en/3/33/The_Age_of_Adaline_film_poster.png",  # NOQA
    "https://youtu.be/7UzSekc0LoQ",
    "Lee Toland Krieger",
    "2015",
    "Blake Lively, Michiel Huisman, Kathy Baker, "
    "Harrison Ford, Ellen Burstyn"
    )

# movies to be passed to the media file
movies = [
    stardust,
    v_for_vendetta,
    the_mummy,
    inception,
    inglorious_basterds,
    the_age_of_adaline
    ]

# This call opens the page of movies
# from its input, a list of movie instances.
fresh_tomatoes.open_movies_page(movies)
