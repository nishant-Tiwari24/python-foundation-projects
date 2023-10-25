from gmplot import gmplot
import csv
gmap = gmplot.GoogleMapPlotter(28.689519,77.324495,17)
gmap.coloricon = "https://googlemapsmakers.com/v1/%s/"

with open('route.csv','r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        gmap.marker(lat,long,'red')
        
gmap.draw('mymap.html')
        
        