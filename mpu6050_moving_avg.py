import machine, math, time

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))

MPU_ADDR = 0x68

i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')

readings = []

filter_size = 20

def read_raw_g():
    
    data = i2c.readfrom_mem(MPU_ADDR, 0x3B, 6)
	
  
    def bytes_to_int(high, low):
        val = (high << 8) | low
        return val if val < 32768 else val - 65536

    
    ax = (bytes_to_int(data[0], data[1]) / 16384.0) * 9.80665
    ay = (bytes_to_int(data[2], data[3]) / 16384.0) * 9.80665
    az = (bytes_to_int(data[4], data[5]) / 16384.0) * 9.80665

  
    return math.sqrt(ax**2 + ay**2 + az**2)

while True:
    current_val = read_raw_g()
    readings.append(current_val)
    
    if len(readings) > filter_size:
        readings.pop(0)

    filtered_g = sum(readings) / len(readings)
    print(f"Filtered G: {filtered_g:.4f} m/s^2")
    time.sleep(0.05)