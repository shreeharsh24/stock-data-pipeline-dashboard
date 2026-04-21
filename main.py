from db import get_engine
from etl import extract, transform, load

def run_pipeline():
    print("Starting pipeline...")

    engine = get_engine()

    df = extract()
    print("Extracted data")

    df = transform(df)
    print("Transformed data")

    load(df, engine)
    print("Loaded into database")

if __name__ == "__main__":
    run_pipeline()