from __future__ import annotations
from pathlib import Path
import pandas as pd


def summarize(df: pd.DataFrame) -> dict:
	return {
		"shape": df.shape,
		"columns": list(df.columns),
		"dtypes": df.dtypes.astype(str).to_dict(),
		"missing_ratio": df.isna().mean().to_dict(),
	}


def save_profile(df: pd.DataFrame, out_path: Path) -> None:
	# Placeholder for future profiling report generation
	out_path.write_text("EDA profile placeholder")
