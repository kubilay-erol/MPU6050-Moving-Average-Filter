# MPU6050 Static Test - Data Analysis
# Date: February 11, 2026
# Author: Kubilay Erol

## Test Conditions
- Sensor: MPU6050
- Microcontroller: ESP32 SuperMini
- State: Static (sensor sitting flat on breadboard)
- Duration: ~5 seconds
- Samples: 93
- Filter: Moving Average (window size = 20)

## Statistical Summary
| Parameter           | Value         |
|---------------------|---------------|
| Standard Gravity    | 9.8067 m/s^2  |
| Measured Mean       | 9.9663 m/s^2  |
| Noise (Std Dev)     | ±0.0078 m/s^2 |
| Sensor Bias         | +0.1596 m/s^2 |
| Error               | 1.63%         |

## Observations
- The moving average filter successfully removed high-frequency noise.
- A consistent systematic error of 1.63% was observed.
- The sensor reported ~9.96 m/s^2 instead of the expected 9.81 m/s^2.
- This is attributed to Zero-G Offset, a common manufacturing bias in MEMS sensors.

## Notes
- For calibrated measurements, subtract the 0.16 m/s^2 offset in code.
- Noise level of ±0.0078 m/s^2 is very low, confirming filter effectiveness.
