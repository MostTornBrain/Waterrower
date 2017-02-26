# Waterrower
Experimental Bluez GATT service to export Waterrower data as Cycling Power, Speed and Cadence.

The Waterrower is a great rowing machine, but the provided S4 interface leaves a lot to be desired - such as Bluetooth LE support.  
With this simple set of Python scripts, you can then use any cycling fitness app that support BTLE Cycling sensors to capture your 
workout data.

Currently the GATT service provides kcal/watt and cadence data. A future update will provide speed data.

This was based on some of the sample Python scripts provided with Bluez.   I am not a Python programmer (I mainly use C/C++), so
this is most-likely not the best written Python script you've ever seen.

# Requirements

* This was tested on a Raspberry Pi 3, running Raspbian Jessie.  It should be fairly easy to port to other platforms.
* Requires Bluez with LE support.
* Waterrower with S4 interface
* Python

# Usage

Connect your Raspberry Pi to the Waterrower using  a USB cable.  On my Pi, the Waterrower shows up as /dev/ttyACM0.  You'll need to
edit `waterrower-gatt-server` if your Waterrower is on a different tty.

To enable LE advertising of the service, run:
`waterrower-advertise &`  

To start the Waterrow GATT service:
`waterrower-gatt-server`

NOTE: currently, the script will die if it can not find the Waterrower tty. An improvement would be to have it wait until
the tty is present rather than just crashing.

