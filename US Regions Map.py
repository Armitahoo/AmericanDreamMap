import geopandas as gpd
import folium
from folium import GeoJson
from folium.features import GeoJsonTooltip
from folium import Html

# Load U.S. states shapefile from a reliable source
us_states = gpd.read_file('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json')

# Define U.S. regions with their respective states
us_region_groups = {
    'Northeast': ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'New Jersey', 'Pennsylvania'],
    'Midwest': ['Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin', 'Minnesota', 'Iowa', 'Missouri', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas'],
    'South': ['Delaware', 'Maryland', 'Virginia', 'West Virginia', 'Kentucky', 'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Alabama', 'Mississippi', 'Tennessee', 'Arkansas', 'Louisiana', 'Texas', 'Oklahoma'],
    'West': ['Montana', 'Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Utah', 'Nevada', 'Washington', 'Oregon', 'California', 'Alaska', 'Hawaii']
}

# Function to assign each state to its region
def get_us_region(state_name):
    for region, states in us_region_groups.items():
        if state_name in states:
            return region
    return None

# Add the 'region' column to the GeoDataFrame
us_states['region'] = us_states['name'].apply(get_us_region)

# Create a folium map centered on the U.S.
m_us = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Define hyperlinks for each U.S. region
us_region_links = {
    'Northeast': 'https://example.com/northeast',
    'Midwest': 'https://example.com/midwest',
    'South': 'https://example.com/south',
    'West': 'https://example.com/west'
}

# Function to create popups with clickable hyperlinks using Html
def us_popup_html(region):
    if region in us_region_links:
        html = f'<a href="{us_region_links[region]}" target="_blank">{region}</a>'
        return folium.Popup(folium.Html(html, script=True), max_width=300)
    return folium.Popup('No link available')

# Define colors for each U.S. region
us_region_colors = {
    'Northeast': '#f94144',
    'Midwest': '#f8961e',
    'South': '#f3722c',
    'West': '#90be6d'
}

# Add GeoJson layers for each region with coloring and popups
for region, data in us_states.groupby('region'):
    geojson = GeoJson(data,
                      style_function=lambda feature, region=region: {
                          'fillColor': us_region_colors.get(region, '#adb5bd'),  # Region-specific color
                          'color': 'black',       # Black border for the region
                          'weight': 2,            # Region border thickness
                          'fillOpacity': 0.5      # Opacity of the region fill
                      },
                      highlight_function=lambda feature: {
                          'fillColor': '#ffcccb',  # Highlight color when hovering over
                          'color': 'black',
                          'weight': 3,
                          'fillOpacity': 0.7
                      },
                      tooltip=GeoJsonTooltip(fields=['region']),  # Tooltip shows the region name
                      popup=us_popup_html(region))  # Add popup with clickable link
    geojson.add_to(m_us)

# Save the U.S. region map
m_us.save("us_regions_map.html")

# Display the U.S. map in a Jupyter notebook if needed:
# from IPython.display import display
# display(m_us)
