import pandas as pd
import plotly.express as px

# 1️⃣ Load the wide-purpose table (English)
wide_table = pd.read_csv("tajik_purpose_wide_en.csv", encoding="utf-8-sig")

# 2️⃣ Strip whitespace in region names
wide_table["Region_EN"] = wide_table["Region_EN"].str.strip()

# 3️⃣ Exclude g. Moscow and Moskovskaja oblast'
regions_to_exclude = ["g. Moskva", "Moskovskaja oblast'"]
rest_regions = wide_table[~wide_table["Region_EN"].isin(regions_to_exclude)].copy()

# 4️⃣ Optional: Sort by total number of migrants descending
rest_regions = rest_regions.sort_values(by="Total", ascending=False)

# 5️⃣ Convert to long format for stacked bar chart
long_rest = rest_regions.melt(
    id_vars=["Region_EN", "Total"],
    value_vars=["Work", "Study", "Private Visit", "Business Trip", "Other"],
    var_name="Purpose",
    value_name="Number_of_Migrants"
)

# 6️⃣ Purple palette (dark → slightly light)
purpose_colors = {
    "Work": "#6a51a3",         # dark purple
    "Study": "#9e9ac8",        # medium-dark
    "Private Visit": "#bcbddc",# medium-light
    "Business Trip": "#dadaeb",# light
    "Other": "#e6e0f0"         # slightly lighter
}

# -----------------------------
# Stacked Bar Chart: All regions except Moscow
# -----------------------------
fig_rest = px.bar(
    long_rest,
    x="Region_EN",
    y="Number_of_Migrants",
    color="Purpose",
    color_discrete_map=purpose_colors,
    category_orders={"Purpose": ["Work", "Study", "Private Visit", "Business Trip", "Other"]},
    labels={"Region_EN": "Region", "Number_of_Migrants": "Number of Migrants"},
    title="Tajik Migrants in Russian Regions by Purpose (excluding g. Moscow and Moskovskaja oblast')"
)

fig_rest.update_layout(
    xaxis_tickangle=-45,
    barmode="stack",
    legend_title_text="Purpose",
    margin={"r":20,"t":50,"l":20,"b":200},  # increased bottom margin for long region names
    height=700
)

# Show chart
fig_rest.show()
