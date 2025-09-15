import requests, pytz
from rich.console import Console
from rich.table import Table
console=Console()
cities={"Pune": "18.5204, 73.8567",
    "Mumbai": "19.0760, 72.8777",
            }
table=Table(title="⛅Weather Dashboard", style="cyan")
table.add_column("City", justify="center")
table.add_column("Temperature (C)", justify="center")
for city, coords in cities.items():
    temp=requests.get(f"https://wttr.in/{coords}?format=%t").text
    table.add_row(city, temp)
console.print(table)