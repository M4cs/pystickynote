# pystickynote

Stickynotes for your desktop easily from the command line! Built using [PySimpleGUI](http://pysimplegui.com)

# Preview

<p align="center">
  <a><img src="https://github.com/M4cs/pystickynote/blob/master/preview.png?raw=true"></a>
</p>

# How does it work?

Pystickynote creates a small QT window for you to jot your ideas down and then display them later on all with a command line tool. On top of that, the note itself is fully customizable allowing you to change colors, alpha, and borders.

# Installation

```
pip3 install pystickynote
```

# Running It

```
<pystickynote/pysn> create <name_of_note> # Displays stickynote window

<pystickynote/pysn> open <name_of_note> # Displays old stickynote

<pystickynote/pysn> delete <name_of_note> # Deletes stickynote

<pystickynote/pysn> list # Displays all notes
```

# Changelog

### Update 1.5.1:

- Added box_height and box_width values to config

### Update 1.5:

- Added new entry point: `pysn`

- Added delete function thanks to @synackray

- Fixed error with mouse_offset (possibly still buggy)

- New local version of PySimpleGUIQt for that ^

# Configuration

Config files and notes can be found in `~/.config/pystickynote/`. Inside this folder you will find `pysn.conf` and `notes.json`.

You can also find the default config and notes file in this repository.

The config file looks something like this:

```
[DEFAULT]
background_color = #454545
text_color = #fafafa
alpha = 0.8
border_width = 0
title_size = 8
font_size = 10
box_height = 5
box_width = 50
```

`background_color` = the background hex color for the note

`text_color` = the text color for the note

`alpha` = the note window's alpha

`border_width` = border around input box and buttons

`font_size` = font size for text

`title_size` = font size for title

`box_height` = height of box

`box_width` = width of box


