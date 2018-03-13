#!/usr/bin/python2.7

import sys
import re

artist_uri = ""
artist_name = ""
album_uri = ""
album_name = ""
track_uri = ""
track_name = ""
one = "1"
num_tracks = ""
pos = ""
done = 0

# Input comes from stdin
for line in sys.stdin:

	if "num_tracks" in line:
		num_tracks = line.split(':',1)[1]
		num_tracks = float(re.sub('[",\n\t]','',num_tracks))

	if '"pos":' in line:
		pos = line.split(':',1)[1]
		pos = float(re.sub('[",\n\t]','',pos))

	if "artist_name" in line:
		artist_name = line.split(':',1)[1]
		artist_name = re.sub('[",\n\t]','',artist_name)

	elif "artist_uri" in line:
		artist_uri = line.split(':',1)[1]
		artist_uri = re.sub('[",\n\t]','',artist_uri)

	elif "album_name" in line:
		album_name = line.split(':',1)[1]
		album_name = re.sub('[",\n\t]','',album_name)
		done = 1

	elif "album_uri" in line:
		album_uri = line.split(':',1)[1]
		album_uri = re.sub('[",\n\t]','',album_uri)

	elif "track_uri" in line:
		track_uri = line.split(':',1)[1]
		track_uri = re.sub('[",\n\t]','',track_uri)

	elif "track_name" in line:
		track_name = line.split(':',1)[1]
		track_name = re.sub('[",\n\t]','',track_name)

	# Check to see if we have all the data we need
	if done == 1:
		normalized_position = "{:4.3f}".format(float(pos / num_tracks))
		to_print = [track_uri, track_name, artist_uri, artist_name, album_uri, album_name, normalized_position]
		to_print_string = "|".join(to_print)
		print('{0}\t{1}'.format(to_print_string,one))
		done = 0
