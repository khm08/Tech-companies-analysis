
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = 'path_to_dataset/Top 1000 technology companies.csv'
tech_companies_data = pd.read_csv(file_path)

# Clean the 'Market Cap' column by removing special characters and converting to numerical values
tech_companies_data['Market Cap'] = tech_companies_data['Market Cap'].replace(
    {'\$': '', 'T': 'e12', 'B': 'e9', 'M': 'e6'}, regex=True
)
tech_companies_data['Market Cap'] = tech_companies_data['Market Cap'].str.replace(' ', '').astype(float)

# Sorting the data by 'Ranking'
sorted_tech_companies_data = tech_companies_data.sort_values(by='Ranking')

# Summary Statistics
summary_stats = sorted_tech_companies_data.describe()

# Distribution of Market Cap
plt.figure(figsize=(10, 6))
sns.histplot(sorted_tech_companies_data['Market Cap'], bins=30, kde=True)
plt.title('Distribution of Market Cap')
plt.xlabel('Market Cap (in $)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Market Cap by Country
plt.figure(figsize=(14, 7))
country_market_cap = sorted_tech_companies_data.groupby('Country')['Market Cap'].sum().sort_values(ascending=False).head(20)
sns.barplot(x=country_market_cap.values, y=country_market_cap.index, palette='coolwarm')
plt.title('Top 20 Countries by Total Market Cap')
plt.xlabel('Total Market Cap (in $)')
plt.ylabel('Country')
plt.grid(True)
plt.show()

# Market Cap by Sector
plt.figure(figsize=(14, 7))
sector_market_cap = sorted_tech_companies_data.groupby('Sector')['Market Cap'].sum().sort_values(ascending=False)
sns.barplot(x=sector_market_cap.values, y=sector_market_cap.index, palette='viridis')
plt.title('Market Cap by Sector')
plt.xlabel('Total Market Cap (in $)')
plt.ylabel('Sector')
plt.grid(True)
plt.show()

# Top 10 Companies by Market Cap
top_10_companies = sorted_tech_companies_data.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x='Market Cap', y='Company', data=top_10_companies, palette='magma')
plt.title('Top 10 Technology Companies by Market Capitalization')
plt.xlabel('Market Cap (in trillions)')
plt.ylabel('Company')
plt.grid(True)
plt.show()

# Sector distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='Sector', data=sorted_tech_companies_data, order = sorted_tech_companies_data['Sector'].value_counts().index, palette='cubehelix')
plt.title('Distribution of Companies by Sector')
plt.xlabel('Number of Companies')
plt.ylabel('Sector')
plt.grid(True)
plt.show()

# Industry distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='Industry', data=sorted_tech_companies_data, order = sorted_tech_companies_data['Industry'].value_counts().index[:15], palette='crest')
plt.title('Top 15 Industries by Number of Companies')
plt.xlabel('Number of Companies')
plt.ylabel('Industry')
plt.grid(True)
plt.show()

# Correlation matrix
correlation = sorted_tech_companies_data[['Ranking', 'Market Cap']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

# Saving the cleaned dataset for future use
cleaned_excel_path = 'cleaned_tech_companies_data.xlsx'
sorted_tech_companies_data.to_excel(cleaned_excel_path, index=False)
