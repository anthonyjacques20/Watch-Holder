# Instructions
Can run file directly in Thonny and it will run with Flask's development server

Can also run it via gunicorn (which I already installed on the pi). When in the same folder as main.py (/home/pi/GitHub/WatchHolder)
With the following command (to run at 127.0.0.1:8000):
```
gunicorn main:app
```
To run at a designated IP address and port, run the following command:
```
gunicorn -b <ip_address>:<port> main:app
```

When running with ip_address, I was able to access it over wifi from my chromebook.
Need to investigate nginx and how it passes requests from a URL to a locally hosted server. (Seems similar to Microsoft's IIS)
Next step is to be able to access from anywhere, this will allow me to command it from Google Assistant.
Should I start running my raspberry pi from anthonyjacques20.com??! And stop hosting it from heroku?!


## To resume testing:
1. Need to access code from anywhere so Google Assistant can access it
1. When I launch gunicorn with a given IP address, what exactly is that doing? Is 192.168.x.x only accessible on wifi? Do I need to adjust some router settings?
