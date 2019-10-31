from bottle import run, route, post, template, request, response
import json

run(host='localhost', port=8080)
run(host='0.0.0.0', port=80, server='osx')

@post('/odds/<sport>')
def odds_handler(sport):
    team = request.forms.get('team')
    home_odds, away_odds = 2.44, 3.29
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps([team, home_odds, away_odds])
