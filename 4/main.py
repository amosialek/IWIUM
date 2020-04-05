from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.ml.feature import *
import os
os.environ['JAVA_HOME'] = 'f:\\Downloads\\SPARK_READY\\Java\\jdk1.8.0_131'
os.environ['SCALA_HOME'] = 'f:\\Downloads\\SPARK_READY\\scala-2.11.7'
os.environ['SPARK_HOME'] = 'f:\\Downloads\\SPARK_READY\\spark-2.3.0-bin-hadoop2.7'
os.environ['HADOOP_HOME'] = 'f:\\Downloads\\SPARK_READY\\hadoop-2.8.3'

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

def inside(p):
    x, y = 2 * random.random(), 5 * random.random()
    return y < x*x + 1 




def zad1():
	count = sc.parallelize(xrange(0, NUM_SAMPLES)).filter(inside).count()
	print("Integral of x^2+1 in range [0,2] is roughly:", 10.0 * count / NUM_SAMPLES)
	
def zad2():
	pass
def zad3():
	pass
	
zad1()
# tu jest miejsce na twoje rozwiazanie

spark.stop()
