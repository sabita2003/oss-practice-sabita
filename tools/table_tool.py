import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser(description="Filter server data")
parser.add_argument("csv_path", help="Path to the CSV file")
args = parser.parse_args()

df = pd.read_csv(args.csv_path)

# My filter: show servers with CPU usage above 50%
result = df[df["cpu"] > 50]

table = Table(title="Server Information")

for column in result.columns:
    table.add_column(column)

for _, row in result.iterrows():
    table.add_row(*[str(value) for value in row])

console = Console()
console.print(table)

result.to_excel("result.xlsx", index=False)
print("Saved result.xlsx")