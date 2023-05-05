# Global Technology Connection, Inc.
# Jesse Williams
#
# Reading data from the Seeed Studio Industrial Soil Moisture & Temperature & EC Sensor MODBUS-RTU RS485 (S-Soil MTEC-02A)


# to install PySerial: python -m pip install pyserial
import serial

# Construct (and open) the serial connection
# Note that you will have to use the correct port, see 0_scan_com_ports.py

ser = serial.Serial(
    port='COM5',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=5
)

# Construct the Modbus message to read a register
# This grabs the first 7 registers
message = (0x01, 0x03, 0x00, 0x00, 0x00, 0x07, 0x04, 0x08)

# Send the message to the device
ser.write(message)

# Read the response
response = ser.readline()

# Close the connection
ser.close()

# Extract the data from the response
data = response[3:-2]

# Convert the data to a list of integers
values = [int.from_bytes(data[i:i+2], byteorder='big', signed=False) for i in range(0, len(data), 2)]

# Extract values
temp = values[0] # -4000 to 8000, where 1000 = 10C
temp = temp/100 # Now in units of C

water_content = values[1] # 0-10000 corresponds to 0-100%
water_content = water_content/100 #Units of percent

elec_conduct = values[2] # 0-20000 corresponds to 0-20000us/cm

salinity = values[3] # 0-20000 corresponds to 0-20000mg/L

tds = values[4] # 0-20000 corresponds to 0-20000mg/L

epsilon = values[5] # 0-8200 corresponds to 0.00~82.00
epsilon = epsilon/100 # convert to percent

soil_type = values[6] #0-3
                    # 0: Mineral soil
                    # 1: Sandy soil
                    # 2: Clay
                    # 3: Organic soil 

print("Temp: {}, Water %: {}".format(temp, water_content))
print("Elect Cond: {}, Salinity: {}, TDS: {}".format(elec_conduct, salinity, tds))
print("Soil type: {}".format(soil_type))