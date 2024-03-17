from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

spark = SparkSession.builder \
                    .master("spark://spark-master:7077") \
                    .appName('Job Example') \
                    .getOrCreate()

input_path = '/opt/shared_environment/data/input/adventureworks_products.csv'
output_path = '/opt/shared_environment/data/output/adventureworks_products/'

df = spark.read.csv(input_path, 
                    sep='\t', 
                    header=True)

for column_name in df.columns:
    novo_nome = column_name.replace(" ", "_").lower()
    df = df.withColumnRenamed(column_name, novo_nome)

df_step1 = df.withColumn("standard_cost", regexp_replace(col("standard_cost"), "\$", "").cast("float"))
df_step1.write.save(path=output_path, format='parquet', mode='overwrite')
