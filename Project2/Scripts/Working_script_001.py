import pandas as pd

# Load Excel
df = pd.read_excel("ethinicity-purpose-province.xlsx", skiprows=3)

# Fix merged cells + clean text
df.iloc[:, 0] = df.iloc[:, 0].ffill().astype(str).str.strip()

filtered_rows = []

def is_russian_region(text):
    t = text.lower()
    return (
        "федеральный округ" in t
        or "область" in t
        or "край" in t
        or "автономный округ" in t
        or text in [
            "г. Москва",  # <-- Added Moscow
            "Республика Башкортостан", "Республика Марий Эл", "Республика Мордовия",
            "Республика Татарстан", "Удмуртская Республика", "Чувашская Республика",
            "Республика Алтай", "Республика Тыва", "Республика Хакасия",
            "Республика Карелия", "Республика Коми", "Республика Адыгея",
            "Республика Калмыкия", "Республика Крым", "Республика Дагестан",
            "Республика Ингушетия", "Кабардино-Балкарская Республика",
            "Карачаево-Черкесская Республика", "Республика Северная Осетия - Алания",
            "Чеченская Республика", "Марий Эл"
        ]
    )


# Filtering
for i in range(len(df)):
    value = df.iloc[i, 0]

    # Keep summary rows
    if value in ["Всего", "Указавшие цель приезда"]:
        filtered_rows.append(df.iloc[i])
        continue

    # Keep Russian regions
    if is_russian_region(value):
        filtered_rows.append(df.iloc[i])

        # Look ONLY for Tajikistan below
        j = i + 1
        while j < len(df):
            next_val = df.iloc[j, 0]

            # Stop at next region or summary
            if is_russian_region(next_val) or next_val in ["Всего", "Указавшие цель приезда"]:
                break

            # Keep only Tajikistan
            if next_val == "Таджикистан":
                filtered_rows.append(df.iloc[j])
                break

            j += 1

# Build final DataFrame
filtered_df = pd.DataFrame(filtered_rows, columns=df.columns)

# -----------------------
# Rename Unnamed Columns
# -----------------------
new_columns = filtered_df.columns.tolist()

# Set first three columns
if len(new_columns) >= 3:
    new_columns[0] = "Регион"
    new_columns[1] = "Всего"
    new_columns[2] = "Указавшие цель приезда"

# Set last column
new_columns[-1] = "Не указавшие цель приезда"

# Apply the new column names
filtered_df.columns = new_columns

# Save CSV
filtered_df.to_csv("tajik_ethnicity_in_Russia.csv", index=False, encoding="utf-8-sig")

print("DONE")
