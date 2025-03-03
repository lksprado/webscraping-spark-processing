from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

class PopulationDataProcessor:
    def __init__(self, spark: SparkSession, csv_path: str, output_path: str):
        self.spark = spark
        self.csv_path = csv_path
        self.output_path = output_path
        self.df = None
    
    def read_csv(self):
        """Le o arquivo CSV"""
        self.df = self.spark.read.csv(self.csv_path, header=True, inferSchema=True)

    def clean_data(self):
        """Ajusta tipo de dado"""
        self.df = self.df.withColumn("population", regexp_replace(col("population"), ",", "").cast("long"))
        self.df = self.df.withColumn("rate", regexp_replace(col("rate"), " %", "").cast("double"))
    
    def filter_data(self):
        """Manter populacao acima de 1M"""
        self.df = self.df.filter(col("population") > 1000000)
    
    def calculate_population_2030(self):
        """Populacao projetada em 2030"""
        self.df = self.df.withColumn("populacao_em_2030", 
                                     (col("population") * pow((1 + col("rate") / 100), 6)).cast("long"))
    
    def rename_columns(self):
        """Renomeia as colunas"""
        self.df = self.df.withColumnRenamed("country", "pais") \
                         .withColumnRenamed("population", "populacao") \
                         .withColumnRenamed("rate", "taxa_crescimento")

    def write_parquet(self):
        """Escreve parquet"""
        self.df.write.parquet(self.output_path)

    def process(self):
        """Metodo executor"""
        self.read_csv()
        self.clean_data()
        self.filter_data()
        self.calculate_population_2030()
        self.rename_columns()
        self.write_parquet()


if __name__ == "__main__":
    spark = SparkSession.builder.appName("CSV to Parquet").getOrCreate()

    csv_path = "populacao_paises.csv"
    output_path = "populacao_paises_processado.parquet"
    
    processor = PopulationDataProcessor(spark, csv_path, output_path)
    processor.process()
