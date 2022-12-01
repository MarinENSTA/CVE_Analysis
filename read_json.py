import findspark

findspark.init()

import spark

import configparser

config = configparser.ConfigParser()
import json
import requests
from pyspark.sql import SQLContext, Row
from pyspark import SparkContext
import pyspark.sql
from pyspark.sql import SparkSession


from pyspark import SparkContext as sc, SparkConf

spark = SparkSession.builder.master("local").appName("test").getOrCreate()




#df = spark.read.option("multiline","true").json("/home/marins/3A-ENSTA/Big data project/nvdcve-1.1-2022.json")

df = spark.read.option("multiline","true").json("/Users/nicolassigal/Desktop/Scolaire/ENSTA/3A/ASI322/PROJECT/CVE_Analysis/test_cve.json")

print("Schema initial : ")
df.printSchema()

#df.show()
# print("Columns : ",df.columns)
#df.select("impact").show()

#df.printSchema()


from pyspark.sql.functions import *

df = df.select(explode(col("CVE_Items")))

print("Columns : ",df.columns)

df.printSchema()


df = df.select("col.cve.CVE_data_meta.*","col.impact.baseMetricV3.cvssV3.*").drop("version")


print("Columns : ",df.columns)
df.printSchema()

print(df.count())
df.show()

print(df.tail(1))