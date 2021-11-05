###
MAX7219 8x8 led with raspberry pi -spi interface in python code
###
import time
import spidev

# We only have SPI bus 0 available to us on the Pi


#Device is the chip select pin. Set to 0 or 1, depending on the connections


# Enable SPI


# Open a connection to a specific bus and device (chip select pin)


# Set SPI speed and mode



class sendmsg():

    def __init__(self):
        bus = 0
        device = 0
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 500000
        self.spi.mode = 0

        
    def sendspi(self,msb,lsb):
#            msg = [0x0f,0xff]
            msg = [msb,lsb]
            self.spi.xfer2(msg)
            time.sleep(1)
    def interruptHandler(self):
            msg = [0x0f,0xff]
            self.spi.xfer2(msg)



if __name__ == '__main__':
    
    spitransfer = sendmsg()
    spitransfer.sendspi(0x0f,0xff)       #display test on
    spitransfer.sendspi(0x0f,0x00)       #display test off
    spitransfer.sendspi(0x0c,0x01)       #shutdown off
    spitransfer.sendspi(0x0b,0x07)       #scan limit
    spitransfer.sendspi(0x0a,0x0f)       #intensity   
    spitransfer.sendspi(0x01,0x00)       #D1 - D8
    spitransfer.sendspi(0x02,0x81)
    spitransfer.sendspi(0x03,0x42)
    spitransfer.sendspi(0x04,0x3c)
    spitransfer.sendspi(0x05,0xe7)
    spitransfer.sendspi(0x06,0x18)
    spitransfer.sendspi(0x07,0x00)
    spitransfer.sendspi(0x08,0xff)

