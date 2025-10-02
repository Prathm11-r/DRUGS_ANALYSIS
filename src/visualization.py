from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from config import FIGSIZE_DEFAULT, STYLE


def plot_missingness(df: pd.DataFrame, out: Path | None = None) -> None:
	sns.set_theme(style=STYLE)
	fig, ax = plt.subplots(figsize=FIGSIZE_DEFAULT)
	df.isna().mean().sort_values(ascending=False).head(20).plot(kind='barh', ax=ax, title='Top 20 Missing Value Ratios')
	fig.tight_layout()
	if out:
		out.parent.mkdir(parents=True, exist_ok=True)
		fig.savefig(out)
	else:
		plt.show()
