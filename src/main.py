from hash_utils import calculate_file_hash

file_path = "tests/sample.txt"

file_hash = calculate_file_hash(file_path)

print("File Integrity Monitor")
print("---------------------")
print("File:", file_path)
print("SHA-256:", file_hash)
