import media
import fresh_tomatoes
def test():
    movies=[]
    #
    movies.append(media.Movie("JURASSIC PARK ","Evolution of a Raptor Suit",
    "https://upload.wikimedia.org/wikipedia/en/9/96/Jurassic_Park_logo.jpg",
    "https://www.youtube.com/watch?v=jAzQr3Ml0UI"))
    #
    movies.append(media.Movie("The Silence of the Lambs","Evolution of a Raptor Suit",
    "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",
    "https://www.youtube.com/watch?v=jAzQr3Ml0UI"))
    #
    movies.append(media.Movie("The Wizard of Oz(1982)","Evolution of a Raptor Suit",
    "https://upload.wikimedia.org/wikipedia/en/5/53/WizOzToho.jpg",
    "https://www.youtube.com/watch?v=jAzQr3Ml0UI"))

    #movie.show_trailer()
    fresh_tomatoes.open_movies_page(movies)




test()