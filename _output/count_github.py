import pandas as pd
from pathlib import Path

# Define file paths based on your directory structure
files = [
    Path("/home/ubuntu/assignment-01-ChialingSung/data/question_tags.csv"),
    Path("/home/ubuntu/assignment-01-ChialingSung/data/questions.csv")
]

count = 0
chunk_size = 100000

# Process each file
for file in files:
    if not file.exists():
        print(f"Warning: File {file} not found, skipping...")
        continue

    print(f"Processing {file}...")

    try:
        for chunk in pd.read_csv(file, encoding='utf-8', on_bad_lines='skip', chunksize=chunk_size, low_memory=False, dtype=str):
            count += chunk.apply(lambda col: col.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()
    except Exception as e:
        print(f"Error processing {file}: {e}")
        continue

# Save the result to _output folder
output_path = Path("/home/ubuntu/assignment-01-ChialingSung/_output/github_count.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure _output directory exists
output_path.write_text(str(count) + "\n")

print(f"Total lines containing 'GitHub': {count}")

