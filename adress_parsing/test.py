import pyap

test_string = "C.W. Wiebe Medical Centre, 385 Main Street, Winkler, MB, R6W 1J2"

parsed = pyap.parse(test_string, country='CA')
print(parsed[0].as_dict())