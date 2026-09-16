import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "Resources" / "budget_data.csv"
OUTPUT_PATH = BASE_DIR / "analysis" / "analysis.txt"


def load_budget_data(csv_path):
    """Load monthly profit and loss records from a CSV file."""
    records = []

    with csv_path.open(mode="r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        required_columns = {"Date", "Profit/Losses"}
        missing_columns = required_columns.difference(reader.fieldnames or [])

        if missing_columns:
            raise ValueError(
                f"Missing required CSV columns: {sorted(missing_columns)}"
            )

        for row in reader:
            records.append(
                {
                    "month": row["Date"],
                    "amount": int(row["Profit/Losses"]),
                }
            )

    if not records:
        raise ValueError("The budget dataset contains no records.")

    return records


def analyze_budget_data(records):
    """Calculate summary statistics for the financial records."""
    total_months = len(records)
    total_amount = sum(record["amount"] for record in records)

    monthly_changes = [
        {
            "month": current["month"],
            "change": current["amount"] - previous["amount"],
        }
        for previous, current in zip(records, records[1:])
    ]

    if monthly_changes:
        average_change = sum(
            record["change"] for record in monthly_changes
        ) / len(monthly_changes)

        greatest_increase = max(
            monthly_changes,
            key=lambda record: record["change"],
        )
        greatest_decrease = min(
            monthly_changes,
            key=lambda record: record["change"],
        )
    else:
        average_change = 0.0
        greatest_increase = {
            "month": records[0]["month"],
            "change": 0,
        }
        greatest_decrease = {
            "month": records[0]["month"],
            "change": 0,
        }

    return {
        "total_months": total_months,
        "total_amount": total_amount,
        "average_change": average_change,
        "greatest_increase": greatest_increase,
        "greatest_decrease": greatest_decrease,
    }


def format_analysis(results):
    """Create one report for both terminal and file output."""
    increase = results["greatest_increase"]
    decrease = results["greatest_decrease"]

    return "\n".join(
        [
            "Financial Analysis",
            "----------------------------",
            f"Total Months: {results['total_months']}",
            f"Total: ${results['total_amount']}",
            f"Average Change: ${results['average_change']:.2f}",
            (
                "Greatest Increase in Profits: "
                f"{increase['month']} (${increase['change']})"
            ),
            (
                "Greatest Decrease in Profits: "
                f"{decrease['month']} (${decrease['change']})"
            ),
        ]
    )


def write_analysis(output_path, report):
    """Write the completed financial report to a text file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"{report}\n", encoding="utf-8")


def main():
    """Run the complete PyBank analysis."""
    records = load_budget_data(INPUT_PATH)
    results = analyze_budget_data(records)
    report = format_analysis(results)

    print(report)
    write_analysis(OUTPUT_PATH, report)


if __name__ == "__main__":
    main()