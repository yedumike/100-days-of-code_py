import camelot

tables = camelot.read_pdf('foo.pdf',pages='1')
print(tables)


#1
"""
What it does:
Exports all detected tables (tables) from the PDF.
Saves them as multiple CSV files, with names like:
css
Copy
Edit
"""
tables.export('myfoo1.csv',f="csv", compress=True)


#the below simply exports a table and saves in csv

# tables[0].to_csv('myfoo.csv')

