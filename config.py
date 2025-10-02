import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / 'data'
REPORTS_DIR = PROJECT_ROOT / 'reports'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
SQL_DIR = PROJECT_ROOT / 'sql'

# Primary dataset file names (searched in project root and data/)
PRIMARY_DATASET_BASENAME = os.getenv('DRUGS_DATA_BASENAME', 'drugs_side_effects_drugs_com.csv')

def find_dataset_path() -> Path:
	"""Return the most likely location of the dataset file.
	Checks in project root first, then in data/.
	"""
	root_candidate = PROJECT_ROOT / PRIMARY_DATASET_BASENAME
	if root_candidate.exists():
		return root_candidate
	data_candidate = DATA_DIR / PRIMARY_DATASET_BASENAME
	return data_candidate

DATA_FILE = find_dataset_path()

# Visualization settings
FIGSIZE_DEFAULT = (10, 6)
STYLE = 'whitegrid'
RANDOM_STATE = 42
