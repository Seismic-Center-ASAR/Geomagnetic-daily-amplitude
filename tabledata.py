import requests
from bs4 import BeautifulSoup

# Make a request to the website page old Intermagnet version
# url = 'https://www.intermagnet.org/data-donnee/dataplot-1-eng.php?year=2023&month=3&day=18&start_hour=0&end_hour=24&filter_region%5B%5D=America&filter_region%5B%5D=Asia&filter_region%5B%5D=Europe&filter_region%5B%5D=Pacific&filter_region%5B%5D=Africa&filter_lat%5B%5D=NH&filter_lat%5B%5D=NM&filter_lat%5B%5D=E&filter_lat%5B%5D=SM&filter_lat%5B%5D=SH&sort=iaga&iaga_code=SUA&type=xyz&fixed_scale=0&format=html'
#new Intermagnet hosting in UK
url = 'https://imag-data.bgs.ac.uk/GIN_V1/GINServices?Request=GetData&format=HTML&testObsys=0&observatoryIagaCode=SUA&samplesPerDay=minute&publicationState=Best%20available&dataStartDate=2023-05-01&dataDuration=1'
response = requests.get(url)

# Parse the HTML source code using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element based on the class attribute, old Intermagnet
#table = soup.find('table', {'class': 'span-6'})
table = soup.find('table')

# Extract the table data and write it to a text file
with open('table_data.txt', 'w') as file:
    file.write("Date/Time (UT)\tX (nT)\tY (nT)\tZ (nT)\tF (nT)\n") # write the header
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            file.write(cell.get_text() + '\t')
        file.write('\n')
