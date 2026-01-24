import pandas as pd
import plotly.express as px

# 1️⃣ Load the wide-purpose table (English)
wide_table = pd.read_csv("tajik_purpose_wide_en.csv", encoding="utf-8-sig")

# 2️⃣ Strip whitespace in region names
wide_table["Region_EN"] = wide_table["Region_EN"].str.strip()

# 3️⃣ Filter exactly both g. Moscow and Moskovskaja oblast'
regions_to_plot = ["g. Moskva"", "Moskovskaja oblast'"]
moscow_only = wide_table[wide_table["Region_EN"].isin(regions_to_plot)].copy()

# Check what is in the filtered DataFrame
print(moscow_only["Region_EN"])

# 4️⃣ Convert to long format for stacked bar chart
long_moscow = moscow_only.melt(
    id_vars=["Region_EN", "Total"],
    value_vars=["Work", "Study", "Private Visit", "Business Trip", "Other"],
    var_name="Purpose",
    value_name="Number_of_Migrants"
)

# Preserve order: Moskovskaja oblast' first, g. Moscow second
long_moscow["Region_EN"] = pd.Categorical(
    long_moscow["Region_EN"],
    categories=regions_to_plot,
    ordered=True
)

# 5️⃣ Purple palette (dark → slightly light)
purpose_colors = {
    "Work": "#6a51a3",         # dark purple
    "Study": "#9e9ac8",        # medium-dark
    "Private Visit": "#bcbddc",# medium-light
    "Business Trip": "#dadaeb",# light
    "Other": "#e6e0f0"         # slightly lighter
}

# -----------------------------
# Stacked Bar Chart: Only Moscow regions
# -----------------------------
fig_moscow = px.bar(
    long_moscow,
    x="Region_EN",
    y="Number_of_Migrants",
    color="Purpose",
    color_discrete_map=purpose_colors,
    category_orders={"Purpose": ["Work", "Study", "Private Visit", "Business Trip", "Other"]},
    labels={"Region_EN": "Region", "Number_of_Migrants": "Number of Migrants"},
    title="Tajik Migrants in g. Moscow and Moskovskaja oblast' by Purpose"
)

fig_moscow.update_layout(
    xaxis_tickangle=-45,
    barmode="stack",
    legend_title_text="Purpose",
    margin={"r":20,"t":50,"l":20,"b":100},
    height=500
)

# Show chart
fig_moscow.show()
