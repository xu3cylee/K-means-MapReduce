#!bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
	do
		hdfs dfs -copyFromLocal -f /home/cylee/c2.txt /mda/c2.txt
		hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapperkmMHc2.py,reducerkm.py -mapper mapperkmMHc2.py -reducer reducerkm.py -input wasb:///mda/data.txt -output wasb:///mda/output0$i
		cp c2.txt c2_$i.txt
		rm c2.txt
		hdfs dfs -copyToLocal /mda/output0$i/part-00000 /home/cylee/c2.txt
	done
