---
title: "Exploring the Representation of Islamic World Heritage Sites"
Link to the project: https://colab.research.google.com/drive/1OtxyA58I0ER2R7BHdR8j6yZwyesD0-3T
categories:
  - project1
---

Exploring the Representation of Islamic World Heritage Sites

<!--more-->

Research Question

1.	How many UNESCO World Heritage sites are Islamic and how this changes over time?
2.	Is the proportions of Islamic sites relative to all sites awarded in a given year?



What We Did

To answer this question, we used Python in Google Colab and followed these steps:

*	Import the data:
We downloaded site descriptions from a GitHub repository.

*	Search for Islamic sites:
We identified files containing keywords like "mosque", "muslim", or "islam". Each file represents a site, so if a keyword appeared, it counted as an Islamic site.

* Calculate yearly percentages:
For each year, we computed the proportion of Islamic sites relative to all sites awarded that year.

* Aggregate over 5-year periods:
To smooth out fluctuations and get a clearer view of trends, we grouped the data into 5-year periods and calculated the average percentage of Islamic sites in each period.

* Visualize the results:
We created bar charts showing the percentage of Islamic sites per 5-year period, highlighting periods with more or fewer Islamic sites relative to total sites.


![Manuscript Cover Page]({{site.baseurl}}images/Image1.jpeg

Interpreting the Results

The 5-year aggregated data shows that the recognition of Islamic sites varies over time. Some periods have higher percentages, indicating greater attention to Islamic heritage, while other periods show lower percentages, reflecting fewer sites designated relative to other cultural heritage. Aggregating over five years smooths out single-year fluctuations, allowing us to see longer-term trends more clearly. Overall, the data suggests that Islamic sites, while consistently part of World Heritage designations, represent a smaller fraction compared to other cultural sites, highlighting patterns of cultural recognition over time.



