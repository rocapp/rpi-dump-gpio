# coding: utf-8
import os
import pigpio
import tabulate
import pandas as pd
import numpy as np
import time
import sys
import click

PINS = (17, 19, 21, 23, 24, 25)


@click.group(invoke_without_command=True)
@click.option('-p', '--pins', default=PINS, type=click.INT, multiple=True,
              help='GPIO pins to monitor.')
def main(pins):
    pi = pigpio.pi()
    print('Initialized PiGPIO instance.')
    
    df = pd.DataFrame(dict(zip(pins, -np.zeros((1,len(pins))))), columns=pins)
    
    def read_pin(p: int):
        return pi.read(int(p))

    input('\n[Press any key to continue...]\n')
    print('Continuously monitoring GPIO values (in 1 sec)...')
    time.sleep(1)
    print('...Go!\n')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        df.iloc[0] = df.iloc[0].apply(lambda el: read_pin(int(el.name)), )
        print(df.T.to_markdown())
        sys.stdout.flush()


if __name__ == '__main__':
    main()

