# Python Challenge: Financial and Election Analysis

Two Python command-line programs that analyze CSV datasets and generate summary reports. **PyBank** summarizes monthly financial records, while **PyPoll** counts votes and identifies election winners.

Originally completed for the OSU Data Analytics Bootcamp, this project was later refactored to use reusable functions, portable file paths, and consistent terminal and text-file reports.

## Technologies

- Python 3
- `csv` for reading CSV data
- `pathlib` for file and directory paths

Both programs use only the Python standard library. No third-party packages are required.

## Project Files

| File | Purpose |
| --- | --- |
| `PyBank/main.py` | Financial analysis program |
| `PyBank/Resources/budget_data.csv` | Monthly financial records |
| `PyBank/analysis/analysis.txt` | Generated financial report |
| `PyPoll/main.py` | Election analysis program |
| `PyPoll/Resources/election_data.csv` | Election records |
| `PyPoll/analysis/analysis.txt` | Generated election report |
| `docs/assignment.md` | Original assignment instructions and grading rubric |

## Getting Started

Clone the repository and enter its directory:

```bash
git clone https://github.com/a1990alpalo/Python-challege.hw.git
cd Python-challege.hw
```

Run each program from the repository root:

```bash
python PyBank/main.py
python PyPoll/main.py
```

Each program prints its results in the terminal and saves the same report in its own `analysis` folder. The folder is created automatically if needed, and running the program again replaces the previous report.

Data and output paths are resolved relative to each script, so they do not depend on a specific username or computer.

## PyBank: Financial Analysis

PyBank reads the `Date` and `Profit/Losses` columns from `budget_data.csv` and calculates:

- Total number of monthly records.
- Net total profit and loss.
- Average change between consecutive monthly records.
- Greatest increase and decrease, including their dates.

The average change uses the differences between consecutive records—not the average of the monthly profit and loss amounts. The input records must already be in chronological order.

### Expected Results for the Provided Dataset

```text
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

### Functions

| Function | Responsibility |
| --- | --- |
| `load_budget_data()` | Validate required columns and load financial records |
| `analyze_budget_data()` | Calculate totals and changes between records |
| `format_analysis()` | Build the financial report |
| `write_analysis()` | Save the report to a text file |
| `main()` | Coordinate the analysis workflow |

Missing required columns and empty datasets raise descriptive errors. Profit and loss values must be integers. For a single record, the program reports zero for the change statistics because no consecutive-record comparison is available.

## PyPoll: Election Analysis

PyPoll reads the `Candidate` column from `election_data.csv`, treats each data row as one vote, and calculates:

- Total votes cast.
- Votes received by each candidate.
- Each candidate's percentage of the total.
- The winner, or all tied winners.

### Results for the Provided Dataset

```text
Election Results
--------------------------
Total Votes: 369711
--------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
--------------------------
Winner: Diana DeGette
--------------------------
```

### Functions

| Function | Responsibility |
| --- | --- |
| `count_votes()` | Count total votes and votes per candidate |
| `build_report()` | Calculate percentages and format election results |
| `save_report()` | Save the report to a text file |
| `main()` | Coordinate the analysis workflow |

When no votes are found, the report states that no votes were found. When candidates tie for the highest count, the report lists them under `Tie`.

The program assumes the input contains a `Candidate` column and valid candidate names. It counts rows without checking for duplicate ballot identifiers.

## Refactoring Improvements

- Replaced hardcoded Windows paths with script-relative paths.
- Organized each analysis into functions with focused responsibilities.
- Used named CSV columns through `csv.DictReader`.
- Created each report once for consistent terminal and file output.
- Added automatic output-directory creation.
- Used `if __name__ == "__main__":` guards so functions can be imported without running the full analysis.

## Validation

The PyPoll script was run against the provided election dataset. Its terminal and saved reports matched, showing 369,711 votes and Diana DeGette as the winner with 73.812%.

Git whitespace checks passed before the PyPoll refactor was committed.

The PyBank results above are the expected values provided in the original assignment. To check both programs locally, run:

```bash
python PyBank/main.py
python PyPoll/main.py
```

Compare the terminal output with each generated `analysis/analysis.txt` file and the results shown above.

## Assignment Background

The datasets and original requirements came from the OSU Data Analytics Bootcamp Module 3 Python Challenge. The original instructions are preserved in [docs/assignment.md](docs/assignment.md).