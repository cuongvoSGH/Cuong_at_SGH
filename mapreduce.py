import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

sc = SparkSession.builder.getOrCreate()

text = """
The quick brown fox jumps over the lazy dog.
But the dog wasn't that lazy, it was just tired.
"""

text = text.replace(".","")
text = text.replace(",","")
text = text.replace(chr(10)," ")
text = text.replace("  ","")
text = text.lower()

# Creating an RDD from a Python collection (list of strings)
text_rdd = sc.parallelize([text])

# MapReduce Operations
counts = (
    text_rdd.flatMap(lambda line: line.split(" ")) # Splitting the lines into words
    .map(lambda word: (word, 1)) # Mapping each word with the number 1
    .reduceByKey(lambda a, b: a + b) # Reducing by key (word) and summing the counts
)

# Collecting the results and printing
for (word, count) in counts.collect():
    print(f"{word}: {count}")