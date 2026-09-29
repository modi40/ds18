import pandas as pd
import matplotlib.pyplot as plt
import squarify

df = pd.read_csv('worldcities.csv')

print("World Cities Dataset Preview:")
print(df.head())

plt.figure(figsize=(12, 6))
plt.scatter(df['longitude'], df['latitude'], s=df['population']/500000, c='coral', alpha=0.7, edgecolors='black')
for i, txt in enumerate(df['city']):
    plt.annotate(txt, (df['longitude'][i] + 1, df['latitude'][i]))
plt.title("Geospatial Visualization of World Cities")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
labels = [f"{city}\n{pop//1000000}M" for city, pop in zip(df['city'], df['population'])]
squarify.plot(sizes=df['population'], label=labels, alpha=0.8)
plt.title("Treemap of World Cities Population Distribution")
plt.axis('off')
plt.tight_layout()
plt.show()
