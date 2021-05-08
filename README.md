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
Next step is to be able to access from anywhere, this will allow me to command it from Google Assistant. -Just need to figure out nginx
Should I start running my raspberry pi from anthonyjacques20.com??! And stop hosting it from heroku?!
    -I could but would have to configure a lot of database stuff to make that work which sounds like a lot of work...
    -Will focus on the watch holder website for now and redirect to it from Dynu


## To resume:
1. Need to access code from anywhere so Google Assistant can access it
1. Need to figure out why we are getting a 502 Bad Gateway from nginx...

Latest Update - Created an IP Passthrough on modem so that Raspberry Pi has public IP address
Setup Dynu Dynamic DNS to update the IP address on my website whenever my Raspberry Pi has its IP address updated
Am able to navigate to Raspberry Pi's IP address/port and see my website if I'm running it with gunicorn IP:Port where IP matches raspberry pi's public IP
Getting a 502 Bad Gateway when trying to navigate to regular website/IP address
Note that uwsgi and nginx are both set to start as services on startup

