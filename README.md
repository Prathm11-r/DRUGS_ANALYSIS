# Drugs Analysis Project

Analyze and model the `drugs_side_effects_drugs_com` dataset with a modular pipeline: preprocessing, EDA, visualization, and basic ML.

## Structure
```
drugs_analysis_project/
├── .vscode/
├── data/
├── src/
│   ├── data_preprocessing.py
│   ├── eda_analysis.py
│   ├── ml_models.py
│   ├── visualization.py
│   └── utils.py
├── notebooks/
├── reports/
├── sql/
├── tests/
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

## Dataset
Place `drugs_side_effects_drugs_com.csv` in the project root or `data/`.

## Quickstart
```bash
python -m venv .venv
. .venv/Scripts/Activate.ps1    # Windows PowerShell
pip install -r requirements.txt
python main.py
```

## Notes
- Default theme: seaborn whitegrid
- Figures saved to `reports/`
