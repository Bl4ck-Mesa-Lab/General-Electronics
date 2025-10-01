# Embedded Diving Sensors

## Desciption: 

This project contains all informations about design and coding of esp to simulate Dynamic patient management

## Equipments used: 

- ESP32 LOLIN32
- OLED Screen SSD160

## Softwares used: 

- Thonny Pyhton : https://thonny.org/
- Frizting : https://fritzing.org/
- Python
- Bash

## Usage 💻

```bash
chmod a+x flashing.sh run.sh
```
Connect the ESP32 to the computer via USB, then verify that it is detected.

```bash
ls /dev/tty*
``` 

and verify that it is present by checking that `/dev/ttyUSB0` exists (or `/dev/ttyACM0` depending on the chip used by the ESP32), then launch the program.

```bash
./flashing.sh
```

If the `flashing.sh` program finishes without errors and displays `ESP_FLASHER DONE`, launch the `main.py` program by executing the following command

```bash
./run.sh
```

But you can use thonny instead.

## Design POC: 

<img src="https://github.com/Bl4ck-Mesa-Lab/General-Electronics/blob/main/Pictures/Example.png"/>
