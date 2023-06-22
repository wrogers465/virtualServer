This repository is meant to be run on the Raspberry Pi

On the Raspberry Pi, this is the location of the script that run on restart to launch the server: /etc/systemd/system/server.service. cd to the directory and then do
"sudo nano server.service" to edit. NOTE: FIX THIS IF RESTART DOES NOT WORK: ExecStart=python /home/pi/Python/Projects/virtualServer/sample/app.py

Instructions on how to update pi to Python 3.10

Current point in tutorial: https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/



OTHER LINKS:
Great instructions on how to update Python version on raspberry pi: https://aruljohn.com/blog/python-raspberrypi/
