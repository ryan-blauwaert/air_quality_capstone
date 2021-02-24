# Title
### Ryan Blauwaert

## Background
* State the practical application of this analysis
* Describe the difficulty of measuring the effects of air pollution
* Pinpoint health outcomes as focus of analysis
* Describe the rationale behind using infant mortality and child asthma hospitalization rates as a proxy for the health effects on the general population

## The Data
* Air pollutant data
    - comes from the EPA
    - give number of metrics in data; describe as annual averages adjusted for seasonal fluctuation
    - across n cities over 20 years
    - describe the metrics which will be the primary focus of the study; give units
* Infant mortality data
    - stress that this is a rate per 1000 births to adjust for differences in location populations
    
* NYC asthma hospitalizations
    - again, this is a rate, this time per 10,000
    - data only available for New York City
    - will test for statistical significance to see if the conclusion about nyc are safe to extend nationally (?)

## Questions
* Is there a statistically significant correlation between air quality and infant mortality?
* Is there a statistically significant correlation between air quality and asthma hospitalizations
* Which, if any, air pollutants are most positively correlated with health outcomes
* Can any conclusions be extended to the health outcomes of the general population?

## Cleaning the Data
* Describe goals of cleaning:
    - address null values
    - narrow scope of study to only major US cities
* Challenges in cleaning data:
    - Data coming from three unrelated sources, therefore data is in particularly disparate formats
    - standardize location names to act as indices
    - infant mortality data contained a gap; no data in 2007, 2008. Describe how this was addressed
    - describe transposition of data from one source to match the format of the others

## EDA 
* Look for outliers??
* Show line graphs with all metrics included
    - describe need to narrow focus to a few metrics only
* correlation matrix of pollutants vs pollutants (use means?)

## Visualizations
![National Air Pollution and Infant Mortality](./images/inner_quartile.png)

* National data inner quartile range
    - highlight negatively sloped trendline across all featured metrics as well as infant mortality
    - 