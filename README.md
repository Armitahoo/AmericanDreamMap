### Interactive World and U.S. Region Maps with Folium

This project includes two interactive maps:
1. A **world map** divided into customized regions.
2. A **U.S. map** divided into four geographic regions: Northeast, Midwest, South, and West.

Both maps allow users to hover over different regions and click on them to access a URL hyperlink that provides more information about that specific region.

#### 1. World Map

The world map was created using **Geopandas** and **Folium** to group countries into customized regions and visualize them with distinct colors. Each region has a hyperlink embedded, so clicking on a region takes the user to an external link for more information.

##### Steps:
- **Loading Data:** 
  The `naturalearth_lowres` dataset from `geopandas` is used to load the geometries of all countries. This dataset contains low-resolution world map data with country boundaries.

- **Custom Region Groupings:**
  Countries are divided into custom geographic and political regions (e.g., North America, MENA, East Africa, etc.). This is done by creating a Python dictionary (`region_groups`) that maps countries to their respective regions.

- **Assigning Regions to Countries:**
  A function `get_region(country)` is used to match each country to its corresponding region based on the dictionary defined earlier. A new column `'region'` is added to the `geopandas` dataframe, assigning each country to a specific region.

- **Hyperlinks:**
  Each region is associated with a hyperlink. The `region_links` dictionary stores the URL for each region. A function `popup_text(region)` creates an interactive popup for each region, which displays the hyperlink in a popup when clicked.

- **Map Customization:**
  The map uses **GeoJSON** layers, colored by region. Each region is given a distinct color for visual differentiation, and the countries within the regions are filled with a semi-transparent color. When hovering over a region, the color changes for emphasis.

- **Highlighting and Tooltip:**
  A tooltip is added to show the region name when hovering over a region. Highlighting is used to give visual feedback when a region is hovered over, changing the fill color.

- **Saving and Viewing:**
  The map is saved as an HTML file (`interactive_map.html`) that can be viewed in a web browser.

---

#### 2. U.S. Map

The U.S. map divides the country into four major regions: Northeast, Midwest, South, and West. Each region is colored distinctly and linked to a URL for more information.

##### Steps:
- **Loading Data:**
  The map of U.S. states is loaded from a GeoJSON file available at a public URL (`https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json`). This file contains state boundaries for the entire U.S.

- **Region Groupings:**
  The U.S. is divided into four regions (Northeast, Midwest, South, and West) using a dictionary (`us_region_groups`) that lists states corresponding to each region.

- **Assigning Regions to States:**
  Similar to the world map, a function `get_us_region(state_name)` is used to assign each U.S. state to its corresponding region. A new `'region'` column is added to the `geopandas` dataframe for U.S. states.

- **Hyperlinks:**
  Each U.S. region has a clickable hyperlink stored in the `us_region_links` dictionary. A popup function `us_popup_html(region)` is used to display an interactive link in the popup for each region.

- **Map Customization:**
  The U.S. map uses **GeoJSON** layers to color each state according to its region. States in each region are filled with a region-specific color, and borders are outlined in black. Hovering over a state highlights it by changing the fill color.

- **Tooltip and Highlighting:**
  A tooltip is added to show the region name when hovering over a state, and states are highlighted with a color change to make interaction more intuitive.

- **Saving and Viewing:**
  The U.S. map is saved as an HTML file (`us_regions_map.html`) that can be viewed in a web browser.

---

### Installation & Usage

#### Dependencies:
- `geopandas`: Used for loading and processing geographical data.
- `folium`: Used to create interactive maps and visualizations.
- `pandas` (optional): For additional data manipulation if needed.

To install the required dependencies, run:

```bash
pip install geopandas folium pandas
