# Weather Base Station

The purpose of this project is to build a weather base station with Raspberry Pi that receives data from Arduino weather station, store these data on SQLite database, and expose these data through REST API written in Flask.

## Sensors
To build this project was used on an Raspberry PI B model 1 with the following sensors:

NRF24l01 - Wireless transceiver module used to receive the collected data by Arduino Weather Station.

## Libraries
In the present project, the following libraries were used:

**pyRF24 by TMRh20**: Necessary library to use the NRF24l01 sensor on Pyhton 3 language;
**pyRF24Network by TMRh20**: Necessary library to create a sensor network using the NRF24l01 transceiver on Pyhton 3 language;

The libraries listed above must be compiled to Raspberry Pi. Follow this [documentation](http://google.com) to compile these libraries on Raspberry Pi.


## Electrical Schematic
The figure bellow show as the phisical sensors must be connected on Raspberry Pi:

![Image of Raspberry Pi Eletronic Schematic](hackaton-raspberry.png)


## Related Projects

This project only receive the aquired data from Arduino Station and tore it on SQLite database and expose it on RESP API. A Arduino Station was developed to collect the data and a dashboard was also built in HTML5, CSS3, and JS that displays this data to the user by consuming a REST API exposed by this base station. For more details of the base station project or dashboard project, visit:

* [Arduino Weather Station](https://github.com/profbrunolopes/weather-arduino-sensor)
* [Weather Station Dashboard](http://google.com)
