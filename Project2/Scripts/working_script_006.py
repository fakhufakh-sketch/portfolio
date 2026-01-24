import pandas as pd

# 1️⃣ Load your CSV
df = pd.read_csv("tajik_aggregated_for_choropleth.csv", encoding="utf-8-sig")

# 2️⃣ Define main purposes and minor purposes
main_purposes = ["Work", "Study", "Private Visit", "Business Trip"]
minor_purposes = ["Tourism/Leisure", "Transit", "Other Purpose"]

# 3️⃣ Ensure numeric values
for col in main_purposes + minor_purposes:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    else:
        df[col] = 0  # safety if missing

# 4️⃣ Sum minor purposes into "Other"
df["Other"] = df[minor_purposes].sum(axis=1)

# 5️⃣ Create wide table with only English columns
wide_table_en = df[["Region_EN", "Total"] + main_purposes + ["Other"]].copy()

# 6️⃣ Optional: preview
print(wide_table_en.head(10))

# 7️⃣ Save table
wide_table_en.to_csv("tajik_purpose_wide_en.csv", index=False, encoding="utf-8-sig")

print("✅ Wide table in English saved as 'tajik_purpose_wide_en.csv'")


