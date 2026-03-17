# MPU6050 Moving Average Filter

Moving average filter for MPU-6050 accelerometer data using MicroPython on ESP32 Supermini C3.

## Hardware

- ESP32 Supermini C3
- MPU-6050 IMU

## Wiring

| MPU-6050 | Pico |
|----------|------|
| VCC      | 3.3V |
| GND      | GND  |
| SCL      | GP9  |
| SDA      | GP8  |

## How It Works

Reads raw accelerometer data from the MPU-6050 over I2C, converts it to m/s² using the 16384 LSB/g sensitivity at ±2g range, computes the vector magnitude, and applies a sliding window moving average filter over the last 20 samples to reduce noise.

## Usage

Flash MicroPython on your Pico, copy `mpu6050_moving_avg.py` to the board, and run it. Output is printed to serial every 50 ms.

```
Filtered G: 9.8231 m/s^2
Filtered G: 9.8214 m/s^2
```

## Dependencies

- MicroPython standard library (`machine`, `math`, `time`)
