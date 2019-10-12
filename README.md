# TinkerBoardDisplayController
A small python script that turns on or off the display output of the Asus TinkerBoard based on the input of a radar sensor (e.g RCWL0516)

I added a `systemd` service file to use it as `systemd` service and start it at boot time.

## Installation

Clone the repository to wherever you want:

`git clone https://github.com/crehmann/TinkerBoardDisplayController`

If you want it started as a `systemd` service, you have to copy the `.service` file to `/lib/systemd/system` and reload the `systemd` daemons:

```
cp ./radar_sensor.service /lib/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable radar_sensor.service
sudo systemctl start radar_sensor.service
```

You have to change line 7 to the location of the `displayController.py` file like this:

`ExecStart=/usr/bin/python /path/to/your/displayController.py > /path/to/your/displayController.log 2>&1`

## Configuration

You can configure the time until the display is turned off with `TimeUntilDisplayOff` variable. The value is given in seconds. 

The `MotionSensor` variable should be set to the connected data pin of the radar sensor. Default is `257`.
