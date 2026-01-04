---
title: "Spatial distribution of Tajik migrants across Russian regions"
excerpt_separator: "<!--more-->"
categories:
  - project1
tags:
  - Projects
  - Machine Learning
  - Mini Project 2
image: images/map-rs.jpeg 
---

This mini-project explores the spatial distribution of Tajik migrants across Russian regions using official migration statistics and analyzes migration purposes to identify which regions attract higher numbers of Tajik migrants and for what primary purposes.

<!--more-->

## Data Corpus

The original dataset was a complex Excel table from the Federal State Statistics Service (Rosstat), combining multiple regions, countries of origin, and migration purposes (Table 8. Population temporarily staying in the territory of the Russian Federation, by country of permanent residence and purpose of visit, by Russian regions,  link).

## Step one 

So far, I have focused on data cleaning and structuring, which was the most time-consuming part due to merged cells, repeated headers, and multiple sections within a single sheet. Using Python (pandas), I parsed the Excel file, programmatically split the table by regions, filtered for Tajik migrants, cleaned column headers, and aggregated the data to produce a machine-readable CSV showing the total number of migrants per region. 

## Step two

To visualise migration data geographically, a GeoJSON file containing the administrative boundaries of Russian regions was used as the spatial base layer. GeoJSON is a widely adopted open standard for encoding geographic features in a machine-readable format, making it particularly suitable for digital humanities projects that combine spatial data with quantitative analysis. By matching region names in the cleaned migration dataset with the corresponding region names in the GeoJSON file, it was possible to link statistical values to precise territorial units. This step ensured that each Russian region could be accurately represented on the map, including regions with no recorded Tajik migrants, which were assigned a value of zero.

## Step three

Combining aggregated migration data with a comprehensive GeoJSON of Russian administrative regions allowed me to create a choropleth map of Russia. A choropleth map was chosen as the primary visualisation method because it is particularly well suited for representing aggregated quantitative data across administrative regions. In this project, the number of Tajik migrants is aggregated at the level of Russian regions, making a region-based colour encoding an effective way to reveal spatial variation. By mapping migrant counts directly onto regional boundaries, the choropleth map allows for immediate visual comparison between regions and highlights patterns of concentration and absence that are difficult to detect in tabular form. This approach supports spatial analysis by showing how Tajik migration is distributed across the entire territory of Russia while preserving the administrative context in which migration statistics are collected.

![A _choropleth_map_ of_Russia]({{site.baseurl}}images/my-map.jpeg)

## Step four 

For the next step, I plan to analyze the purposes of migration — work, study, private visits, and others — focusing on the top ten regions by total migrants. I will reshape the dataset and use Python and Plotly to create a stacked bar chart that shows the breakdown of purposes for each region. This will complement the choropleth map by moving from a descriptive spatial overview to a comparative analysis, helping to understand not just where Tajik migrants are, but why they choose these regions.

## List of Challenges

1) Working with a non-standard Excel table that contained merged cells, repeated headers, and multiple hierarchical levels, which required programmatic cleaning rather than manual correction.

2) Identifying and isolating Tajik migrants within a multi-country dataset while preserving their correct association with each Russian region.

3) Cleaning and standardising column names to make the dataset machine-readable and suitable for analysis.

4) Reconciling differences in regional naming conventions between the migration dataset and the GeoJSON file, including republic naming variants and administrative labels.

5) Ensuring that all Russian regions appear on the map, including those with zero recorded Tajik migrants, to avoid misleading visual gaps.

6) Choosing appropriate classification thresholds and colour schemes for the choropleth map to balance interpretability and visual accuracy.

## Anticipating challenges 

7) Visualising multiple migration purposes without overwhelming the reader in future stages of the project.






