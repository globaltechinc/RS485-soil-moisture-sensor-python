# Python communication with a Seeed Studio RS485 Soil Moisture & Temperture Sensor

[<img alt="GTC Logo" width="100px" src="/images/gtc_logo.png" />](http://globaltechinc.com)


This repository shows how to read data from an industrial soil moisture and temperture sensor using Python via the RS485 protocol.

## Hardware

**Soil Moisture and Temperature Probe**

This code was developed for the [Seeed Studio Industrial Soil Moisture & Temperature & EC Sensor MODBUS-RTU RS485 (S-Soil MTEC-02A)](https://www.seeedstudio.com/RS485-Soil-Moisture-Temperature-EC-Sensor-S-Soil-MTEC-02-p-4633.html). 

[<img alt="soil probe" width="300px" src="/images/moisture_sensor.PNG" />](https://www.seeedstudio.com/RS485-Soil-Moisture-Temperature-EC-Sensor-S-Soil-MTEC-02-p-4633.html)

Note that the wiring is as follows:

<img alt="wire diagram" width="300px" src="/images/wiring_diagram.png" />


**USB to RS485**

An adapater is required to connect a RS485 device to a computer. I'm using the following USB to RS485 device: [FEANTEEK USB to RS485 Converter, RS485 Adapter FT232RL](https://www.amazon.com/gp/product/B08PL23NW8)

<img alt="converter" width="300px" src="/images/feanteek_usb_to_rs485.jpg" />

## Software

