# Python timer
Stupid simple timer in python. Makes a dialog box when time is up. 
To use, execute script with a single argument specifying the number (integer) of minutes. Can also suggest a float less than one for timing a fraction of a minute.

# Usage

Single timer:
```bash
python timer.py <time in minutes>
```

Sequence timer (loops through a sequence of different time intervals):
```bash
python sequence_timer.py <initial time in minutes> <final time in minutes> \
  <number of different times> <a for arithmetic series, g for geometric series>
```

For example:

Time 30 seconds, then create a dialog box:
```bash
python timer.py 0.5
```

Time 1 minute, 1/2 a minute, 1/4 of a minute, 1/8 of a minute, and repeat, creating a dialog box at each time:
```bash
python sequence_timer.py 1 0.125 3 g
```

Time 30 seconds, 20 seconds, 10 seconds, and repeat, creating a dialog box at each time:
```bash
python sequence_timer.py 0.5 0.17 3 a
```
