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
    
    df = pd.DataFrame(np.zeros((1,len(pins))), columns=pins)
    
    def read_pin(p: int):
        return pi.read(int(p))

    input('[Press any key to continue...]')
    print('Continuously monitoring GPIO values...')
    time.sleep(1)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        df = df.apply(lambda el: read_pin(int(el.column)), )
        print(df.to_markdown())
        sys.stdout.flush()


if __name__ == '__main__':
    main()

