---
title:  "Tajik Migrant"
permalink: /tajikmigrant/
layout: page
image: images/projects_banner.png
--- 

<!--more-->

Mini Project 2 offered an opportunity to move beyond theoretical discussions and engage directly with digital methods for research and visualisation. The aim of the project was not only to answer a research question, but also to learn how complex data can be transformed, structured, and visualised in ways that make patterns visible and interpretable. Throughout the project, particular emphasis was placed on methodological choices, data preparation, and reflecting on the challenges encountered during the research process.


When we were asked to choose a research question for Mini Project 2, I initially thought it would be one of the easiest parts of the project—but it turned out not to be. At first, I had chosen a very general question, but after receiving feedback from the instructor, I refined it to make it as specific as possible, ensuring it would fit the scope of this mini project. In the end, I succeeded in formulating a clear and well-defined research question. 

As my final thesis focuses on migration from Tajikistan to Russia, in this Mini Project 2, I chose a topic that I plan to develop further for my thesis proposal. The focus of this project is the spatial distribution of Tajik migrants across Russian regions, based on official migration statistics. The main research question is: Which regions attract higher numbers of Tajik migrants, and what are the primary purposes of their migration? This project aims not only to map of migration but also to gain better understanding of the human stories behind this movements such as where people go, and why the move. This research question is planned to be explored through visualizations, such as a choropleth map and a stacked bar chart. 


## Data Corpus

To answer my research question, I initially planned to collect qualitative data from articles and reports on Tajik migrants in Russia published by sources such as the BBC, the World Bank, UNDP, and Russian media outlets including Asia Plus and Lenta. These sources provided useful background information and contextual insights into Tajik migration to Russia. However, this approach proved to be complicated for several reasons. First, I was required to rely on a single, consistent data source in order to build a coherent and reliable corpus, and combining multiple sources made this difficult. Second, since my project focuses primarily on spatial patterns, it was challenging to extract and standardize place-based information from articles and URLs. Many references included places such as Tajikistan or Dushanbe, which could be mistakenly interpreted as destination regions rather than places of origin, making the data unsuitable for clear spatial analysis.

Following feedback from my instructor, I identified a more appropriate and reliable data source: the provisional results of the 2021 Russian Census published by the Federal State Statistics Service (Rosstat). I downloaded an Excel file from Rosstat, specifically Table 8: “Population temporarily staying in the territory of the Russian Federation, by country of permanent residence and purpose of visit, by Russian regions.” While this dataset was highly relevant to my research question, it was also complex, as it combined multiple Russian regions, countries of origin, and migration purposes within a single file. Preparing this data for visualization required significant effort in cleaning, restructuring, and translating the table. Additionally, due to access restrictions, I was unable to open the Rosstat website using the Safari browser and instead used the Yandex browser to access and download the data.

