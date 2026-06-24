#mPythonType:0
#mPythonType:0
#mPythonType:0

from mpython import *
from decoder import decode
import music
import time

f_index = [196, 262, 294, 330, 349, 370, 392, 440, 494, 523, 587, 659, 698, 784, 880]
codein = ''
decoded = []
bpm = None
pb=0
times = 0
ct = time.time()
mode = 0
mode_note = ['']
info=''
pre_encoded = {}
predata = []

def preload():
    global pre_encoded, mode, mode_note, predata
    with open('pre_encoded.txt', 'r') as f:
        pre_encoded = eval(f.read())
    for it in list(pre_encoded.keys()):
        mode_note.append(it)
    for jt in list(pre_encoded.values()):
        predata.append(jt)


def on_touchpad_p_pressed(_):
    global bpm, item, decoded, f_index, codein
    codein = str(codein) + str('0')

touchpad_p.event_pressed = on_touchpad_p_pressed

def on_touchpad_y_pressed(_):
    global bpm, item, decoded, f_index, codein
    codein = str(codein) + str('1')

touchpad_y.event_pressed = on_touchpad_y_pressed

def on_touchpad_h_pressed(_):
    global bpm, item, decoded, f_index, codein, times, ct, mode, mode_note
    if time.time() - ct > 1.0:
        times = 0
    else:
        times += 1
    ct = time.time()
    if times >= 8:
        codein = ''
        times = 0
        info = 'clear done'
        oled.fill(0)
        oled.DispChar(str(codein)[-18:], 0, 0, 1)
        oled.DispChar(info, 0, 16, 1)
        oled.DispChar('MODE '+str(mode)+mode_note[mode], 0, 48, 1)
        oled.show()
        time.sleep(1)
        info = ''

touchpad_h.event_pressed = on_touchpad_h_pressed

def on_touchpad_o_pressed(_):
    global bpm, item, decoded, f_index, codein, mode
    mode = (mode+1)%2

touchpad_o.event_pressed = on_touchpad_o_pressed

def on_touchpad_n_pressed(_):
    global bpm, item, decoded, f_index, codein
    codein = codein[:-1]

touchpad_n.event_pressed = on_touchpad_n_pressed


def on_button_a_pressed(_):
    global bpm, item, decoded, f_index, codein, pb, info, mode, mode_note
    decoded = decode(codein, 1)
    info = 'decoded successfully'
    oled.fill(0)
    oled.DispChar(str(codein)[-18:], 0, 0, 1)
    oled.DispChar(info, 0, 16, 1)
    oled.DispChar('MODE '+str(mode)+mode_note[mode], 0, 48, 1)
    oled.show()
    time.sleep(1)
    info = ''

button_a.event_pressed = on_button_a_pressed

def on_button_b_pressed(_):
    global bpm, item, decoded, f_index, codein, mode, mode_note, predata
    player = []
    if mode == 0:
        player = decoded
    else:
        player = predata[mode-1]
    bpm = player[-1]
    pb = 15000/bpm
    player.pop()
    info = 'playing'
    oled.fill(0)
    oled.DispChar(str(codein)[-18:], 0, 0, 1)
    oled.DispChar(info, 0, 16, 1)
    oled.DispChar('MODE '+str(mode)+mode_note[mode], 0, 48, 1)
    oled.show()
    for item in player:
        if item[0] <= 14:
            music.pitch(f_index[item[0]], int(pb*item[1]))
        elif item[0] ==15:
            music.pitch(0, int(pb*item[1]))
    info = ''

button_b.event_pressed = on_button_b_pressed


preload()
while True:
    oled.fill(0)
    oled.DispChar(str(codein)[-18:], 0, 0, 1)
    oled.DispChar(info, 0, 32, 1)
    oled.DispChar('MODE '+str(mode)+mode_note[mode], 0, 48, 1)
    oled.show()


