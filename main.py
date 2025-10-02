from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from config import DATA_FILE, FIGSIZE_DEFAULT, STYLE
from src.utils import load_csv, standardize_columns


def run() -> None:
	sns.set_theme(style=STYLE)
	print(f"Loading dataset from: {DATA_FILE}")
	df = load_csv(DATA_FILE, on_missing='error')
	df = standardize_columns(df)

	print("Dataset shape:", df.shape)
	print("Columns:", list(df.columns)[:20])

	# Simple preview and basic stats
	print("\nHead:\n", df.head(5))
	numeric_cols = df.select_dtypes(include='number').columns.tolist()
	if numeric_cols:
		print("\nDescribe (numeric):\n", df[numeric_cols].describe())

	# Quick visualization example (will save to reports/ if possible)
	try:
		fig, ax = plt.subplots(figsize=FIGSIZE_DEFAULT)
		df.isna().mean().sort_values(ascending=False).head(20).plot(kind='barh', ax=ax, title='Top 20 Missing Value Ratios')
		output_path = Path('reports') / 'missing_values.png'
		output_path.parent.mkdir(parents=True, exist_ok=True)
		fig.tight_layout()
		fig.savefig(output_path)
		print(f"Saved figure: {output_path}")
	except Exception as e:
		print(f"[WARN] Could not generate visualization: {e}")


if __name__ == '__main__':
	run()
