#!/usr/bin/python3
"""Tshark processing prototype."""
import argparse


def process_tcpdump(lines, tags):
    """Read stdin tcpdump json and call the print function to convert it to influxdb protocol."""

    for line in lines:
        if ": " in line:
            for tag in tags:
                # process line with format: "tcp.srcport": "34224",
                key_value = line.split(": ")
                key = key_value[0].strip()
                value = key_value[1].strip()

                if tag in key:
                    key = key.split(".")[1]
                    # output is in influx line protocol
                    print(f'tshark,{key[:-1]}={value[1:-2]} {key[:-1]}="{value[1:-2]}"')


def main():
    """Main entrypoint for script execution."""

    ####
    # Set argparse and argparse arguments
    ####
    parser = argparse.ArgumentParser(description="Tcpdump processor prototype")
    parser.add_argument("-t", "--tags", nargs="+", type=str, help="List of tag keys.")
    args = parser.parse_args()

    with open("/usr/local/sbin/tshark.json", "r") as tshark_file:
        lines = tshark_file.readlines()
        process_tcpdump(lines, args.tags)

    # while True: # real time file streaming
    #     # read last line of file
    #     line = tshark_file.readline()  # sleep if file hasn't been updated
    #     if not line:
    #         time.sleep(0.1)
    #         continue
    #     elif ": " in line:
    #         for value in args.filter:
    #             read_process_tcpdump(value, line)


if __name__ == "__main__":
    main()
