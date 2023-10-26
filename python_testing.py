import numpy
import pandas as pd
import pyspark

a = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(a)

print(df) 

# n first prime number