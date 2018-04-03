#!/usr/bin/python2.7

import sys
import json

one = "1"

# Input comes from stdin
for line in sys.stdin:
	splitted = list(map(lambda s : s.strip(), line.split("||JhB||")))
	track_uri = splitted[0].strip().replace("spotify:track:","")
	track_name = splitted[1]
	# artist_uri = splitted[2].strip().replace("spotify:artist:","")
	# artist_name = splitted[3].strip()
	album_uri = splitted[4].strip().replace("spotify:album:","")
	# album_name = splitted[5].strip()

	dic = {}
	dic["uri"] = track_uri
	dic["name"] = track_name
	dic["album_uri"] = album_uri
	key = json.dumps(dic)
	
	print '%s\t%s' %  (key, one)
	
