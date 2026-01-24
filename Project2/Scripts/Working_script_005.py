import pandas as pd
import json
import plotly.express as px

# 1️⃣ Load CSV and GeoJSON
map_df = pd.read_csv("tajik_aggregated_for_choropleth.csv", encoding="utf-8-sig")
map_df['Total'] = pd.to_numeric(map_df['Total'], errors='coerce').fillna(0)

with open("russia.geojson", "r", encoding="utf-8") as f:
    russia_geojson = json.load(f)

# 2️⃣ Merge with GeoJSON regions
geo_names = [feature['properties']['name'] for feature in russia_geojson['features']]
full_df = pd.DataFrame({'Region': geo_names})
full_df = full_df.merge(map_df, on='Region', how='left')
full_df['Total'] = full_df['Total'].fillna(0)

# 3️⃣ Define bins and colors manually
bins = [0, 50, 200, 500, 1000, 5000, 15000]
colors = ['#deebf7','#c6dbef','#9ecae1','#6baed6','#3182bd','#08519c']
labels = ['0-50','51-200','201-500','501-1000','1001-5000','5001+']

# Assign a color to each row based on Total
def assign_color(value):
    for i, upper in enumerate(bins[1:]):
        if value <= upper:
            return colors[i]
    return colors[-1]

full_df['color'] = full_df['Total'].apply(assign_color)

# Assign legend category based on bins
def assign_label(value):
    for i, upper in enumerate(bins[1:]):
        if value <= upper:
            return labels[i]
    return labels[-1]

full_df['category'] = full_df['Total'].apply(assign_label)
full_df['category'] = pd.Categorical(full_df['category'], categories=labels, ordered=True)  # Ordered legend

# 4️⃣ Create choropleth with proper legend order
fig = px.choropleth(
    full_df,
    geojson=russia_geojson,
    locations='Region',
    featureidkey='properties.name',
    color='category',
    color_discrete_map={lab: col for lab, col in zip(labels, colors)},
    category_orders={'category': labels},  # ✅ enforce proper legend order
    hover_name='Region_EN',  # Show English names
    hover_data={'Total': True, 'category': False},
    title='Tajik Migrants in Russia by Region'
)

# 5️⃣ Layout
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    margin={"r":0,"t":50,"l":0,"b":0},
    legend_title_text='Number of Tajik Migrants',
    legend_traceorder='normal'
)

# 6️⃣ Show map
fig.show()
