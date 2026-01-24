import pandas as pd
import json

# -----------------------------
# 1️⃣ Load GeoJSON
# -----------------------------
with open("russia.geojson", "r", encoding="utf-8") as f:
    russia_geojson = json.load(f)

# -----------------------------
# 2️⃣ List all names containing 'Москва'
# -----------------------------
geo_names = [feature['properties']['name'] for feature in russia_geojson['features']]
moscow_in_geojson = [name for name in geo_names if "Москва" in name]
print("Moscow in GeoJSON:", moscow_in_geojson)

# -----------------------------
# 3️⃣ Load your CSV
# -----------------------------
map_df = pd.read_csv("tajik_aggregated_for_choropleth.csv", encoding="utf-8-sig")

# -----------------------------
# 4️⃣ Replace Moscow name in CSV if needed
# -----------------------------
if moscow_in_geojson:
    correct_name = moscow_in_geojson[0]  # take the first match
    map_df['Region'] = map_df['Region'].replace({"Москва": correct_name})
    print(f"Moscow in CSV updated to match GeoJSON: {correct_name}")
else:
    print("No Moscow polygon found in GeoJSON!")

# -----------------------------
# 5️⃣ Save updated CSV
# -----------------------------
map_df.to_csv("tajik_aggregated_for_choropleth_fixed.csv", index=False, encoding="utf-8-sig")
print("✅ CSV updated for Moscow name if needed")
