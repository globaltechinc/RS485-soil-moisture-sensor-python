# Global Technology Connection, Inc.
# Jesse Williams
#
# Use to scan for available serial ports

# to install PySerial: python -m pip install pyserial

from serial.tools import list_ports
port_data = list_ports.comports()
for port, desc, hwid in sorted(port_data):
    print(port)
    print(desc)