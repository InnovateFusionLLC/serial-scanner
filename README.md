# Serial Killer: Terminal Tracker

## What is This?

Ever wondered which Modbus device is lurking on your `/dev/ttyUSBx` ports? Or which mysterious serial devices are hiding out on your system? Look no further! **Serial Killer: Terminal Tracker** is here to help. With a name as fierce as the tool itself, it slices through the confusion and helps you pinpoint exactly which device is where, faster than a hacker tracks down Wi-Fi at a coffee shop.

This tool is your Sherlock Holmes for serial ports, minus the fancy hat and pipe (unless you're into that).

## Features

- **ASCII Art Banner**: You’re greeted with an epic ASCII art banner proclaiming "Serial Killer: Terminal Tracker" in all its glory, complete with a knife! Because, well... it's serious business (but not too serious).
- **Round-Robin Modbus Scanner**: Enter your desired **TTYUSB** port range and watch it hunt for devices across all ports in round-robin fashion. It's like speed dating, but for serial ports.
- **Serial Monitor Mode**: Not just scanning! You can choose to monitor serial data from a specific port, making it versatile for many use cases.
- **Helpful Error Messages**: If a Modbus device doesn’t respond, don’t worry, the tool will let you know—gently. No judgment here.
- **Interactive Menu**: Choose between scanning for Modbus devices or simply monitoring your serial data, all from a simple menu.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_REPO/serial-killer-terminal-tracker.git
   cd serial-killer-terminal-tracker

2. Install dependencies:
   ```bash
   pip3 install minimalmodbus pyserial
   # or
   pipx install minimalmodbus pyserial

   ```

3. Run the scanner:
   ```bash
   python3 serial_killer.py
   ```

4. How It Works
You'll be greeted with an awesome banner and a menu:
- Choose to scan for Modbus devices.
- Or, monitor a specific serial port.

Enter the port range for scanning or select the port to monitor and let the tool do the rest.

Sit back and watch the magic unfold as it scans through the ports or monitors serial data!

### Example

After running the script and entering your port range or port to monitor, you'
   ```bash
TTTT EEEEE RRRR M M III N N AAAAA L TTTT RRRR AAAAA CCCCC K K EEEEE RRRR ! Serial Killer: Terminal Tracker is here!
Knife (ASCII art) here...

Welcome to Serial Killer: Terminal Tracker!

Scan for Modbus devices
Monitor serial data from a specific port
   ```
Choose your option and start hunting down those devices like a pro!

## Who’s This For?

- **Developers** dealing with mysterious **TTYUSB** devices that just won’t quit.
- **Engineers** who enjoy efficient, automated scanning of Modbus addresses without the hassle.
- **Curious Minds** who wonder, "What *is* plugged into my Pi?"

## License

Feel free to use this tool, tweak it, or just admire the beautiful ASCII art. This project is licensed under the MIT License.
