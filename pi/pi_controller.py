import requests
import time
import random
import click
from sense_hat import SenseHat


def get_direction(ev):
    d_long = 0
    d_la = 0
    send_vel = False
    print(ev.direction)
    if ev.direction =='left':
        click.echo('Left')
        send_vel = True
        d_long = -1
        d_la = 0
    elif ev.direction == 'right':
        click.echo('Right')
        send_vel = True
        d_long = 1
        d_la = 0
    elif ev.direction =='up':
        click.echo('Up')
        send_vel = True
        d_long = 0
        d_la = 1
    elif ev.direction == 'down':
        click.echo('Down')
        send_vel = True
        d_long = 0
        d_la = -1
    else:
        d_long = 0
        d_la = 0
        click.echo('Invalid input :(')
        send_vel = False
    return d_long, d_la, send_vel

sense_hat = SenseHat();
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        for event in sense_hat.stick.get_events():
            if event.action == "pressed":
                d_long, d_la, send_vel = get_direction(event)
                if send_vel:
                    with requests.Session() as session:
                        current_location = {'longitude': d_long,
                                            'latitude': d_la
                                            }
                        resp = session.post(SERVER_URL, json=current_location)
