def line_count(path):
	file = open(path)
	count = sum(1 for line in file)
	print(path, count)
	return count

# line_count("track_output.txt")
# line_count("artist_output.txt")
# line_count("album_output.txt")
count = 0
count += line_count("part-00003")
count += line_count("part-00001")
count += line_count("part-00004")
count += line_count("part-00009")
count += line_count("part-00008")
count += line_count("part-00006")
count += line_count("part-00007")
count += line_count("part-00000")
count += line_count("part-00005")
count += line_count("part-00002")

print(count)