#Web

> # $ pip3 install bottle
> from bottle import run, route, post, template, request, response
> import json

## Run

run(host='localhost', port=8080)
run(host='0.0.0.0', port=80, server='cherrypy')

## Static Request

@route('/img/<image>')
def send_image(image):
    return static_file(image, 'images/', mimetype='image/png')

## Dynamic Request

@route('/<sport>')
def send_page(sport):
    return template('<h1>{{title}}</h1>', title=sport)

## REST Request

@post('/odds/<sport>')
def odds_handler(sport):
    team = request.forms.get('team')
    home_odds, away_odds = 2.44, 3.29
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps([team, home_odds, away_odds])

### Test:

> # $ pip3 install requests
> >>> import requests
> >>> url  = 'http://localhost:8080/odds/football'
> >>> data = {'team': 'arsenal f.c.'}
> >>> response = requests.post(url, data=data)
> >>> response.json()
> ['arsenal f.c.', 2.44, 3.29]
