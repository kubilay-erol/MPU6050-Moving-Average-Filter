import machine
import math

import time


i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))

MPU_ADDR = 0x68
i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')

def read_raw_g():
    
    data = i2c.readfrom_mem(MPU_ADDR, 0x3B, 6)
    
    def bytes_to_int(high, low):
        val = (high << 8) | low
        return val if val < 32768 else val - 65536
      
    ax = (bytes_to_int(data[0], data[1]) / 16384.0) * 9.80665
    ay = (bytes_to_int(data[2], data[3]) / 16384.0) * 9.80665
    az = (bytes_to_int(data[4], data[5]) / 16384.0) * 9.80665
    

    return math.sqrt(ax**2 + ay**2 + az**2)

print("Timestamp(ms),Raw_G(m/s^2)")


while True:
    timestamp = time.ticks_ms()
    raw_g = read_raw_g()
  
    print(f"{timestamp},{raw_g:.3f}")
    time.sleep(0.1)
