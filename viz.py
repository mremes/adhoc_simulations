import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('viz.csv')

# Extract the distance column
distances = df['distance']

# Plot a histogram of the distances
plt.figure(figsize=(10, 6))
plt.hist(distances, bins=100, color='blue', edgecolor='black')

# Add title and labels to the histogram
plt.title('Histogram of Distances Between Points')
plt.xlabel('Distance')
plt.ylabel('Frequency')

# Show the plot
plt.show()

