current_movies = { ' Connan ' : '11h30pm',
                   'Doremon' : '10h30am',
                   'Superman':'11h20am',
                   'spiderman': '2h50am'}
print("we're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('what movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print(" Requested showtime isn't playing")
else:
    print(movie, 'is playing at', showtime)