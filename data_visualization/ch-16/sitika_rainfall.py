from pathlib import Path
import csv
import matplotlib.pyplot as plt

from datetime import datetime

path = Path("sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, rainfall = [], []

for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        prcp = float(row[5])
    except ValueError:
        print(f"Invalid data in {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(prcp)

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color="blue")

title = "Precipitation Graph\nSitka 2021"
ax.set_title(title, fontsize=20)

ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (mm)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
