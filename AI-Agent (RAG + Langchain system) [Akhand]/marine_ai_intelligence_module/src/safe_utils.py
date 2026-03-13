def safe_mean(df, column):

    if column not in df.columns:
        return None

    try:
        return df[column].mean()
    except:
        return None


def safe_value(value):

    if value is None:
        return "Data not available"

    try:
        return round(value, 2)
    except:
        return value