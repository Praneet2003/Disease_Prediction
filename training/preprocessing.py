from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DiseasePrediction") \
    .getOrCreate()

# Load dataset
df = spark.read.csv(
    "../data/disease.csv",
    header=True,
    inferSchema=True
)

# Display dataset information
print("Total Rows:", df.count())
print("Total Columns:", len(df.columns))

df.printSchema()

df.show(5, truncate=False)