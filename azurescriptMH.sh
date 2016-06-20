#!bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
	do
		hdfs dfs -copyFromLocal -f /home/cylee/c1.txt /mda/c1.txt
		hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapperkmMH.py,reducerkm.py -mapper mapperkmMH.py -reducer reducerkm.py -input wasb:///mda/data.txt -output wasb:///mda/output0$i
		cp c1.txt c1_$i.txt
		rm c1.txt
		hdfs dfs -copyToLocal /mda/output0$i/part-00000 /home/cylee/c1.txt
	done
