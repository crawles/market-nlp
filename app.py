# -*- coding: utf-8 -*-

"""
app.py
~~~~~~~~~~~~~
marketnlp app
"""
import datetime
import os

from flask import Flask, render_template, request,jsonify

app = Flask(__name__)


up_color = '#20BF2D'
down_color = '#CD0F15'
flat = 'grey'

logos = ['ge.png','aig.png','handr.png','moodys.png','pge.png',
         'disney.png','ensco.jpg','nwl.png']

cos   = ['General Electric (GE)',
         'AIG (AIG)',
         'H & R Block Inc (HRB)',
         "Moody's Corp (MCO)",
         'PG&E Corporation (PCG)',
         'Walt Disney Co (DIS)',
         'Ensco PLC (ESV)',
         'Newell Brands Inc (NWL)']

prices  = ['30.13','57.29','21.59','101.00','61.30','98.81','10.60','48.06']
minutes = [55,47,44,31,26,24,23,16]
arrow_colors = [up_color,down_color,down_color,up_color,flat,down_color,up_color,down_color]
arrow_directions = ['up','down','down','up','','down','up','down']
predictions = ['UP','DOWN','DOWN','UP','FLAT','DOWN','UP','DOWN']
links = ['ge','aig','handr','moodys','pge','disney','esv','nwl']

ntiles = 8
tiles = []

# update everyday
today =  datetime.datetime.now()
day_of_week = today.strftime('%a')
month = today.strftime('%b')
day = today.day
year = today.year
hour = min(9,today.hour) - 1

for i in range(ntiles):
    minute = minutes[i]
    tile = {'logo' : logos[i],
            'name' : cos[i],
            'price' : prices[i],
            'date' : '{}, {} {}, {} at {}:{} EDT'.format(day_of_week,
                                                          month,
                                                          day,
                                                          year,
                                                          hour,
                                                          minute),
            'stock_color' : arrow_colors[i],
            'arrow' : arrow_directions[i],
            'prediction' : predictions[i],
            'link' : links[i]}
    tiles.append(tile)
    

@app.route('/')
def hello_world():
    return render_template('index.html',tiles = tiles)



# negative
@app.route('/aig')
def aig():
    return render_template('AIG 2011-11-03 Down.html')

@app.route('/disney')
def disney():
    return render_template('DIS 2012-11-08 00-00-00 Down_hl.html')

@app.route('/handr')
def handr():
    return render_template('HRB 2012-03-07 00-00-00_hl.html')

@app.route('/nwl')
def nwl():
    return render_template('NWL 2012-10-26_hl.html')

# neutral
@app.route('/pge')
def pge():
    return render_template('PGE 2011-08-04 Stay.html')

# up
@app.route('/esv')
def esv():
    return render_template('ESV 2012-05-02_hl.html')

@app.route('/moodys')
def moodys():
    return render_template('Moodys 2012-07-26 000000 Up.html')

@app.route('/ge')
def ge():
    return render_template('GE 2012-04-20 000000 Up_hl.html')



    
if os.environ.get('VCAP_SERVICES') is None: # running locally
    PORT = 8080
    DEBUG = True
else:                                       # running on CF
    PORT = int(os.getenv("PORT"))
    DEBUG = False
    
app.run(host='0.0.0.0',port=PORT, debug=DEBUG)
