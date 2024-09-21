import geopandas as gpd
import folium
from folium import GeoJson
from folium.features import GeoJsonTooltip
from folium import Html

# Load world geometries using GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Define custom regions and their respective countries
region_groups = {
    'North America': ['United States of America', 'Canada'],
    'Mexico and Central America': ['Mexico', 'Guatemala', 'Belize', 'El Salvador', 'Honduras', 'Nicaragua', 'Costa Rica', 'Panama'],
    'South America': ['Brazil', 'Argentina', 'Chile', 'Colombia', 'Peru', 'Venezuela', 'Ecuador', 'Bolivia', 'Paraguay', 'Uruguay', 'Guyana', 'Suriname'],
    'West Europe': ["Ireland", 'Iceland', 'Denmark', 'Norway', 'Sweden', 'Finland', 'France', 'Germany', 'Spain', 'Portugal', 'Netherlands', 'Belgium', 'Switzerland', 'Austria', 'Italy', 'United Kingdom'],
    'East Europe': ['Poland', 'Ukraine', 'Romania', 'Hungary', 'Czech Republic', 'Slovakia', 'Bulgaria', 'Serbia', 'Croatia', 'Bosnia and Herzegovina', 'Moldova', 'Turkey', 'Greece', 'Albania', 'North Macedonia', 'Kosovo', 'Montenegro', 'Bosnia and Herz.', 'Slovenia', 'Czechia', 'Belarus', 'Lithuania', 'Latvia', 'Estonia', 'Cyprus', 'N. Cyprus'],
    'Central Asia': ['Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Tajikistan', 'Kyrgyzstan'],
    'MENA': ['Saudi Arabia', 'Iran', 'Iraq', 'Jordan', 'Syria', 'Lebanon', 'Israel', 'Palestine', 'Kuwait', 'Bahrain', 'Qatar', 'United Arab Emirates', 'Oman', 'Yemen', 'Egypt', 'Libya', 'Algeria', 'Morocco', 'Tunisia', 'Sudan', 'W. Sahara', 'Mauritania', "S. Sudan", 'Somaliland'],
    'South Asia': ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Bhutan', 'Maldives', 'Afghanistan'],
    'East Asia': ['China', 'Japan', 'South Korea', 'Mongolia', 'North Korea'],
    'Southeast Asia': ['Indonesia', 'Thailand', 'Vietnam', 'Malaysia', 'Singapore', 'Philippines', 'Myanmar', 'Cambodia', 'Laos', 'Brunei', 'Timor-Leste'],
    'Oceania': ['Australia', 'New Zealand', 'Papua New Guinea', 'Fiji', 'Solomon Islands', 'Vanuatu', 'Samoa', 'Tonga'],
    'Southern Africa': ['Nigeria', 'Ghana', "Côte d'Ivoire", 'Senegal', 'Mali', 'Guinea', 'Sierra Leone', 'Liberia', 'Burkina Faso', 'Togo', 'Benin', 'Niger', 'Cape Verde', 'Gambia', 'Guinea-Bissau', 'Mauritania', 'South Africa', 'Namibia', 'Botswana', 'Zimbabwe', 'Zambia', 'Angola', 'Malawi', 'Mozambique', 'Lesotho', 'eSwatini', 'Kenya', 'Tanzania', 'Uganda', 'Ethiopia', 'Somalia', 'Rwanda', 'Burundi', 'Djibouti', 'Eritrea', 'South Sudan', 'Madagascar', 'Seychelles', 'Comoros', 'Mauritius', 'Dem. Rep. Congo', 'Congo', 'Cameroon', 'Gabon', 'Eq. Guinea', 'Central African Rep.', 'Chad'],
    'Caribbean': ['Cuba', 'Haiti', 'Dominican Rep.', 'Jamaica', 'Trinidad and Tobago', 'Barbados', 'Bahamas', 'Saint Lucia', 'Grenada', 'Saint Vincent and the Grenadines', 'Antigua and Barbuda', 'Saint Kitts and Nevis', 'Dominica']
}

# Assign regions to countries
def get_region(country):
    for region, countries in region_groups.items():
        if country in countries:
            return region
    return 'Other'

# Add region column to world dataframe
world['region'] = world['name'].apply(get_region)

