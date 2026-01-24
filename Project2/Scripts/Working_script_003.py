import pandas as pd

# -----------------------------
# 1️⃣ Load the CSV with Russian and English region names
# -----------------------------
df = pd.read_csv("tajik_ethnicity_in_Russia_EN_Latin_v2.csv", encoding="utf-8-sig", keep_default_na=False)

# -----------------------------
# 2️⃣ Forward-fill Russian region names for Tajikistan rows
# -----------------------------
df['Region_Fill'] = df['Region'].where(df['Region'] != "Таджикистан").ffill()

# -----------------------------
# 3️⃣ Forward-fill English names for Tajikistan rows
# -----------------------------
df['Region_EN_Fill'] = df['Region_EN'].where(df['Region'] != "Таджикистан").ffill()

# -----------------------------
# 4️⃣ Keep only Tajikistan rows
# -----------------------------
df_tajik = df[df['Region'] == "Таджикистан"].copy()

# -----------------------------
# 5️⃣ Identify numeric columns (exclude region columns)
# -----------------------------
non_numeric_cols = ['Region', 'Region_EN', 'Region_Fill', 'Region_EN_Fill']
numeric_cols = [col for col in df_tajik.columns if col not in non_numeric_cols]

# Convert numeric columns safely
for col in numeric_cols:
    df_tajik[col] = pd.to_numeric(df_tajik[col], errors='coerce').fillna(0)

# -----------------------------
# 6️⃣ Aggregate by parent region
# -----------------------------
agg_df = df_tajik.groupby(['Region_Fill', 'Region_EN_Fill'])[numeric_cols].sum().reset_index()
agg_df.rename(columns={'Region_Fill':'Region', 'Region_EN_Fill':'Region_EN'}, inplace=True)

# -----------------------------
# 7️⃣ Save aggregated CSV
# -----------------------------
agg_df.to_csv("taji12k_aggregated_for_map.csv", index=False, encoding="utf-8-sig")

print("Aggregation complete ✅ CSV saved as 'tajik_aggregated_for_map.csv'")
