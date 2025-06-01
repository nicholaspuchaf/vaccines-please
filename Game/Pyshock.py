import serial
import serial.tools.list_ports
import time

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None

port = find_arduino_port()
if port is not None:
    ser = serial.Serial(port=port, baudrate=9600, timeout=1)
else:
    raise Exception("No Arduino found")

def shock():
    ser.write(b's')
    time.sleep(1)
    #time.sleep(1)
    ser.write(b'0')

def main():
    if not port:
        print("❌ Arduino not found. Make sure it's connected.")
        return

    print(f"✅ Arduino found on {port}")

    time.sleep(2)  # Wait for Arduino to reset

    print("🔁 Turning LED ON")
    ser.write(b's')
    time.sleep(10)

    print("🔁 Turning LED OFF")
    ser.write(b'0')

    ser.close()
    print("✅ Done.")

if __name__ == "__main__":
    main()
