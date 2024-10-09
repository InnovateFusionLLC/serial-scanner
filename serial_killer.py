import minimalmodbus
import serial
import time
import os

# ASCII Art for "Serial Killer: Terminal Tracker"
banner = [
    "SSSS  EEEEE  RRRR  III  AAAAA  L     K   K III L     L      EEEEE  RRRR  !",
    "S     E      R   R  I   A   A  L     K  K   I  L     L      E      R   R !",
    " SSS  EEEE   RRRR   I   AAAAA  L     KKK    I  L     L      EEEE   RRRR  !",
    "    S E      R  R   I   A   A  L     K  K   I  L     L      E      R  R   ",
    "SSSS  EEEEE  R   R III  A   A  LLLLL K   K III LLLLL LLLLL  EEEEE  R   R !",
    "  ",
    " TTTT  EEEEE  RRRR  M   M  III  N   N   AAAAA  L     TTTT  RRRR   AAAAA  CCCCC K   K EEEEE RRRR  !",
    "   T   E      R   R MM MM   I   NN  N  A   A  L       T    R   R  A   A C      K  K  E     R   R !",
    "   T   EEEE   RRRR  M M M   I   N N N  AAAAA  L       T    RRRR   AAAAA C      KKK   EEEE  RRRR  !",
    "   T   E      R  R  M   M   I   N  NN  A   A  L       T    R  R   A   A C      K  K  E     R  R   ",
    "   T   EEEEE  R   R M   M  III  N   N  A   A  LLLLL   T    R   R  A   A  CCCCC K   K EEEEE R   R !",
    " ",
]

knife = [
     "                                                                                                                                          ",
     "                                                                                                                                          ",
     "                                                          ███                                                                             ",
     "                                                          ████                                                                            ",
     "                                                          ████                                                                            ",
     "    ██████████████████████████████████████████████████████████                                                                            ",
     "   ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████    ",
     "   ███    ██████████   █ ███   █████    █████   █████████   ██████████████████████████████████████████████████████████████████████████    ",
     "  ███     █    ████    █ ███   ██ ██    ████    ██ ███     ███   █ █        █████████████████   █        █    █       ██   ███████████    ",
     "  ███     █   ██ ██    █ ███   ██ ██    ████    ██ ██    █ ███   █ █                           █               ████     █    ███████      ",
     "  ███     █    █ ██    █ ███   ██ ██    ████    ██ ███  █   ██   █ █ ███                       █                     ████  ███████        ",
     "  ███     ██   █ ███   █  ██   █████    █████   █████     █ ██   █ █                                                  ██████████          ",
     "   █████████████████████████████████████████████████████████████ ████████████████████████████████████████████████████████████             ",
     "   ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                 ",
     "                                                          █████████                                                                       ",
     "                                                          ████                                                                            ",
     "                                                           ██                                                                             ",
     "                                                                                                                                          ",
     "                                                                                                                                          ",
     "                                                                                                                                          ",
]

def display_banner():
    """Scroll the ASCII art banner 'Serial Killer: Terminal Tracker' and show the knife."""
    os.system('clear')  # Clear the terminal for a clean start
    for line in banner:
        print(line)
        time.sleep(0.5)  # Delay between each line to simulate scrolling effect
    for line in knife:  # Display the knife ASCII art
        print(line)

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

def serial_monitor(port):
    """Monitor the serial data from the selected port."""
    try:
        ser = serial.Serial(port, 9600, timeout=1)
        print(f"Connected to {port}")

        while True:
            if ser.in_waiting > 0:
                # Read the serial data and print it
                data = ser.readline().decode('utf-8').strip()
                print(f"Data from {port}: {data}")
    except serial.SerialException as e:
        print(f"Error opening {port}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if ser and ser.is_open:
            ser.close()
            print(f"Closed connection to {port}")

def display_menu():
    """Display a menu for the user to choose between scanning and monitoring serial data."""
    print("\nWelcome to Serial Killer: Terminal Tracker!")
    print("1. Scan for Modbus devices")
    print("2. Monitor serial data from a specific port")
    choice = int(input("\nSelect an option (1 or 2): "))
    return choice

def main():
    # Display the scrolling banner
    display_banner()

    # Display the user menu
    choice = display_menu()

    if choice == 1:
        # Get the range of TTYUSB ports from the user and scan for Modbus devices
        ports = get_ttyusb_ports()
        scan_modbus_addresses(ports)
    elif choice == 2:
        # Ask for a specific port and start serial monitoring
        port = input("Enter the port to monitor (e.g., /dev/ttyUSB1): ")
        serial_monitor(port)
    else:
        print("Invalid option. Please restart the program and select 1 or 2.")

if __name__ == "__main__":
    main()