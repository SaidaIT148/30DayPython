import requests
import pandas as pd
import os
import sys
from requests_html import HTML
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def url_to_text(url, filename="workd.html", save=False):
    with requests.get(url) as r:
        if r.status_code == 200:
            html_text = r.text
            if save:
                with open(filename, "w") as f:
                    f.write(html_text)
            return html_text
        return None


def parse_and_extract(url, name='2021'):
    html_text = url_to_text(url)
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    # table class
    r_table = r_html.find(table_class)
    # print table
    header_names = []
    table_data = []
    if len(r_table) == 0:
        return False
    if len(r_table) == 1:
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")
        header_row = rows[0]
        header_cols = header_row.find("th")
        header_names = [x.text for x in header_cols]
        table_data = []
        for row in rows[1:]:
            cols = row.find("td")
            row_data = []
            for i, col in enumerate(cols):
                row_data.append(col.text)
            table_data.append(row_data)

    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join('data', f'{name}.csv')
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(file_path, index=False)
    return True


def run(start_year=None, years_ago=10):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    # if condition fails it will throw assertionError or else it will work as continue
    assert isinstance(start_year, int)
    assert len(f"{start_year}") == 4
    assert isinstance(years_ago, int)

    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"{start_year} not finished")
        start_year -= 1


if __name__ == '__main__':
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 1
    run(start, count)
