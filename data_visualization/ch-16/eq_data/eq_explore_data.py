from pathlib import Path
import json

import plotly.express as px

path = Path("significant_month.geojson")
# path = Path("all_month.geojson")

contents = path.read_text()
all_eq_data = json.loads(contents)


path = Path("readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

# mags, lons, lats, eq_titles = [], [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict["properties"]["mag"]
#     lon = eq_dict["geometry"]["coordinates"][0]
#     lat = eq_dict["geometry"]["coordinates"][1]
#     eq_title = eq_dict["properties"]["title"]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)
#     eq_titles.append(eq_title)


mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    eq_titles.append(eq_dict["properties"]["title"])


title = all_eq_data["metadata"]["title"]
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
print(mags[:10])
print(lons[:5])
print(lats[:5])
