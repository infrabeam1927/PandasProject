"""Load the 2025-26 football dataset and display its column headers."""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

if __name__ == "__main__":
	Barca={}
	DATA_FILE = Path(__file__).parent / "Football Data Source" / "season-2526.csv"
	matches = pd.read_csv(DATA_FILE)
	matches['Date'] = pd.to_datetime(matches['Date'])
	print("Dataset headers:")
	for header in matches.columns:
		print(header)
	Barca['matches']=matches[(matches['HomeTeam'] == 'Barcelona')|(matches['AwayTeam'] == 'Barcelona')]
	print(Barca['matches'])	
	Barca['Homewins']=Barca['matches'][(Barca['matches']['HomeTeam'] == 'Barcelona') & (Barca['matches']['FTR'] == 'H')]
	print(Barca['Homewins'])
	Barca['Awaywins']=Barca['matches'][(Barca['matches']['AwayTeam'] == 'Barcelona') & (Barca['matches']['FTR'] == 'A')]
	print(Barca['Awaywins'])
	Barca['Homewins'].plot(x='AwayTeam', y='FTHG', kind='scatter', title='Barcelona Home Goals Over Time')
	plt.show()
	root = tk.Tk()
	root.mainloop()
    
	plt.savefig('Barcelona_Home_Goals_Over_Time.png')
	