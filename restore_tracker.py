import csv
import sys


def evaluate(row):
    rto_ok = int(row["restore_minutes"]) <= int(row["rto_minutes"])
    rpo_ok = int(row["data_loss_minutes"]) <= int(row["rpo_minutes"])
    return "pass" if rto_ok and rpo_ok else "fail"


def failures(rows):
    return [row["workload"] for row in rows if evaluate(row) == "fail"]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in failures(list(csv.DictReader(handle))):
            print(item)


if __name__ == "__main__":
    main(sys.argv[1])