# Define hyperlinks for each region
region_links = {
    'North America': 'https://example.com/north-america',
    'Mexico and Central America': 'https://example.com/mexico-central-america',
    'South America': 'https://example.com/south-america',
    'West Europe': 'https://example.com/west-europe',
    'East Europe': 'https://example.com/east-europe',
    'Central Asia': 'https://example.com/central-asia',
    'MENA': 'https://example.com/mena',
    'South Asia': 'https://example.com/south-asia',
    'East Asia': 'https://example.com/east-asia',
    'Southeast Asia': 'https://example.com/southeast-asia',
    'Oceania': 'https://example.com/oceania',
    'Southern Africa': 'https://example.com/southern-africa',
    'Caribbean': 'https://example.com/caribbean',
    'Other': 'https://example.com/other'
}

# Function to generate pop-up text with clickable hyperlink
def popup_text(region):
    link = region_links.get(region, 'https://example.com')
    return f'<a href="{link}" target="_blank">{region} Information</a>'

# Initialize a Folium map
m = folium.Map(location=[20, 0], zoom_start=2)

# Define a color map for the world regions
world_region_colors = {
    'North America': 'blue',
    'Mexico and Central America': 'green',
    'South America': 'red',
    'West Europe': 'purple',
    'East Europe': 'orange',
    'Central Asia': 'pink',
    'MENA': 'lightblue',
    'South Asia': 'cyan',
    'East Asia': 'magenta',
    'Southeast Asia': 'teal',
    'Oceania': 'lightgreen',
    'Southern Africa': 'brown',
    'Caribbean': 'darkblue',
    'Other': 'gray'
}

# Function to set the style for each world region
def world_style_function(feature):
    region = feature['properties']['region']
    return {
        'fillOpacity': 0.7,
        'weight': 1,
        'color': 'black',
        'fillColor': world_region_colors.get(region, 'gray')
    }

# Add a GeoJson layer for world regions to the map
folium.GeoJson(
    world,
    style_function=world_style_function,
    highlight_function=lambda feature: {
        'weight': 3,
        'color': 'blue',
        'fillOpacity': 0.9
    },
    tooltip=folium.GeoJsonTooltip(fields=['name', 'region'], aliases=['Country:', 'Region:']),
    popup=folium.GeoJsonPopup(fields=['region'], aliases=['Region:'], labels=True,
                              style="background-color: white;", localize=True,
                              sticky=False),
).add_to(m)

# Load U.S. states shapefile
us_states = gpd.read_file('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json')

# Define a color map for U.S. regions
us_region_colors = {
    'Northeast': 'yellow',
    'Midwest': 'darkgreen',
    'South': 'lightcoral',
    'West': 'darkorange'
}

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

# Add 'region' column to the U.S. states GeoDataFrame
us_states['region'] = us_states['name'].apply(get_us_region)

# Function to set style for U.S. states
def us_style_function(feature):
    region = feature['properties']['region']
    return {
        'fillOpacity': 0.5,
        'weight': 2,
        'color': 'black',
        'fillColor': us_region_colors.get(region, 'grey')  # Use color from U.S. regions
    }

# Function to create popups for U.S. regions
us_region_links = {
    'Northeast': 'https://example.com/northeast',
    'Midwest': 'https://example.com/midwest',
    'South': 'https://example.com/south',
    'West': 'https://example.com/west'
}

def us_popup_html(region):
    if region in us_region_links:
        html = f'<a href="{us_region_links[region]}" target="_blank">{region}</a>'
        return folium.Popup(folium.Html(html, script=True), max_width=300)
    return folium.Popup('No link available')

# Add U.S. GeoJson layer to the map
folium.GeoJson(
    us_states,
    style_function=us_style_function,
    highlight_function=lambda feature: {
        'fillColor': '#ffcccb',
        'color': 'black',
        'weight': 3,
        'fillOpacity': 0.7
    },
    tooltip=GeoJsonTooltip(fields=['name', 'region'], aliases=['State:', 'Region:']),
    popup=lambda feature: us_popup_html(feature['properties']['region'])
).add_to(m)

# Save the map to an HTML file
m.save('combined_world_us_map.html')
