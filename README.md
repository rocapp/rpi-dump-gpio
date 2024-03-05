# rpi-dump-gpio

Script to dump raspberry pi gpio values.

## Installation

```bash
    $ poetry install
```

## Usage

### CLI

```bash
    $ rpi-dump-gpio --help
Usage: rpi-dump-gpio [OPTIONS] COMMAND [ARGS]...

Options:
-p, --pins INTEGER  GPIO pins to monitor.
--help              Show this message and exit.
```

```bash
    $ rpi-dump-gpio --p 17 -p 19 -p 21 -p 23 -p 24 -p 25
```