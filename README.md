# Python timer
Stupid simple timer in python. Makes a dialog box when time is up. 

# Usage

### Single timer:
```
python timer.py <time in minutes>
```

### Sequence timer (loops through a sequence of different time intervals):

Condensed reference:
```
python sequence_timer.py t_0 t_f N [ag]
```
Expanded:
```
python sequence_timer.py <initial time in minutes> <final time in minutes> \
  <number of different times> <a for arithmetic series, g for geometric series>
```

# Examples

Time 30 seconds, then create a dialog box:
```
python timer.py 0.5
```

Time 1 minute, 1/2 a minute, 1/4 of a minute, 1/8 of a minute, and repeat, creating a dialog box at each time:
```
python sequence_timer.py 1 0.125 4 g
```

Time 30 seconds, 20 seconds, 10 seconds, and repeat, creating a dialog box at each time:
```
python sequence_timer.py 0.5 0.17 3 a
```
