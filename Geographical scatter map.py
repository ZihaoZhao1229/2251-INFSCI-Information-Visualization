import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)

# Step 2: Map state names to coordinates
state_coords = {
    "AL": (32.806671, -86.791130), "AK": (61.370716, -152.404419), "AZ": (33.729759, -111.431221),
    "AR": (34.969704, -92.373123), "CA": (36.116203, -119.681564), "CO": (39.059811, -105.311104),
    "CT": (41.597782, -72.755371), "DE": (39.318523, -75.507141), "FL": (27.766279, -81.686783),
    "GA": (33.040619, -83.643074), "HI": (21.094318, -157.498337), "ID": (44.240459, -114.478828),
    "IL": (40.349457, -88.986137), "IN": (39.849426, -86.258278), "IA": (42.011539, -93.210526),
    "KS": (38.526600, -96.726486), "KY": (37.668140, -84.670067), "LA": (31.169546, -91.867805),
    "ME": (44.693947, -69.381927), "MD": (39.063946, -76.802101), "MA": (42.230171, -71.530106),
    "MI": (43.326618, -84.536095), "MN": (45.694454, -93.900192), "MS": (32.741646, -89.678696),
    "MO": (38.456085, -92.288368), "MT": (46.921925, -110.454353), "NE": (41.125370, -98.268082),
    "NV": (38.313515, -117.055374), "NH": (43.452492, -71.563896), "NJ": (40.298904, -74.521011),
    "NM": (34.840515, -106.248482), "NY": (42.165726, -74.948051), "NC": (35.630066, -79.806419),
    "ND": (47.528912, -99.784012), "OH": (40.388783, -82.764915), "OK": (35.565342, -96.928917),
    "OR": (44.572021, -122.070938), "PA": (40.590752, -77.209755), "RI": (41.680893, -71.511780),
    "SC": (33.856892, -80.945007), "SD": (44.299782, -99.438828), "TN": (35.747845, -86.692345),
    "TX": (31.054487, -97.563461), "UT": (40.150032, -111.862434), "VT": (44.045876, -72.710686),
    "VA": (37.769337, -78.169968), "WA": (47.400902, -121.490494), "WV": (38.491226, -80.954456),
    "WI": (44.268543, -89.616508), "WY": (42.755966, -107.302490),
}

data['Coordinates'] = data['State'].map(state_coords)

# Split latitude and longitude
data[['latitude', 'longitude']] = pd.DataFrame(data['Coordinates'].tolist(), index=data.index)

# Step 3: Aggregate data by state
state_data = data.groupby('State').agg({'TONE_Score': 'mean', 'latitude': 'first', 'longitude': 'first'}).reset_index()

# Step 4: Create a scatter plot
plt.figure(figsize=(14, 10))
scatter = plt.scatter(
    state_data['longitude'],
    state_data['latitude'],
    c=state_data['TONE_Score'],
    cmap='coolwarm',
    s=300,  # Increased size of points
    edgecolor='k',
    alpha=0.9  # Reduced transparency
)

# Add colorbar and labels
plt.colorbar(scatter, label='Average Tone Score')
plt.title('Average Tone Score by State (Enhanced Density)', fontsize=18)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)  # Optional: Add a grid
plt.tight_layout()
plt.show()