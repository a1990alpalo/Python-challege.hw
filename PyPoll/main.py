import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "Resources" / "election_data.csv"
OUTPUT_PATH = BASE_DIR / "analysis" / "analysis.txt"


def count_votes(csv_path):
    """Read the election CSV and count votes for each candidate."""
    candidates = {}
    total_votes = 0

    with csv_path.open(newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            candidate = row["Candidate"]
            candidates[candidate] = candidates.get(candidate, 0) + 1
            total_votes += 1

    return total_votes, candidates


def build_report(total_votes, candidates):
    """Build one report for both the terminal and the output file."""
    if total_votes == 0:
        return "Election Results\nNo votes found.\n"

    highest_votes = max(candidates.values())
    winners = [
        candidate
        for candidate, votes in candidates.items()
        if votes == highest_votes
    ]

    separator = "--------------------------"
    lines = [
        "Election Results",
        separator,
        f"Total Votes: {total_votes}",
        separator,
    ]

    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        lines.append(f"{candidate}: {percentage:.3f}% ({votes})")

    winner_label = "Winner" if len(winners) == 1 else "Tie"
    lines.extend([
        separator,
        f"{winner_label}: {', '.join(winners)}",
        separator,
    ])

    return "\n".join(lines) + "\n"


def save_report(report, output_path):
    """Create the output directory if needed and save the report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")


def main():
    """Run the election analysis."""
    total_votes, candidates = count_votes(INPUT_PATH)
    report = build_report(total_votes, candidates)

    print(report, end="")
    save_report(report, OUTPUT_PATH)


if __name__ == "__main__":
    main()