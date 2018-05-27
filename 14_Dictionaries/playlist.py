playlist = {
        'title': 'My Song List',
        'author': 'Sachin',
        'songs': [
            {'title':'song1', 'artist':['blue'], 'duration': 2.5},
            {'title':'song2', 'artist':['lata','rahman'], 'duration': 5.25},
            {'title':'song3', 'artist':['garfield'], 'duration': 2.0}
        ]
}

total_length = 0

for song in playlist['songs']:
    total_length += song['duration']

print("total duration of the songs in the playlist is {0}".format(total_length))

### output is
##$ python playlist.py
#total duration of the songs in the playlist is 9.75

