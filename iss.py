import urllib
import turtle
import json
import time


def find_astros():
    response = json.loads(urllib.urlopen(
        'http://api.open-notify.org/astros.json').read())
    for person in response['people']:
        print "Craft: {}".format(person['craft'])
        print "Name: {}".format(person['name'])
    print "Total number of astronauts in space: {}".format(response['number'])


def get_current_coords():
    response = json.loads(urllib.urlopen(
        'http://api.open-notify.org/iss-now.json').read())
    return response['iss_position'], response['timestamp']


def pass_over():
    response = json.loads(urllib.urlopen(
        'http://api.open-notify.org/iss-pass.json?lat=39&lon=-86').read())
    return ("Next time the ISS will be over Indianapolis, IN: " +
            time.ctime(response['response'][-1]['risetime']))


def create_map():
    coords = get_current_coords()
    world = turtle.Screen()
    iss = turtle.Turtle()
    indy = turtle.Turtle()
    world.setup(width=720, height=360, startx=0, starty=0)
    world.setworldcoordinates(-180, -90, 180, 90)
    indy.shape('circle')
    indy.color('yellow')
    indy.penup()
    indy.resizemode('user')
    indy.shapesize(.25, .25, .1)
    indy.goto(-86, 39)
    indy.write(pass_over(), False, align="center")
    iss.penup()
    iss.goto(float(coords[0]['longitude']), float(coords[0]['latitude']))
    world.bgpic('map.gif')
    world.register_shape('iss.gif')
    iss.shape('iss.gif')
    world.exitonclick()


def main():
    find_astros()
    create_map()


if __name__ == "__main__":
    main()
