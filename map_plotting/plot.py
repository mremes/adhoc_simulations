import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.geodesic import Geodesic

# Top 20 Finnish cities by population and their approximate coordinates
finnish_cities = [
    ("Helsinki", 60.1699, 24.9384),
    ("Espoo", 60.2055, 24.6559),
    ("Tampere", 61.4991, 23.7871),
    ("Vantaa", 60.2934, 25.0378),
    ("Oulu", 65.0126, 25.4715),
    ("Turku", 60.4518, 22.2666),
    ("Jyväskylä", 62.2426, 25.7473),
    ("Lahti", 60.9827, 25.6612),
    ("Kuopio", 62.8924, 27.6770),
    ("Pori", 61.4847, 21.7972),
    ("Kouvola", 60.8699, 26.7042),
    ("Joensuu", 62.6012, 29.7636),
    ("Lappeenranta", 61.0587, 28.1887),
    ("Hämeenlinna", 60.9959, 24.4643),
    ("Vaasa", 63.0960, 21.6158),
    ("Seinäjoki", 62.7903, 22.8403),
    ("Rovaniemi", 66.5039, 25.7294),
    ("Mikkeli", 61.6886, 27.2723),
    ("Kotka", 60.4666, 26.9458),
    ("Salo", 60.3833, 23.1333),
]

# Create a new map using Cartopy
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.EuroPP())

# Set extent for Northern Europe to zoom in on Finland
ax.set_extent([19, 32, 59, 70], crs=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.LAKES)

# Draw a circle of 150km radius around Helsinki using the Geodesic
geodetic = Geodesic()
circle_points = geodetic.circle(lon=finnish_cities[0][2], lat=finnish_cities[0][1], radius=150000, n_samples=100)

# Plot the circle on the map
ax.plot([point[0] for point in circle_points],
        [point[1] for point in circle_points],
        color='blue', linewidth=2, transform=ccrs.Geodetic())

# Annotate the map with city names
for city_name, lat, lon in finnish_cities:
    ax.plot(lon, lat, marker='o', color='red', markersize=5, transform=ccrs.Geodetic())
    ax.text(lon + 0.1, lat - 0.1, city_name, fontsize=9, transform=ccrs.Geodetic())

# Add gridlines
ax.gridlines(draw_labels=True, dms=False, x_inline=False, y_inline=False)

# Show the plot
plt.show()
