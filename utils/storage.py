import pandas as pd
from datetime import datetime

def save_assessment(mood, stress, anxiety, burnout):

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mood": mood,
        "stress": stress,
        "anxiety": anxiety,
        "burnout": burnout
    }

    df = pd.DataFrame([row])

    df.to_csv(
        "data/assessments.csv",
        mode="a",
        header=False,
        index=False
    )