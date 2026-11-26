import os
import json

from hash_utils import calculate_file_hash


def scan_directory(directory):
    file_hashes = {}

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            relative_path = os.path.relpath(file_path, directory)

            file_hash = calculate_file_hash(file_path)

            file_hashes[relative_path] = file_hash

    return file_hashes


def save_baseline(file_hashes, baseline_file):
    with open(baseline_file, "w") as file:
        json.dump(file_hashes, file, indent=4)


def load_baseline(baseline_file):
    with open(baseline_file, "r") as file:
        return json.load(file)


def compare_files(old_files, new_files):
    added = []
    modified = []
    deleted = []

    for filename in new_files:
        if filename not in old_files:
            added.append(filename)

        elif old_files[filename] != new_files[filename]:
            modified.append(filename)

    for filename in old_files:
        if filename not in new_files:
            deleted.append(filename)

    return added, modified, deleted
