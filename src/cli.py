import argparse
import os

from monitor import (
    scan_directory,
    save_baseline,
    load_baseline,
    compare_files
)


def main():
    parser = argparse.ArgumentParser(
        description="Python File Integrity Monitor"
    )

    parser.add_argument("directory", help="Directory to monitor")
    parser.add_argument(
        "--baseline",
        default="baseline.json",
        help="Baseline file location"
    )

    parser.add_argument(
        "--initialize",
        action="store_true",
        help="Create a new baseline"
    )

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Error: Directory does not exist.")
        return

    current_files = scan_directory(args.directory)

    if args.initialize:
        save_baseline(current_files, args.baseline)
        print("Baseline created successfully.")
        return

    if not os.path.isfile(args.baseline):
        print("Error: Baseline not found. Initialize first.")
        return

    old_files = load_baseline(args.baseline)

    added, modified, deleted = compare_files(
        old_files, current_files
    )

    print("\nFile Integrity Report")
    print("---------------------")
    print("Added:", added)
    print("Modified:", modified)
    print("Deleted:", deleted)


if __name__ == "__main__":
    main()
