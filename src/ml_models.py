from __future__ import annotations
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split


def split_features_target(df: pd.DataFrame, target_col: str, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
	X = df.drop(columns=[target_col])
	y = df[target_col]
	return train_test_split(X, y, test_size=test_size, random_state=random_state)
