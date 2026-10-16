import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.srikanthtechnologies.com/default.aspx"
resp = requests.get(WEBSITE,
                    headers={
                        "User-Agent": (
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/130.0.0.0 Safari/537.36"
                        )
                    },
                    timeout=20
                    )


bs = BeautifulSoup(resp.text, "html.parser")

schedule_table = bs.find(id = "GridView2")

rows = schedule_table.find_all("tr")

# Take second row onwards as first row is having headings
for row in rows[1:]:
    cols = row.find_all("td")
    course = cols[1].text
    timings = cols[2].text
    start_date = cols[3].text
    sessions = cols[6].text
    print(f"{course:40}   {timings:20} {start_date:10}  {sessions:3}")