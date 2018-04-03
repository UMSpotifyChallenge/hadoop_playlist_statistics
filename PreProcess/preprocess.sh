yarn jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming.jar \
-input data \
-output mpd_output \
-mapper unique_songs_map.py \
-reducer unique_songs_reduce.py \
-file unique_songs_map.py \
-file unique_songs_reduce.py \
-numReduceTasks 10

