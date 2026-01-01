import os

# -----------------------------
# CONFIGURATION
# -----------------------------
project_path = "."  # Pfad zu deinem Projekt, "." = aktueller Ordner
file_extensions = [".html", ".css", ".js", ".py"]  # Dateitypen, die gezählt werden sollen

# -----------------------------
# LINE COUNT FUNCTION
# -----------------------------
def count_lines(path, extensions):
    total_lines = 0
    file_counts = {}

    for root, dirs, files in os.walk(path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    line_count = len(lines)
                    total_lines += line_count
                    file_counts[file_path] = line_count

    return total_lines, file_counts

# -----------------------------
# RUN
# -----------------------------
total, details = count_lines(project_path, file_extensions)

print(f"\nTotal lines in project: {total}\n")
print("Lines per file:")
for file_path, lines in details.items():
    print(f"{file_path}: {lines} lines")
