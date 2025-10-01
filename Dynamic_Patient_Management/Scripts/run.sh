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
echo -e "   [*] ${GREEN} RUN ESP PROGRAM ${ENDCOLOR} [*]"
echo "-----------------------------------"

sleep 2
action 'Step 1: Getin VENV' 'source ESP_venv/bin/activate'
sleep 1
action 'Step 1: Starting program' 'mpremote connect /dev/ttyUSB0 run main.py'
sleep 1
