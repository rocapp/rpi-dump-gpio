# coding: utf-8
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

    def read_pins():
        df = df.apply(lambda el: read_pin(int(el.column)), )
        return df

    input('[Press any key to continue...]')
    print('Continuously monitoring GPIO values...')
    time.sleep(1)
    while True:
        df = read_pins()
        print(df.to_markdown())


if __name__ == '__main__':
    main()

