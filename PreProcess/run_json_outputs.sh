hdfs dfs -rm -r mpd_artist_output

yarn jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming.jar \
-input mpd_output \
-output mpd_artist_output \
-mapper artists_map.py \
-reducer json_reduce.py \
-file artists_map.py \
-file json_reduce.py \
-numReduceTasks 10

hdfs dfs -rm -r mpd_album_output

yarn jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming.jar \
-input mpd_output \
-output mpd_album_output \
-mapper album_map.py \
-reducer json_reduce.py \
-file album_map.py \
-file json_reduce.py \
-numReduceTasks 10

hdfs dfs -rm -r mpd_track_output

yarn jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming.jar \
-input mpd_output \
-output mpd_track_output \
-mapper track_map.py \
-reducer json_reduce.py \
-file track_map.py \
-file json_reduce.py \
-numReduceTasks 10
