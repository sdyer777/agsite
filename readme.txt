AGSITE - README

INSTRUCTIONS
- check out from GitHub https://github.com/sdyer777/agsite.git 
- start python server:
- change to folder ‘agsite’
- run python server - python manage.py runserver
- In browser, enter UIRL - http://127.0.0.1:8000

FEATURES
rollover highlights
tooltips
admin system
sample CSV file download
average wait times rounded to 1 decimal place.
retrieves max latest 1000 records from the database

ADMIN:
username: admin
password: avantgarde

NOTES
Mixed back-end and front end data logic - backend queries into aggregated values per date, front end then works with that to draw graphs.
Included D3 from website - saving d3.zip to local wasn’t providing the Time function, causing JS errors.  d3 lib is still in the repo under static/d3 but is unused
Effective tutorials:
- Python:  https://docs.python.org/3/tutorial/
- Django:  https://docs.djangoproject.com/en/1.11/intro/tutorial01/
A breakdown of "m" vs. "f" patients was intended for the chart, but was left out.  This "patient type" is still present in the data though.

TOOLS USED
macOS Terminal shell
python 3.6
django 1.11
sqlite 
web browser included with python (python manage.py runserver)
virtual environment
IDLE was used for IDE
DB Browser for SQLite - http://sqlitebrowser.org
D3 V3
labratrevenge tooltips -  http://labratrevenge.com/d3-tip/javascripts/d3.tip.v0.6.3.js
SmartGit client
Textwrangler

