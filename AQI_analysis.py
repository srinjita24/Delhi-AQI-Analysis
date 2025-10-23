# AQI Analysis in Delhi - Auto Display + Save Version

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

url = "https://drive.google.com/uc?id=1DqkaLn2MDOZwXKoZgqaPdpSWE4sMJOSu&export=download"
df = pd.read_csv(url)

print("\n Dataset loaded successfully!\n")
print(df.head())
print(df.info())


print("\n Cleaning data...")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Fill missing values with mean
df.fillna(df.mean(), inplace=True)

print("Data cleaned successfully!")


print("\n Generating correlation heatmap...")

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation of Pollutants in Delhi AQI Data")

# Save and show
plt.savefig("correlation_heatmap.png")
plt.show(block=True)
print(" Saved: correlation_heatmap.png")


print("\n Performing seasonal AQI analysis...")

df['Month'] = df['date'].dt.month
df['Season'] = df['Month'].apply(lambda x: 
    'Winter' if x in [12,1,2] else 
    'Summer' if x in [3,4,5] else 
    'Monsoon' if x in [6,7,8,9] else 
    'Autumn'
)

# Average PM2.5 by season
season_pm25 = df.groupby('Season')['pm2_5'].mean().sort_values()

plt.figure(figsize=(8,5))
season_pm25.plot(kind='bar', color='orange')
plt.ylabel("Average PM2.5 Concentration")
plt.title("Seasonal Variation of PM2.5 in Delhi")
plt.savefig("seasonal_pm25_bar.png")
plt.show(block=True)
print(" Saved: seasonal_pm25_bar.png")


print("\n Plotting pollutant trends over time...")

pollutants = ['co','no','no2','o3','so2','pm2_5','pm10','nh3']

plt.figure(figsize=(12,6))
for pollutant in pollutants:
    if pollutant in df.columns:
        plt.plot(df['date'], df[pollutant], label=pollutant)

plt.xlabel("Date")
plt.ylabel("Pollutant Concentration")
plt.title("Pollutant Levels Over Time in Delhi")
plt.legend()
plt.tight_layout()
plt.savefig("pollutant_trends.png")
plt.show(block=True)
print(" Saved: pollutant_trends.png")


print("\n Identifying hazardous pollution days...")

hazardous_days = df[df['pm2_5'] > 250]
print(f"Number of very high PM2.5 days: {len(hazardous_days)}")

cols_to_save = ['date','pm2_5','pm10','no2','co']
hazardous_days[cols_to_save].to_csv("hazardous_days.csv", index=False)
print(" Saved: hazardous_days.csv")


print("\n Analysis Complete! All graphs displayed and saved.")
print("Check your folder for:")
print("   - correlation_heatmap.png")
print("   - seasonal_pm25_bar.png")
print("   - pollutant_trends.png")
print("   - hazardous_days.csv")

