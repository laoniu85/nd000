import media
import fresh_tomatoes
def test():
    movie=media.Movie("title","stroyline",
    "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
    "https://www.youtube.com/watch?v=jAzQr3Ml0UI")
    #movie.show_trailer()
    fresh_tomatoes.open_movies_page([movie])




test()