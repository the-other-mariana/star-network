sudo apt install setserial # UART: unknown means no device 
sudo setserial -g /dev/ttyS[0123456789] # list tty devices
dmesg | grep tty # list tty devices
sudo apt install cu
sudo chmod 666 /dev/ttyS0 # if cu command outputs: Line in use
sudo cu -l /dev/ttyS0 -s 115200 # out: Connected
~. # disconnect