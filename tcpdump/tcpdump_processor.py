#!/usr/bin/python3
"""Metrics utility for reporting IoT measurements."""
import argparse
import sys
import os
import time


def read_process_tcpdump(filter_key, line, epoch):
    """Read stdin tcpdump json and call the print function to convert it to influxdb protocol."""

    key_value = line.split(": ")
    key = key_value[0].strip()
    value = key_value[1].strip()

    if filter_key in key:
        key = key.split(".")[1]
        print(f"tshark,{key[:-1]}={value[1:-2]} {key[:-1]}={value[1:-2]}")


def main():
    """Main entrypoint for script execution."""

    ####
    # Set argparse and argparse arguments
    ####
    parser = argparse.ArgumentParser(description="Tcpdump processor prototype")
    parser.add_argument("-t", "--tag", nargs="+", type=str, help="List of filter keys.")
    parser.add_argument(
        "-f", "--field", nargs="+", type=str, help="List of filter keys."
    )
    args = parser.parse_args()

    # tshark_file = open("./tshark.log", "r")

    with open("/usr/local/sbin/tshark.log", "r") as tshark_file:
        lines = tshark_file.readlines()
        for line in lines:
            if ": " in line:
                for value in args.tag:
                    read_process_tcpdump(value, line)

    # while True:
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
