def safe_mean(df,column):

    if column not in df.columns:
        return None

    try:
        return df[column].mean()
    except:
        return None