# pystickynote

Stickynotes for your desktop easily from the command line! Built using [PySimpleGUI](http://pysimplegui.com)

# How does it work?

Pystickynote creates a small QT window for you to jot your ideas down and then display them later on all with a command line tool. On top of that, the note itself is fully customizable allowing you to change colors, alpha, and borders.

# Installation

```
pip3 install pystickynote
```

# Running It

```
pystickynote create <name_of_note> # Displays stickynote window

pystickynote open <name_of_note> # Displays old stickynote
```

# Configuration

Config files and notes can be found in `~/.config/pystickynote/`. Inside this folder you will find `pysn.conf` and `notes.json`. The config file looks something like this:

```
[DEFAULT]
background_color = #454545
text_color = #fafafa
alpha = 0.8
border_width = 0
font_size = 10
title_size = 8
```

`background_color` = the background hex color for the note

`text_color` = the text color for the note

`alpha` = the note window's alpha

`border_width` = border around input box and buttons

`font_size` = font size for text

`title_size` = font size for title


