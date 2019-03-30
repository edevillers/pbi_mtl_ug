import pyap
import pandas as pd
import json

test_string = "C.W. Wiebe Medical Centre, 385 Main Street, Winkler, MB, R6W 1J2"

parsed = pyap.parse(test_string, country='CA')
print(parsed[0].as_dict())


# data = {'adress': ["C.W. Wiebe Medical Centre, 385 Main Street, Winkler, MB, R6W 1J2"
#                 ,"Tootelo, 204 boul Montarville, suite 2500, Boucherville, Qc, J4b6S2"]}
# df = pd.DataFrame(data=data)
# df.info()
df = pd.read_csv('PhysicianDirectory.csv')

print(df)

df['concat'] = df['OFFICE_ADDRESS'] + ", " +  df['OFFICE_CITY'] + ", " + df['OFFICE_PROVINCE'] + ", " + df['OFFICE_POSTAL']

# no_match = "{""full_address"": ""{full}"", ""full_street"": """", ""street_number"": """", ""street_name"": """", ""street_type"": """", ""route_id"": """", ""post_direction"": """", ""floor"": """", ""building_id"": """", ""occupancy"": """", ""postal_box"": """", ""city"": """", ""region1"": """", ""postal_code"": """", ""country_id"": """"}"

def parse_adress(colonne, no_match=no_match):
    try:
        parsed_obj = pyap.parse(colonne, country='CA')
        try:
            parsed = parsed_obj[0].as_dict()
        except IndexError:
            parsed = ""
    except TypeError:
        print(colonne)
        parsed = ""
    parsed = json.dumps(parsed)
    return parsed
    

df['parsed'] = df['concat'].apply(parse_adress)

print(df['concat'])
df.info()
print(df)