"""
Get the serial number associated with a Raspberry Pi in a mildly kludge-y way.
"""


def main():
    try:
        for line in open('/proc/cpuinfo', 'r').readlines():
            if line[0:6] == "Serial":
                return line[10:].strip()
    except Exception as e:
        raise(e)

if __name__ == "__main__":
    print(main())

