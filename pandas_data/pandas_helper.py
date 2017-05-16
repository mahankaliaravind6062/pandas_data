def clean_x_with_quantile(df, cols, quantiles):
    df_ = df.copy()
    for col in cols:
        df_ = df_[((df_[col] > df_[col].quantile(quantiles[0])) & (df_[col] < df_[col].quantile(quantiles[1])))]
        df_ = df_[~df_[col].isnull()]
    return df_
