import keyboard
pressed = []
def print_pressed_keys(e):
    if flag:
        if e.name == 'enter' and len(pressed) < 3:
            pass
        elif e.name == 'backspace' and len(pressed) > 0 and e.event_type == 'down':
            print('Delete:' + pressed[len(pressed)-1])
            pressed.pop()
            if len(pressed) > 0:
                for i in pressed:
                    print(i.upper())
            return

        if e.name not in pressed and e.event_type == 'down' and e.name != 'backspace':
            pressed.append(e.name)
            if len(pressed) < 4:
                print(e.name.upper())
            elif e.name != 'enter':
                pressed.clear()
                print('Enter a new combination of three keys')


flag = True
hotkey = ''
try:
    with open('ht.in','r') as f:
        hotkey = f.readline()
        print(hotkey)
        flag = False
except FileNotFoundError:
    pass

while flag:
    pressed.clear()
    print('Enter combination of three keys.\nPress Enter when the combination is complete.\nPress Backspace if you want to remove the last key from the combination.')
    keyboard.hook(print_pressed_keys)
    keyboard.wait('enter')
    pressed.pop()
    print(pressed)
    if len(pressed) == 3:
        flag = False
        with open('ht.in', 'w') as f:
            hotkey = ' + '.join(pressed)
            f.write(hotkey)
keyboard.unhook_all()

import sys,os
cdir = os.getcwd()
os.startfile(cdir + '\\tr.exe')
