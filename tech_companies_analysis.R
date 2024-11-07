
# Load necessary libraries
library(tidyverse)
library(readr)
library(ggplot2)

# Load the tech companies dataset
tech_companies_data <- read_csv('path_to_cleaned_tech_companies_data.csv')

# Summary statistics
summary(tech_companies_data)

# Distribution of Market Cap
ggplot(tech_companies_data, aes(x = Market_Cap)) +
    geom_histogram(bins = 30, fill = 'blue', color = 'black', alpha = 0.7) +
    labs(title = 'Distribution of Market Cap', x = 'Market Cap (in $)', y = 'Frequency') +
    theme_minimal()

# Market Cap by Country
country_market_cap <- tech_companies_data %>%
    group_by(Country) %>%
    summarise(Total_Market_Cap = sum(Market_Cap)) %>%
    arrange(desc(Total_Market_Cap)) %>%
    head(20)

ggplot(country_market_cap, aes(x = Total_Market_Cap, y = reorder(Country, Total_Market_Cap))) +
    geom_bar(stat = 'identity', fill = 'darkred') +
    labs(title = 'Top 20 Countries by Total Market Cap', x = 'Total Market Cap (in $)', y = 'Country') +
    theme_minimal()
