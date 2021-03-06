# pi-flowers

# config 

create a file called pi_name.txt in the root file, and enter the pi name in that file as the only line.

# Server for pi-flowers

This server listens for pi-flower button presses. When one pi-flower has its button pressed, the server tells the other to light up.

# Startup

`node index.js`

# Creation Steps

npm init
npm install express

# Headless script startup

Copy `pi-flowers.service` into `/etc/systemd/system`:
`sudo cp pi-flowers.service /etc/systemd/system/pi-flowers.service`

Test starting and stopping:
`sudo systemctl start pi-flowers.service`
`sudo systemctl stop pi-flowers.service`

Run this command to enable the app to run on startup:
`sudo systemctl enable pi-flowers.service`

Read logs:
`journalctl -u pi-flowers.service`

# SSH into Pi

Get Pi's IP address:
`ifconfig` 

On remote:
`ssh pi@<IP address>`
