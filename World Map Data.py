import folium
import geopandas as gpd

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
    'Russia': 'https://example.com/russia',
    'Central Asia': 'https://example.com/central-asia',
    'MENA': 'https://example.com/mena',
    'North Africa': 'https://example.com/north-africa',
    'South Asia': 'https://example.com/south-asia',
    'East Asia': 'https://example.com/east-asia',
    'Southeast Asia': 'https://example.com/southeast-asia',
    'Oceania': 'https://example.com/oceania',
    'Southern Africa': 'https://example.com/southern-africa',
    'Central Africa': 'https://example.com/central-africa',
    'West Africa': 'https://example.com/west-africa',
    'East Africa': 'https://example.com/east-africa',
    'Caribbean': 'https://example.com/caribbean',
    'Pacific Islands': 'https://example.com/pacific-islands',
    'Other': 'https://example.com/other'
}

# Function to generate pop-up text with clickable hyperlink
def popup_text(region):
    link = region_links.get(region, 'https://example.com')
    return f'<a href="{link}" target="_blank">{region} Information</a>'

# Initialize a Folium map
m = folium.Map(location=[20, 0], zoom_start=2)

# Define a color map for the regions
region_colors = {
    'North America': 'blue',
    'Mexico and Central America': 'green',
    'South America': 'red',
    'West Europe': 'purple',
    'East Europe': 'orange',
    'Russia': 'yellow',
    'Central Asia': 'pink',
    'MENA': 'lightblue',
    'North Africa': 'darkgreen',
    'South Asia': 'cyan',
    'East Asia': 'magenta',
    'Southeast Asia': 'teal',
    'Oceania': 'lightgreen',
    'Southern Africa': 'brown',
    'Central Africa': 'gold',
    'West Africa': 'violet',
    'East Africa': 'silver',
    'Caribbean': 'darkblue',
    'Pacific Islands': 'lightyellow',
    'Other': 'gray'
}

# Function to set the style for each region
def style_function(feature):
    region = feature['properties']['region']
    return {
        'fillOpacity': 0.7,
        'weight': 1,
        'color': 'black',
        'fillColor': region_colors.get(region, 'gray')
    }

# Function to highlight a region on hover
def highlight_function(feature):
    return {
        'weight': 3,
        'color': 'blue',
        'fillOpacity': 0.9
    }

# Add a GeoJson layer to the map
folium.GeoJson(
    world,
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.GeoJsonTooltip(fields=['name', 'region'], aliases=['Country:', 'Region:']),
    popup=folium.GeoJsonPopup(fields=['region'], aliases=['Region:'], labels=True,
                              style="background-color: white;", localize=True,
                              sticky=False),
).add_to(m)

# Save the map to an HTML file
m.save('interactive_world_map.html')
