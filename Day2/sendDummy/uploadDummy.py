import serial
import requests

ser = serial.Serial(
    port='/dev/ttyUSB0',  
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
ser.flush()
if __name__ == '__main__':
    API_ENDPOINT = "http://insecure.benax.rw/iot/"
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            f = open("data.txt", "a")
            data = {"device": "SAUVEJeanLuc",
                    "distance": line}
            res = requests.post(url=API_ENDPOINT, data=data)
            user_input = res.text
            print("User data %s " % user_input)
            f.write(line)
            f.write("\n")
            f.close()
            print(line)