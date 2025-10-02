from pathlib import Path
import pandas as pd
import pytest

from src.utils import load_csv, standardize_columns, DataLoadError


def test_load_csv_missing_error(tmp_path: Path):
	with pytest.raises(DataLoadError):
		load_csv(tmp_path / 'nope.csv', on_missing='error')


def test_standardize_columns():
	df = pd.DataFrame({" Col A ": [1, 2], "B col": [3, 4]})
	std = standardize_columns(df)
	assert list(std.columns) == ["col_a", "b_col"]
