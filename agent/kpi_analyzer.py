def compute_kpis(df):
    df = df.copy()

    df["CTR"] = df["clicks"] / df["impressions"]
    df["CPC"] = df["cost"] / df["clicks"]
    df["CPA"] = df["cost"] / df["conversions"]

    return df
