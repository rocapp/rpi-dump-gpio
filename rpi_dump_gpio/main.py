# coding: utf-8
import os
import pigpio
import tabulate
import pandas as pd
import numpy as np
import time
import sys
import click
from dotenv import load_dotenv, find_dotenv

loaded_env = load_dotenv(find_dotenv(), override=True)

PIGPIO_HOST = os.getenv('PIGPIO_HOST', 'localhost')

PINS = (17, 19, 21, 23, 24, 25)


@click.group(invoke_without_command=True)
@click.option('-p', '--pins', default=PINS, type=click.INT, multiple=True,
              help='GPIO pins to monitor.')
@click.option('-H', '--host', default=PIGPIO_HOST, type=click.STRING,
              help='Raspberry Pi Host IP.')
@click.option('-P', '--port', default=8888, type=click.INT, help='Raspberry Pi Port.')
def main(pins, host, port):
    print(f'Starting rpi-dump-gpio (at {host}:{port})...')
    pi = pigpio.pi(host=host, port=port)
    print('Initialized PiGPIO instance on {}:{}.'.format(
        host, port) if pi.connected else 'Failed to connect.')

    if not pi.connected:
        exit(1)

    if not pins:
        exit(0)

    df = pd.DataFrame([len(pins) * [-0.0, ]], columns=pins)

    def read_pin(p: int):
        return pi.read(int(p))

    input('\n[Press any key to continue...]\n')
    print('Continuously monitoring GPIO values (in 1 sec)...')
    time.sleep(1)
    print('...Go!\n')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        df = df.apply(lambda el: read_pin(int(el.name)))
        print(df.to_markdown())
        sys.stdout.flush()


if __name__ == '__main__':
    main()
