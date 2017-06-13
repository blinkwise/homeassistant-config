"""this is only for testing."""
import logging
import sys
import time

from pylutron_caseta.smartbridge import Smartbridge
root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)


if __name__ == '__main__':
    sb = Smartbridge(hostname="192.168.86.101")
    print(sb.get_devices())
    time.sleep(5)
    sb.turn_on("7")
    time.sleep(5)
    sb.turn_off("7")
    time.sleep(5)