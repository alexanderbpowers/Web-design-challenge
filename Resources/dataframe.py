import pandas as pd

data = pd.read_csv('Web-design-challenge/Resources/cities.csv')
print(data)

data_html = data.to_html()
print(data_html)

text_file = open("Web-design-challenge/Website/data.html", "w")
text_file.write(data_html)
text_file.close()