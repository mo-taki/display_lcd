import mh_z19
import time
import timeout_decorator
import drivers
import locale
from time import sleep
from datetime import datetime

@timeout_decorator.timeout(10)
def get_sensor_info():
    value = ""
    while value == "":
        value = mh_z19.read_all()

    return value

if __name__ == '__main__':
    locale.setlocale(locale.LC_TIME, 'C.UTF-8')
    display = drivers.Lcd()

    while True:
        sensor_info = get_sensor_info()
        co2 = sensor_info['co2']
        temp = sensor_info['temperature'] - 1 # MEMO: なんかずれるから1度引く

        now = datetime.now()
        lcd_string1 = str(now.strftime('%m/%d%a%H:%M:%S'))
        lcd_string2 = 'CO2:{} TEMP:{}{}'.format(co2, temp, chr(0xDF))

        display.lcd_display_string(lcd_string1, 1)
        display.lcd_display_string(lcd_string2, 2)
        sleep(1)
