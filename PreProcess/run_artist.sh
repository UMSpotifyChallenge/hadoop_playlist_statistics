hdfs dfs -rm -r mpd_artist_output

yarn jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming.jar \
-input mpd_output \
-output mpd_artist_output \
-mapper artists_map.py \
-reducer artists_reduce.py \
-file artists_map.py \
-file artists_reduce.py \
-numReduceTasks 10
