from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.getOrCreate()
    
    # Example data
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    columns = ["name", "age"]
    
    df = spark.createDataFrame(data, columns)
    df.show()
    
    # Here you might do transformations or writes to Delta tables
    # df.write.format("delta").mode("append").save("/mnt/datalake/landing/test")
    
    print("ETL job finished successfully.")

if __name__ == "__main__":
    main()
