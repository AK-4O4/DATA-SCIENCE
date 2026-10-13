import pandas as pd
import matplotlib.pyplot as plt

raw = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"],
}
df = pd.DataFrame(raw)

# (a)
df["Name"] = df["Name"].str.strip().str.title()

# (b)
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean().round(2))

# (c)
print(df)

# (d)
plt.figure(figsize=(7, 4))
plt.bar(df["Name"], df["Marks"], color="#4C78A8")
plt.title("Marks per Student")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()
print("Saved marks_bar.png")