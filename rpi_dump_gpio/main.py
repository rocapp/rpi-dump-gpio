# coding: utf-8
import pigpio
import tabulate
import pandas as pd
import numpy as np

PORTS = (17, 19, 21, 23, 24, 25)


def main():
    pi = pigpio.pi()
    df = pd.DataFrame(np.zeros((1,len(PORTS))), columns=PORTS)
    def read_pin(p: int):
        return pi.read(int(p))
    
    while True:
        df = df.apply(lambda el: read_pin(int(el.column)), axis=1)
        print(df.to_markdown())


if __name__ == '__main__':
    main()

