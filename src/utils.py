from __future__ import annotations
from pathlib import Path
from typing import Optional
import pandas as pd

class DataLoadError(Exception):
	pass

def load_csv(csv_path: Path | str, *, on_missing: str = 'error', dtype: Optional[dict] = None, encoding: str = 'utf-8') -> pd.DataFrame:
	"""Load a CSV into a DataFrame with helpful errors.

	on_missing: 'error' | 'warn' | 'empty'
	"""
	p = Path(csv_path)
	if not p.exists():
		msg = f"CSV not found at {p}"
		if on_missing == 'error':
			raise DataLoadError(msg)
		if on_missing == 'warn':
			print(f"[WARN] {msg}")
		return pd.DataFrame() if on_missing in {'warn','empty'} else None  # type: ignore[return-value]

	try:
		df = pd.read_csv(p, dtype=dtype, encoding=encoding)
	except UnicodeDecodeError:
		df = pd.read_csv(p, dtype=dtype, encoding='utf-8-sig')
	return df

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
	df = df.copy()
	df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
	return df
