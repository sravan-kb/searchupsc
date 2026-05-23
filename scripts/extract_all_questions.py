import os
import re
import pandas as pd

# Folder containing cleaned TXT files
input_folder = r"D:\Projects_CDAC\2025UPSC_CLEANED"

# Store all extracted questions
all_questions = []

# Regex pattern for question numbers
pattern = r"\n(\d+)\."

# Process all TXT files
for filename in os.listdir(input_folder):

    # Process only TXT files
    if filename.endswith(".txt"):

        # Full file path
        file_path = os.path.join(input_folder, filename)

        print(f"Processing: {filename}")

        # Read TXT file
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Split using question numbers
        parts = re.split(pattern, text)

        # Extract questions
        for i in range(1, len(parts), 2):

            question_number = parts[i]

            full_text = parts[i + 1].strip()

            # Store question block
            all_questions.append({
                "year": 2025,
                "source_file": filename,
                "question_number": question_number,
                "full_text": full_text
            })

# Create DataFrame
df = pd.DataFrame(all_questions)

# Save CSV
output_csv = r"D:\Projects_CDAC\2025_questions.csv"

df.to_csv(
    output_csv,
    index=False,
    encoding="utf-8"
)

print(df.head())

print(f"\nCSV saved successfully:\n{output_csv}")