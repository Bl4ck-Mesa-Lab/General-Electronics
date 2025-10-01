#!/bin/bash
#!/bin/sh

RED="\e[31m"
GREEN="\e[32m"
ORANGE="\e[33m"
ENDCOLOR="\e[0m"

failure() {
  local lineno=$1
  local msg=$2
  echo "Failed at $lineno: $msg"
  echo -e "${RED} Error in command, please check above ${ENDCOLOR}"
  echo -e "${RED} Abort... ${ENDCOLOR}"
  exit 1
}

action() {
echo ""
echo -e "[*] --> ${ORANGE} $1 ${ENDCOLOR}"
echo ""
trap 'failure ${LINENO} "$BASH_COMMAND" error ' ERR
$2
sleep 0.5
if [[ $? -eq 0 ]]; then
    echo -e "${GREEN} DONE ${ENDCOLOR}"
fi
}

echo "-----------------------------------"
echo -e "   [*] ${GREEN} ESP_FLASHER PROGRAM ${ENDCOLOR} [*]"
echo "-----------------------------------"

sleep 2
action 'Step 1: Create VENV' 'python3 -m venv ESP_venv'
sleep 1
action 'Step 2: Getin VENV' 'source ESP_venv/bin/activate'
sleep 1
action 'Step 3: Install Packages' 'pip3 install -r requirements.txt'
sleep 1
action 'Step 4: Erase esp32 flash' 'python3 -m esptool --chip esp32 erase_flash'
sleep 1
action 'Step 5: Flashing micropython firmware' 'esptool.py write_flash 0x1000 ESP32_GENERIC-*.bin'
sleep 1
action 'Step 6: Copy main program' 'mpremote connect /dev/ttyUSB0 fs cp main.py :main.py'
sleep 1
action 'Step 7: Reset board' 'mpremote connect /dev/ttyUSB0 reset'
sleep 1
action 'Step 8: Exiting VENV' 'deactivate'
sleep 1

echo ""
echo -e " ${GREEN} ESP32 Setup completed ${ENDCOLOR}"
echo ""
echo "-----------------------------------"
echo -e "     [*] ${GREEN} ESP_FLASHER DONE ${ENDCOLOR} [*]"
echo "-----------------------------------"
