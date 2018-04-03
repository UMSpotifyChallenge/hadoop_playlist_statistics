# #!/usr/bin/env python
# from operator import itemgetter 
# import sys

# current_word = None 
# current_count = 0
# word = None
# # input comes from STDIN
# for line in sys.stdin:
# 	# remove leading and trailing whitespace
# 	line = line.strip()
# 	# parse the input we got from mapper.py
# 	word, count = line.split('\t', 1)
# 	# convert count (currently a string) to int
# 	try: 
# 		count = int(count)
# 	except ValueError: # count was not a number, so silently # ignore/discard this line 
# 		continue

# 	# this IF-switch only works because Hadoop sorts map output # by key (here: word) before it is passed to the reducer
# 	if current_word == word:
# 		current_count += count
# 	else:
# 		if current_word:
# 		# write result to STDOUT
# 			print '%s\t%s' % (current_word, current_count) 
# 			current_count = count
# 			current_word = word

# # do not forget to output the last word if needed!
# if current_word == word:
# 	print '%s\t%s' % (current_word, current_count)

#!/usr/bin/python2.7

import sys

# Init
current_track = None
current_count = 0
# total_pos = 0

# Input comes from stdin
for line in sys.stdin:

	data, count = line.split('\t',1)
	# cur_line, pos = data.rsplit('|',1)
	# pos = float(pos)
	count_i = int(count)

	if current_track is None:
		current_track = data

	if data == current_track:
		# total_pos += pos
		current_count += count_i

	else:
		# avg_normalized_pos = total_pos / float(current_count)
		# to_print = current_track + "|" + "{:4.3f}".format(avg_normalized_pos)
		print('{0}\t{1}'.format(current_track,str(current_count)))
		# total_pos = pos
		current_count = count_i
		current_track = data

if data == current_track:
	print(data + '\t' + str(current_count))
