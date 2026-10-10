"""Load the 2025-26 football dataset and display its column headers."""

from pathlib import Path

import pandas as pd


DATA_FILE = Path(__file__).parent / "Football Data Source" / "season-2526.csv"
matches = pd.read_csv(DATA_FILE)
matches['Date'] = pd.to_datetime(matches['Date'])
print("Dataset headers:")
for header in matches.columns:
	print(header)
Barca_matches=matches[(matches['HomeTeam'] == 'Barcelona')|(matches['AwayTeam'] == 'Barcelona')]
print(Barca_matches)	
