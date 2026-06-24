#mPythonType:0
#mPythonType:0
#mPythonType:0

from mpython import *
from decoder import decode
import music
import time

f_index = [196, 262, 294, 330, 349, 370, 392, 440, 494, 523, 587, 659, 698, 784, 880, 0]
codein = ''
decoded = []
times = 0
ct = time.time()
mode = 0
mode_note = ['']
info=''
predata = []

def preload():
    global mode_note, predata
    with open('pre_encoded.txt', 'r') as f:
        pre_encoded = eval(f.read())
    for it in list(pre_encoded.keys()):
        mode_note.append(it)
    for jt in list(pre_encoded.values()):
        predata.append(jt)

def oled_show():
    global codein, info, mode, mode_note
    oled.fill(0)
    oled.DispChar(codein[-18:], 0, 0, 1)
    oled.DispChar(info, 0, 16, 1)
    oled.DispChar('MODE '+str(mode)+' '+mode_note[mode], 0, 48, 1)
    oled.show()


def on_touchpad_p_pressed(_):
    global codein
    codein += '0'

touchpad_p.event_pressed = on_touchpad_p_pressed

def on_touchpad_y_pressed(_):
    global codein
    codein += '1'

touchpad_y.event_pressed = on_touchpad_y_pressed

def on_touchpad_h_pressed(_):
    global codein, times, ct, info
    if time.time() - ct > 1.0:
        times = 0
    else:
        times += 1
    ct = time.time()
    if times >= 8:
        codein = ''
        times = 0
        info = 'clear done'
        oled_show()
        time.sleep(1)
        info = ''

touchpad_h.event_pressed = on_touchpad_h_pressed

def on_touchpad_o_pressed(_):
    global mode, mode_note
    mode = (mode+1)%len(mode_note)

touchpad_o.event_pressed = on_touchpad_o_pressed

def on_touchpad_n_pressed(_):
    global codein
    codein = codein[:-1]

touchpad_n.event_pressed = on_touchpad_n_pressed


def on_button_a_pressed(_):
    global decoded, codein, info
    decoded = decode(codein, 1)
    info = 'decoded successfully'
    oled_show()
    time.sleep(1)
    info = ''

button_a.event_pressed = on_button_a_pressed

def on_button_b_pressed(_):
    global decoded, f_index, mode, predata, info, predata
    player = []
    if mode == 0:
        player = decoded[:]
    else:
        player = predata[mode-1][:]
    if player:
        bpm = player.pop()
        pb = 15000/bpm
        info = 'playing'
        oled_show()
        for item in player:
            music.pitch(f_index[item[0]], int(pb*item[1]))
        info = ''

button_b.event_pressed = on_button_b_pressed


preload()
while True:
    oled_show()


