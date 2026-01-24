import pandas as pd
import plotly.express as px

# 1️⃣ Load the wide-purpose table (English)
wide_table = pd.read_csv("tajik_purpose_wide_en.csv", encoding="utf-8-sig")

# 2️⃣ Filter out regions with very low total migrants
threshold = 50
wide_table = wide_table[wide_table["Total"] >= threshold]

# 3️⃣ Sort regions by Total (highest → lowest)
wide_table = wide_table.sort_values(by="Total", ascending=False)

# 4️⃣ Convert wide table to long format for stacked bar chart
long_table = wide_table.melt(
    id_vars=["Region_EN", "Total"],
    value_vars=["Work", "Study", "Private Visit", "Business Trip", "Other"],
    var_name="Purpose",
    value_name="Number_of_Migrants"
)

# 5️⃣ Preserve sorted order for x-axis
long_table["Region_EN"] = pd.Categorical(
    long_table["Region_EN"], 
    categories=wide_table["Region_EN"], 
    ordered=True
)

# 6️⃣ Define purple palette (dark → slightly light)
purpose_colors = {
    "Work": "#6a51a3",         # dark purple
    "Study": "#9e9ac8",        # medium-dark
    "Private Visit": "#bcbddc",# medium-light
    "Business Trip": "#dadaeb",# light
    "Other": "#e6e0f0"         # slightly lighter than Business Trip
}

# 7️⃣ Plot stacked bar chart
fig = px.bar(
    long_table,
    x="Region_EN",
    y="Number_of_Migrants",
    color="Purpose",
    color_discrete_map=purpose_colors,
    category_orders={"Purpose": ["Work", "Study", "Private Visit", "Business Trip", "Other"]},
    labels={"Region_EN": "Region", "Number_of_Migrants": "Number of Migrants"},
    title="Tajik Migrants in Russia by Purpose (regions with ≥50 migrants)"
)

# 8️⃣ Layout adjustments
fig.update_layout(
    xaxis_tickangle=-45,
    barmode="stack",
    legend_title_text="Purpose",
    margin={"r":20,"t":50,"l":20,"b":150},
    height=700
)

fig.show()
