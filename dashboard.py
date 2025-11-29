import csv


def load_data(path):
    records = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(
                {
                    "timestamp": row["timestamp"],
                    "traffic_in": int(row["traffic_in"]),
                    "traffic_out": int(row["traffic_out"]),
                    "errors": int(row["errors"]),
                }
            )
    return records


def summarize(records):
    total_in = sum(r["traffic_in"] for r in records)
    total_out = sum(r["traffic_out"] for r in records)
    total_errors = sum(r["errors"] for r in records)

    max_in = max(records, key=lambda r: r["traffic_in"])
    max_out = max(records, key=lambda r: r["traffic_out"])

    n = len(records)
    return {
        "points": n,
        "total_in": total_in,
        "total_out": total_out,
        "avg_in": total_in // n,
        "avg_out": total_out // n,
        "total_errors": total_errors,
        "max_in": max_in,
        "max_out": max_out,
    }


def print_dashboard(stats):
    print("====== Network Traffic Dashboard ======")
    print(f"Data points         : {stats['points']}")
    print()
    print("Traffic (bytes)")
    print(f"  Total IN          : {stats['total_in']}")
    print(f"  Total OUT         : {stats['total_out']}")
    print(f"  Average IN        : {stats['avg_in']}")
    print(f"  Average OUT       : {stats['avg_out']}")
    print()
    print("Errors")
    print(f"  Total errors      : {stats['total_errors']}")
    print()
    print("Peaks")
    print(
        f"  Peak IN  at {stats['max_in']['timestamp']}  "
        f"-> {stats['max_in']['traffic_in']} bytes"
    )
    print(
        f"  Peak OUT at {stats['max_out']['timestamp']} "
        f"-> {stats['max_out']['traffic_out']} bytes"
    )


def main():
    data = load_data("network_data.csv")
    stats = summarize(data)
    print_dashboard(stats)


if __name__ == "__main__":
    main()

