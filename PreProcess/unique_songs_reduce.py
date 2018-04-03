#!/usr/bin/python2.7

import sys

# Init
current_track = None
current_count = 0
total_pos = 0

# Input comes from stdin
for line in sys.stdin:

	data, count = line.split('\t',1)
	cur_line, pos = data.rsplit('||JhB||',1)
	pos = float(pos)
	count_i = int(count)

	if current_track is None:
		current_track = cur_line

	if cur_line == current_track:
		total_pos += pos
		current_count += count_i

	else:
		avg_normalized_pos = total_pos / float(current_count)
		to_print = current_track + "||JhB||" + "{:4.3f}".format(avg_normalized_pos)
		print('{0}\t{1}'.format(to_print,str(current_count)))
		total_pos = pos
		current_count = count_i
		current_track = cur_line

if data == current_track:
	print(data + '\t' + str(current_count))

