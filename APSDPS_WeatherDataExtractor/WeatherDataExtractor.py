import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup

# Downloading contents of the web page
base_url = "http://www.apsdps.ap.gov.in/Realtime/"



data = requests.get(base_url+"Rainfall24.jsp").text


# Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# Verifying tables and their classes
print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))

# Creating list with all tables
tables = soup.find_all('table')

# table with date time information
heading_table = soup.find('table', class_='table2')
log_datetime = datetime.datetime.strptime(heading_table.thead.find('span',class_='head2').text.rsplit('to', maxsplit=1)[1].strip(), '%d/%m/%Y %I:%M %p')

#  Looking for the data table with the classes 'data-tabel'
data_table = soup.find('table', class_='data-tabel')


# Defining of the dataframe
df = pd.DataFrame(columns=['Station_ID','Date', 'Time', 'District', 'Mandal', 'Location', 'Cum_Rainfall(mm)'])

# Collecting Ddata
for row in data_table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        station_id = columns[1].text.strip()
        district = columns[2].text.strip()
        mandal = columns[3].text.strip()
        location = columns[4].text.strip()
        cum_rainfall_mm = columns[5].text.strip()

        df = pd.concat([df, pd.DataFrame({ 'Station_ID': [station_id], 'Date': [log_datetime.date()], 'Time': [log_datetime.time()], 'District': [district], 'Mandal': [mandal], 'Location': [location], 'Cum_Rainfall(mm)': [cum_rainfall_mm]})], ignore_index=True)

print(df.head())