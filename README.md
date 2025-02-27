# python-mega-course
Code exercise for the python-mega-course

Name | Description
------------ | -------------
Interactive Dictionary | Simple command line application to get definition of words based on in-memory/database source.
Web Map | Web-map with multiple layers and markers, using Folium
Website Blocker | Simple python script to block (predefine) websites during the predefine time window
Static Web Side | Simple web side with Flask and Jinja templating
Windows GUI | Simple GUI for CRUD operations
Motion Detection | Detect any motion on a webcam view port, record detection timestamp and visual the result in time series graph
Web Scrapper | Extract real state data with web scrapper
Stock Market Data Visualizer | Visualize stock market data

### Application 01 - Interactive Dictionary
Simple command line application to get definition of words based on in-memory/database source.

External Modules - [_mysql.connector, difflib, json_]

![Image description](doc/app_dictonary.JPG)

### Application 02 - WebMap with Folium
Web-map with multiple layers and markers, using Folium (wrapper for [leaflet.js](https://python-visualization.github.io/folium/))

External Modules - [_folium, pandas_]

![Image description](doc/webmap.JPG)
Source: 
1. https://eric.clst.org/tech/usgeojson/
2. https://www.census.gov/

### Application 03 - Website Blocker 
Simple python script to block (predefine) websites during the predefine time window
![Image description](doc/web_blocker.jpg)

### Application 04 - Static Web Side
Simple web side with Flask and Jinja templating

External Modules - [_flask, jinja_]

https://k-sample-app.herokuapp.com/about

### Application 05 - Windows GUI
Simple GUI for CRUD operations
External Modules - [_sqlite3, tkinter_]

![Image description](doc/book_store.JPG)

### Application 06 - Motion Detection
Detect any motion on a webcam view port, record detection timestamp and visual the result in time series graph

External Modules - [_open-cv, scikit-image, numpy_]

![Image description](doc/motion_detect.JPG)
![Image description](doc/motion_detect_graph.jpg)

### Application 07 - Web Scrapper
Extract real state data with web scrapper

External Modules - [_request, bs4, pandas_]

![Image description](doc/web-scrape.JPG)

### Application 08 - Stock Market Data Visualizer
Visualize stock market data

External Modules - [_bokeh, pandas, pandas_datareader, Flask_]

![Image description](doc/stock-market.JPG)
