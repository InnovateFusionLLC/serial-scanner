import minimalmodbus
import serial
import time
import os

# ASCII Art for "TTY SCANNER!"
banner = [
    "TTTT  TTTT  Y   Y       SSS  CCCCC  AAAAA  N   N  N   N  EEEEE  RRRR  !",
    "  T     T    Y Y       S     C      A   A  NN  N  NN  N  E      R   R !",
    "  T     T     Y         SSS  C      AAAAA  N N N  N N N  EEEE   RRRR  !",
    "  T     T     Y            S C      A   A  N  NN  N  NN  E      R  R   ",
    "  T     T     Y         SSS   CCCCC A   A  N   N  N   N  EEEEE  R   R !",
]

def display_banner():
    """Scroll the ASCII art banner 'TTY SCANNER!' at the start of the script."""
    os.system('clear')  # Clear the terminal for a clean start
    for line in banner:
        print(line)
        time.sleep(0.5)  # Delay between each line to simulate scrolling effect

def get_ttyusb_ports():
    """Prompt the user to enter the range of TTYUSB ports."""
    start_port = int(input("Enter the starting TTYUSB port number (e.g., 0 for /dev/ttyUSB0): "))
    end_port = int(input("Enter the ending TTYUSB port number (e.g., 3 for /dev/ttyUSB3): "))
    
    # Generate the list of TTY ports based on the user input
    ports = [f"/dev/ttyUSB{i}" for i in range(start_port, end_port + 1)]
    print(f"\nScanning on the following ports: {ports}")
    return ports

def scan_address_on_port(port, address):
    """Scan a specific Modbus address on a given serial port."""
    try:
        instrument = minimalmodbus.Instrument(port, address)  # Create instrument for each address
        instrument.serial.baudrate = 9600  # Set baud rate
        instrument.serial.bytesize = 8  # Set data bits
        instrument.serial.parity = minimalmodbus.serial.PARITY_NONE  # No parity
        instrument.serial.stopbits = 2  # Set stop bits
        instrument.serial.timeout = 1  # Set timeout for response

        # Try to read a register to check if the device at this address responds
        voltage = instrument.read_register(0x0000, number_of_decimals=2, functioncode=4)
        print(f"Modbus device found on {port} at address {address}: Voltage = {voltage} V")
        return True  # Device found
    except minimalmodbus.NoResponseError:
        print(f"Address {address} on {port}: No response")
    except minimalmodbus.SlaveReportedException as e:
        print(f"Address {address} on {port}: Slave reported error - {e}")
    except Exception as e:
        print(f"Address {address} on {port}: Error - {e}")
    return False  # No device found

def scan_modbus_addresses(ports):
    """Scan through all addresses across all ports in a round-robin order."""
    START_ADDRESS = 1  # Starting Modbus address to scan
    END_ADDRESS = 247  # Ending Modbus address (Modbus devices typically support addresses up to 247)

    for address in range(START_ADDRESS, END_ADDRESS + 1):
        print(f"\n--- Scanning Modbus Address {address} ---")
        for port in ports:
            try:
                found = scan_address_on_port(port, address)
                if found:
                    print(f"Device found at {port} with address {address}.")
            except serial.SerialException as e:
                print(f"Failed to open {port}: {e}")

def main():
    # Display the scrolling banner
    display_banner()

    # Get the range of TTYUSB ports from the user
    ports = get_ttyusb_ports()

    # Start the scanning process across all addresses and ports
    scan_modbus_addresses(ports)

if __name__ == "__main__":
    main()
