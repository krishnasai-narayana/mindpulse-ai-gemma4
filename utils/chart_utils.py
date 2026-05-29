import pandas as pd

def save_assessment(row):
    df = pd.DataFrame([row])
    df.to_csv(
        "data/assessments.csv",
        mode="a",
        header=False,
        index=False
    )