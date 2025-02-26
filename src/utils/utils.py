import numpy as np
import polars as pl


def reduce_mem_usage(df: pl.DataFrame) -> pl.DataFrame:
    """
    Reduce memory usage of a DataFrame.

    Args:
        df (pl.DataFrame): The DataFrame to reduce memory usage.

    Returns:
        pl.DataFrame: The DataFrame with reduced memory usage.
    """
    start_mem = df.estimated_size("mb")
    for col in df.columns:
        col_type = df[col].dtype
        if col_type != "object":
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.estimated_size("mb")
    print(f"Memory usage decreased to {end_mem} Mb ({100 * (start_mem - end_mem) / start_mem:.2f} % reduction)")
    return df