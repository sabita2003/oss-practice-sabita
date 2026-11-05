
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(
    description="Display a simple student introduction."
)
parser.add_argument("--name", default="Student")
args = parser.parse_args()

student_info = [
    ["Name", args.name],
    ["Course", "Open Source Software"],
    ["Chapter", "Chapter 8"],
    ["Learning", "Python programming"],
    ["Library", "Tabulate"]
]

print("\nWelcome to my OSS practice project!\n")
print(tabulate(
    student_info,
    headers=["Information", "Details"],
    tablefmt="grid"
))
