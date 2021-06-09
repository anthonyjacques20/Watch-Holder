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

Created an IP Passthrough on modem so that Raspberry Pi has public IP address.
Setup Dynu Dynamic DNS to update the IP address on my website whenever my Raspberry Pi has its IP address updated

In order to access from anywhere (so I can command it from Google Assistant), I am going to use Dynu to redirect to raspberry pi's IP address where nginx will point to the locally running server via uswgi

Was getting a 502 Bad Gateway from nginx because my uwsgi file (WatchHolder.ini) was incorrectly pointing at main.sock and should've been pointed at WatchHolder.sock

Should I start running my raspberry pi from anthonyjacques20.com??! And stop hosting it from heroku?!
    -I could but would have to configure a lot of database stuff to make that work which sounds like a lot of work...
    -Will focus on the watch holder website for now and redirect to it from Dynu

To test just the uwsgi (note that I must activate the virtual environment because uwsgi is only installed in WatchHolder's virtual environment at `/home/pi/GitHub/WatchHolder/venv` and activate with `source venv/bin/activate`. Deactivate with `deactivate`):
```
uwsgi --socket 0.0.0.0:8000 --protocol.http -w wsgi:app
```

To restart the uwsgi server to receive new updates:
```
sudo systemctl restart WatchHolder.service
```

Note that I was following this [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)

## To resume:
1. Power on Raspberry Pi and plug into network
    1. It should be that easy because both uwsgi and nginx are services that are set to start on power on
    1. Make sure that the IP address of the raspberry pi matches the IPv4 listed in [dynu](dynu.com/en-US/ControlPanel/DDNS), if not then Dynu will be redirecting to the wrong IP address
    1. Check the status of the services with `sudo systemctl status WatchHolder` for the uwsgi status and `sudo systemctl status nginx` for the nginx status
        1. Both should show `active(running)`
        1. Can also verify that uwsgi is working correctly by navigating to `localhost` from raspberry pi
    
## Next Steps:
1. Wire up actuator again to verify that calling the URL from outside actually triggers the actuator to move
    1. Need to solder things together to have a more rigid solution
    1. Wire up buttons and add to electrical drawings
1. Setup google assistant actions to hit the URL on certain commands (will need to use IFTTT for this)
1. Add LCD to raspberry pi to show IP address on it so that I can ssh into it from my chromebook and not have to get the raspberry pi setup all the time but rather just leave it plugged in.
	1. To see the IP address, look at /home/pi/Sandbox/PrintIPAddress.py. It is a super simple program that uses netifaces to print the current IP Address to the console every 10 minutes
	1. Need to make this python program run on startup and make it more robust