[Regional Table](https://fakhufakh-sketch.github.io/portfolio/Project2/Corpus/ethinicity-purpose-province.xlsx)

## Step one 

The original table was highly complex, containing merged cells, repeated headers, and multiple sections within a single worksheet. It presented data on migrants from various countries arriving in Russia, categorized by region and purpose of visit. After several attempts, I successfully processed the dataset by working with ChatGPT and using Python (pandas). I parsed the CSV file, split the table by regions, filtered the data to include only Tajik migrants, cleaned the column headers, removed additional information that was not relevant to the analysis and produce a machine-readable CSV showing the total number of Tajik migrants per region. Later, I realized that my processed table did not include Tajik migrants in the Moscow region, even though the original dataset contained this information. This led me to reload the original Excel file and add Moscow to the table in order to ensure completeness and consistency with the original data.

## Step two

Initially, the data were in Russian because the original source was published in Russian. However, after receiving comments from the professor, I translated all Russian region names and migration purposes into English (Latin script). For this task, I used ChatGPT for translation and transliteration dictionary for the place name to create a consistent English-language version of the table. This step was necessary because the entire project is presented in English and intended for an English-speaking audience.

## Step three

To create the choropleth map, the migration data were aggregated at the regional level so that each administrative unit was represented by a single total value. This aggregation step was necessary because choropleth maps can display only one quantitative variable per spatial unit, and regional totals provide a clear overview of the spatial distribution of Tajik migrants across Russia.

After aggregation, the statistical table was matched with a Russian administrative GeoJSON file by aligning region names between the two datasets. GeoJSON is a JSON-based file format containing the administrative boundaries of Russian regions and was used as the spatial base layer for the map. As a widely adopted open standard for encoding geographic features in a machine-readable format, GeoJSON is particularly suitable for digital humanities projects that combine spatial data with quantitative analysis.

Care was taken to ensure consistent naming conventions across both datasets. During this process, several region names in the Tajik migration data did not initially match those used in the GeoJSON file and were therefore renamed to ensure consistency. Additionally, the Crimea region was removed from the table, as it could not be matched to a corresponding feature in the GeoJSON file.

By matching region names in the cleaned migration dataset with the corresponding region names in the GeoJSON file, it was possible to link statistical values to precise territorial units. This step ensured that each Russian region could be accurately represented on the map, including regions with no recorded Tajik migrants, which were assigned a value of zero.


## Step four 

Combining the aggregated migration data with a comprehensive GeoJSON file of Russian administrative regions made it possible to create a choropleth map of Russia. A choropleth map was chosen as the primary visualisation method because it is particularly well suited to representing aggregated quantitative data across administrative units. In this project, the number of Tajik migrants is aggregated at the level of Russian regions, making region-based colour encoding an effective way to reveal spatial variation.

By mapping migrant counts directly onto regional boundaries, the choropleth map enables immediate visual comparison between regions and highlights patterns of concentration and absence that are difficult to identify in tabular form. The use of a sequential colour scale further supports interpretation by indicating relative differences in migrant presence, from regions with low or no recorded migration to those with higher concentrations.


![A _choropleth_map_ of_Russia]({{site.baseurl}}images/map_ch.jpeg)

[Choropleth](https://fakhufakh-sketch.github.io/portfolio/Project2/Visualizations/Choropleth_map_Final.html)


## Step five

To explore the composition of migration purposes across regions, a stacked bar chart was used as a complementary visualisation to the choropleth map. While the map provides an overview of the spatial distribution of Tajik migrants across Russia, the stacked bar chart enables a more detailed examination of how different migration purposes contribute to regional totals.

For the bar chart, the dataset used for the choropleth map was further processed and adapted. Migration purposes were first grouped into a limited number of meaningful categories to improve readability. Purposes with higher migrant counts were retained as separate categories—namely work, study, private visits, and official or business trips—while all remaining purposes were aggregated into an “other” category. This step reduced visual complexity while preserving the main structure of the data.

Because Moscow city (g. Moskva) and Moscow oblast (Moskovskaja oblast’) record substantially higher numbers of Tajik migrants than other regions, including them in a single chart made comparisons between smaller regions difficult. To address this imbalance, two separate stacked bar charts were created: one focusing exclusively on Moscow city and Moscow oblast, and another displaying all remaining regions. This approach improves comparability and allows patterns in migration purposes across less dominant regions to be interpreted more clearly.Additionally, the colour scheme of the stacked bars was changed from a blue palette to a purple palette to improve visual clarity and make distinctions between categories easier to perceive, enhancing the overall readability of the chart.

![A _choropleth_map_ of_Russia]({{site.baseurl}}images/Barchart.jpeg)

[Stacked_Bar_Chart](https://fakhufakh-sketch.github.io/portfolio/Project2/Visualizations/SBarchart_Final_001.htmll)

The visualisations reveal clear spatial and functional patterns in Tajik migration across Russia. The choropleth map shows that Moscow city and Moscow oblast host the highest numbers of migrants, with other regions exhibiting much lower totals. This highlights the central role of the capital region in attracting Tajik migrants. The stacked bar charts further unpack these patterns by migration purpose: work-related migration dominates in most regions, followed by study and private visits, while official or business trips represent a smaller proportion. Aggregating minor purposes into an “other” category simplified the comparison between regions without losing meaningful information. Separating Moscow city and Moscow oblast into a dedicated chart also made it easier to observe patterns in smaller regions, where the relative importance of study and private visits is more visible. Overall, these visualisations demonstrate both the concentration of migration in the capital region and the diverse purposes driving Tajik migration throughout the country.


Finally, this mini project was both interesting and engaging, though it required a significant amount of time and effort to fully understand all the components. Since much of this was new to me, I spent extra time digesting the concepts and learning how to apply them. The work was challenging, but it provided a wealth of new knowledge, starting from the basics and progressing to more advanced skills, such as crafting effective prompts for ChatGPT, working with Python, and handling data with Pandas and JSON and Ploty. The instructor was extremely helpful throughout the process, providing continuous comments, feedback, and explanations that guided our improvement. Overall, the project was a valuable learning experience that helped me build practical skills while exploring an exciting digital humanities application. For future development, the project could be enhanced with more interactive visualizations, deeper exploration of migration purposes, or integration of temporal data to analyze trends over time. Overall, this project was a rewarding learning experience that strengthened both my technical abilities and my understanding of how to transform complex datasets into meaningful, interpretable insights.




