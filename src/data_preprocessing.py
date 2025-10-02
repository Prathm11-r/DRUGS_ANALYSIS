from __future__ import annotations
import pandas as pd

from .utils import standardize_columns


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
	df = standardize_columns(df)
	# Drop completely duplicate rows
	df = df.drop_duplicates()
	return df
