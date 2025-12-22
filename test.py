import requests
import pandas as pd

url = '{(copied url here)}' 
res = requests.get(url, allow_redirects=True)
with open('download_file_name.csv','wb') as file:
    file.write(res.content)
download_file_name = pd.read_csv('download_file_name.csv') 
