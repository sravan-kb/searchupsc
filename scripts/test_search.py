import pandas as pd

# Load CSV
df = pd.read_csv(r"D:\Projects_CDAC\2025_questions.csv")

# Search keyword
keyword = "Delhi"

# Search rows containing keyword
results = df[
    df["full_text"].str.contains(
        keyword,
        case=False,
        na=False
    )
]

# Show results
print(results[["question_number", "full_text"]])