# check profanity 
def read_text():
    quotes=open("/Users/yongliuli/Documents/workspace/udacity_nd000/movie_quotes.txt")
    contents_of_files=quotes.read()
    print contents_of_files
    quotes.close()
read_text()