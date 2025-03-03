from app.extract import extract_html
from app.extract import extract_country_population_save_csv
from app.transform import PopulationDataProcessor
from pyspark.sql import SparkSession

def main():
    URL = 'https://www.worldometers.info/world-population/population-by-country/'

    website_html = extract_html(URL)
    extract_country_population_save_csv(website_html)
    
    spark = SparkSession.builder.appName("CSV to parquert").getOrCreate()
    csv_path = "populacao_paises.csv"  
    output_path = "populacao_paises_processado.parquet"
    
    processor = PopulationDataProcessor(spark, csv_path, output_path)   
    processor.process()

if __name__ == '__main__':
    main()
    
    
    