import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\edevillers\\Documents\\Tokens\\pympPowerBi-72417e0c908e.json", scope)

gc = gspread.authorize(credentials)

sheet1 = gc.open_by_key("1JzfY2XkCGlMD9ot7HGLQz81adgnME8XWOo3GmLcfK2Y").sheet1

# get_all_values gives a list of rows.
rows = sheet1.get_all_values()
print(rows)

# Convert to a DataFrame and render.
df = pd.DataFrame.from_records(rows)