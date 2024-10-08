# usb-scanner
Quick and easy USB / TTY scanner tool.

# TTY Scanner!

## What is This?

Ever wondered which Modbus device is hiding on your `/dev/ttyUSBx` ports? Fear not! The **TTY Scanner!** is here to track them down faster than a hacker tracks down Wi-Fi signals at a coffee shop.

This modest (but mighty) tool will comb through all the **TTYUSB** ports you throw at it and hunt for those elusive Modbus devices, one address at a time, one port at a time. It’s like Sherlock Holmes for your serial devices... except without the funny hat.

## Features

- **ASCII Art Banner**: Greets you with an epic "TTY SCANNER!" banner made from the finest ASCII characters known to humans. It scrolls to let you know this is serious business (but not *too* serious).
- **Port Detective**: Enter your desired **TTYUSB** port range, and this tool will sniff them out, scanning each port in round-robin fashion across Modbus addresses like it’s nobody's business.
- **Error Messages That Won’t Judge You**: If a Modbus device doesn’t respond, this tool will gently let you know. Maybe they’re just not in the mood. Or, you know... unplugged.
- **Humans, Not Robots**: Scans through **TTYUSB** ports, because there’s no fun in manually checking each one. We’ve automated the tedium so you can focus on more important things, like making coffee.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_REPO/tty-scanner.git
   cd tty-scanner
   ```

2. Install dependencies:
   ```bash
   pip3 install minimalmodbus pyserial
   ```

3. Run the scanner:
   ```bash
   python3 modbus_scanner.py
   ```

4. Enter your **TTYUSB** port range, sit back, and let **TTY Scanner!** do the rest!

## How It Works

1. **Banner Flash**: You’ll be greeted by a spectacular **TTY SCANNER!** ASCII banner that scrolls down your terminal in true hacker movie fashion.
2. **Modbus Madness**: After you wipe the awe-struck look off your face, you’ll input the range of **TTYUSB** ports to scan. Watch in amazement as this script hunts down Modbus devices like a bloodhound.
3. **The Results**: For every Modbus device it finds, you’ll get a detailed report on which address it responded to, and from which port it was found. You can’t hide, Modbus!

## Who’s This For?

- **Developers** dealing with mysterious **TTYUSB** devices that just won’t quit.
- **Engineers** who enjoy efficient, automated scanning of Modbus addresses without the hassle.
- **Curious Minds** who wonder, "What *is* plugged into my Pi?"

## License

Feel free to use this tool, tweak it, or just admire the beautiful ASCII art. This project is licensed under the MIT License.
