# Waterrower
Experimental Bluez GATT service to export Waterrower data as Cycling Power, Speed and Cadence.

The Waterrower is a great rowing machine but the provided S4 interface leaves a lot to be desired - such as Bluetooth LE support. With this simple set of Python scripts and a Raspberry Pi, you can then use any cycling fitness app that supports BTLE Cycling sensors to capture your workout data.

Provides support for two GATT services: Cycling Power (0x818) and Cycling Speed and Cadence (0x816).

The reported speed (wheel revolutions) is not a 1:1 match to what the S4 displays.  The S4 appears to do some complex math to compute drag and momentum of a boat, so the speed ramps up slowly and ramps down slowly.   This script simply reports wheel revolutions based on observed pin counts in the paddle wheel and does not attempt to do any drag or momentum calculations.  Once your rowing gets to a constant speed as reported on the S4, the reported speed in an app using this GATT service should roughly match. 

This was based on some of the sample Python scripts provided with Bluez.   I am not a Python programmer (I mainly use C/C++), so this is most-likely not the best written Python script you've ever seen.

# Requirements

* This was tested on a Raspberry Pi 3, running Raspbian Jessie.  It should be fairly easy to port to other platforms.
* Requires Bluez with LE support.
  * I tested using Bluez 5.43.  
* Waterrower with S4 interface
* Python

# Usage

Connect your Raspberry Pi to the Waterrower using  a USB cable.  On my Pi, the Waterrower shows up as /dev/ttyACM0.  You'll need to edit `waterrower-gatt-server` if your Waterrower is on a different tty.

To enable LE advertising of the service, run:
`waterrower-advertise &`  

To start the Waterrow GATT service:
`waterrower-gatt-server`



