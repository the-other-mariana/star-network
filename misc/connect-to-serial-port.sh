sudo apt install setserial # UART: unknown means no device 
sudo setserial -g /dev/ttyS[0123456789]
sudo apt install cu
sudo chmod 666 /dev/ttyS0
sudo cu -l /dev/ttyS0 -s 115200 # out: Connected
~. # disconnect