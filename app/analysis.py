import pandas as pd

def load_data():
    df = pd.read_csv("data/accidents.csv")
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['Hour'] = df['Start_Time'].dt.hour
    return df

def accidents_by_hour():
    df = load_data()
    return df['Hour'].value_counts().sort_index().to_dict()
