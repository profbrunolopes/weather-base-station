# Weather Base Station

The purpose of this project is to build a weather base station with a Raspberry Pi that receives data from an Arduino weather station, store these data on an SQLite database, and expose these data through a REST API written in Flask.

## Sensors
This project was built with the use of a Raspberry PI B model 1 and the following sensors:

NRF24l01 - Wireless transceiver module used to receive the collected data by Arduino Weather Station.

## Libraries
In the present project, the following libraries were used:

**pyRF24 by TMRh20**: This library was necessary to use the NRF24l01 sensor on Pyhton 3 language;
**pyRF24Network by TMRh20**: This library was necessary to create a sensor network using the NRF24l01 transceiver on Pyhton 3 language;

The libraries listed above must be compiled to Raspberry Pi. Follow this [documentation](http://google.com) to do so.

## Electrical Schematic
The figure bellow shows how the physical sensors must be connected on the Raspberry Pi:

![Image of Raspberry Pi Eletronic Schematic](hackaton-raspberry.png)

## Running the project

To get this project running you need Python 3 installed on Raspberry Pi as well as the New Relic Python Agent. First it's necessary to create an account on [New Relic](https://newrelic.com/) and follow their [instructions](https://docs.newrelic.com/docs/agents/python-agent/installation/standard-python-agent-install). The file **newrelic.ini** must be in the same folder as weather_base_station.py, or you can create the environment variable NEW_RELIC_CONFIG_FILE pointing to **newrelic.ini** location. See the bellow example:

```bash
#You must create the New Relic account first
$ pip3 install newrelic
$ newrelic-admin generate-config <YOUR_LICENSE_KEY> newrelic.ini
$ export NEW_RELIC_CONFIG_FILE=<YOUR_NEWRELIC.INI_FILE_PATH>
$ chmod 755 weather_base_station.py
$ newrelic-admin run-program weather_base_station.py
```

## Related Projects
This project only receives data from Arduino Station, store it on an SQLite database and exposes it with a RESP API. An Arduino Station was developed to collect the data and a dashboard was also built in HTML5, CSS3, and JS to display all the data to the user by consuming the REST API exposed by this base station. For more details about the base station project or the dashboard project, visit:

* [Arduino Weather Station](https://github.com/profbrunolopes/weather-arduino-sensor)
* [Weather Station Dashboard](https://github.com/profbrunolopes/weather-dashboard)
