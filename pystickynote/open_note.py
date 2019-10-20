from pystickynote.paths import NOTES_PATH
import PySimpleGUIQt as g
import sys
import json

if 'darwin' in sys.platform:
    NTB = False
else:
    NTB = True
    
    
def open_note(name, config):
    g.SetOptions(background_color=config.background_color, text_color=config.text_color,
                 input_elements_background_color=config.background_color, input_text_color=config.text_color,
                 button_color=(config.text_color, config.background_color), border_width=config.border_width)
    with open(NOTES_PATH, 'r+') as notes:
        note_obj = json.load(notes)
        match = False
        content = ''
    for k, v in note_obj.items():
        if name == k:
            match = True
            content = v
    if match == False:
        print('No Note Found With That Name')
        exit(1)
    layout = [
        [g.T(name, font=('Arial', 8), justification='center')],
        [g.Multiline(content, size=(50, 5), key='content')],
        [g.B('Close'), g.B('Delete'), g.B('Save')]
    ]
    
    window = g.Window('Create', no_titlebar=NTB, keep_on_top=True, grab_anywhere=True, layout=layout, alpha_channel=float(config.alpha))
    
    while True:
        event, value = window.Read()
        if event == 'Close':
            window.Close()
            break
        elif event == 'Save':
            note_obj[name] = value['content']
            with open(NOTES_PATH, 'r+') as notes:
                notes.seek(0)
                notes.truncate()
                json.dump(note_obj, notes, indent=4)
            window.Close()
            break
        elif event == 'Delete':
            new_layout = [
                [g.T('Are you sure you want to delete {}?'.format(name), justification='center')],
                [g.B('No'), g.B('Yes')]
            ]
            confirm_window = g.Window('', no_titlebar=NTB, keep_on_top=True, grab_anywhere=True, layout=new_layout)
            while True:
                event1, value1 = confirm_window.Read()
                if event1 == 'Yes':
                    note_obj.pop(name, [])
                    with open(NOTES_PATH, 'r+') as notes:
                        notes.seek(0)
                        notes.truncate()
                        json.dump(note_obj, notes, indent=4)
                    confirm_window.Close()
                    break
                else:
                    confirm_window.Close()
                    break
            window.Close()
            break
                
                