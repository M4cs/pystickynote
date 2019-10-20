from pystickynote.paths import NOTES_PATH
import PySimpleGUIQt as g
import sys
import json

if 'darwin' in sys.platform:
    NTB = False
else:
    NTB = True

def create_note(name, config):
    g.SetOptions(background_color=config.background_color, text_color=config.text_color,
                 input_elements_background_color=config.background_color, input_text_color=config.text_color,
                 button_color=(config.text_color, config.background_color), border_width=config.border_width)
    layout = [
        [g.T('Create Note', font=('Arial', 8), justification='center')],
        [g.Multiline('', size=(50, 5), key='content')],
        [g.B('Close'), g.B('Save')]
    ]
    window = g.Window('Create', no_titlebar=NTB, keep_on_top=True, grab_anywhere=True, layout=layout, alpha_channel=float(config.alpha))
    while True:
        event, value = window.Read()
        if event == 'Close':
            window.Close()
            break
        elif event == 'Save':
            with open(NOTES_PATH, 'r+') as notes:
                note_obj = json.load(notes)
                note_obj.update({
                    name: value['content']
                })
                notes.seek(0)
                notes.truncate()
                json.dump(note_obj, notes, indent=4)
            window.Close()
            break