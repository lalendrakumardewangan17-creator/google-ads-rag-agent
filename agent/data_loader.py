import pandas as pd

def load_campaign_data(path: str) -> pd.DataFrame:
    """
    Load Google Ads campaign performance data
    """
    return pd.read_csv(path)
