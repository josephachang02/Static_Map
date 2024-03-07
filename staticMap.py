import geopandas as gpd
import matplotlib.pyplot as plt

grid_fp = "r/C:/Users/Joe Chang/Desktop/CS/Python/Data/dataE5/TravelTimes_to_5975375_RailwayStation.shp"
roads_fp = "r/C:/Users/Joe Chang/Desktop/CS/Python/Data/dataE5/roads.shp"
metro_fp = "r/C:/Users/Joe Chang/Desktop/CS/Python/Data/dataE5/metro.shp"

# Read Files
grid = gpd.read_file(grid_fp)
roads = gpd.read_file(roads_fp)
metro = gpd.read_file(metro_fp)

# Get the CRS of the grid
gridCRS = grid.crs

# Reproject geometries using the crs of travel time grid
roads['geometry'] = roads['geometry'].to_crs(crs=gridCRS)
metro['geometry'] = metro['geometry'].to_crs(crs=gridCRS)

# Visualize the travel times into 9 classes using "Quantiles" classification scheme
my_map = grid.plot(column="car_r_t", linewidth=0.03, cmap="Reds", scheme="quantiles", k=9, alpha=0.9)

#Add roads and metro
roads.plot(ax=my_map, color="grey", linewidth=1.5)
metro.plot(ax=my_map, color="red", linewidth=2.5)

#Remove the empty white-space around the axes
plt.tight_layout()

outfp = "r/C:/Users/Joe Chang/Desktop/CS/Python/Data/dataE5/static_map.png"
plt.savefig(outfp, dpi=300)

