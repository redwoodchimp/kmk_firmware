import board
from busio import I2C

from bytearrays import arrays as frames

from kmk.extensions.oled import OLED
from kmk.extensions.boardLED import boardLED
from kmk.extensions.statusLED import statusLED
from kmk.modules.layers import Layers
from kmk.keys import KC

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    #Raspberry Pi Pico based keyboard
    col_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22)
    row_pins = (board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = I2C(scl=board.GP1, sda=board.GP0)
    ledPin = board.GP25 #This is the on board led
    capsLedPin = board.GP28
    powersave_pin = board.GP23


keyboard  = KMKKeyboard()
oledanimation = frames()
layers_ext = Layers()
statusLED_ext = statusLED(capsLedPin=keyboard.capsLedPin)
boardLED_ext = boardLED(keyboard.ledPin)

_______ = KC.TRNS
xxxxxxx = KC.NO
LOWER = KC.MO(1)

keyboard.keymap = [ #pi75 - Keymap
    [   #Main
        KC.ESC, KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.PSCR, KC.MPLY,
        KC.GRV, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,KC.EQL, KC.BSPC, KC.DEL, 
        KC.TAB, KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,KC.RBRC,KC.BSLS, KC.HOME,
        KC.CAPS,KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,xxxxxxx,KC.ENT,  KC.PGUP,
        KC.LSFT,KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.RSFT,xxxxxxx,KC.UP,   KC.PGDN,
        KC.LCTL,KC.LWIN,KC.LALT,xxxxxxx,xxxxxxx,xxxxxxx,KC.SPC, xxxxxxx,xxxxxxx,KC.RALT,LOWER,  KC.LEFT,xxxxxxx,KC.DOWN, KC.RGHT,
    ],
    [   #Extra keys
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,xxxxxxx,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,xxxxxxx,_______,_______,
        _______,_______,_______,xxxxxxx,xxxxxxx,xxxxxxx,_______,xxxxxxx,xxxxxxx,_______,_______,KC.MPRV,xxxxxxx,KC.MPLY,KC.MNXT,
    ],
    '''
    [   #Unused/blank
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,xxxxxxx,_______,_______,
        _______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,_______,xxxxxxx,_______,_______,
        _______,_______,_______,xxxxxxx,xxxxxxx,xxxxxxx,_______,xxxxxxx,xxxxxxx,_______,_______,_______,xxxxxxx,_______,_______,
    ],
    '''
]

oled_ext = OLED(i2c=keyboard.i2c, frames=oledanimation.borpa2, enableText=True)

keyboard.extensions = [oled_ext, layers_ext, boardLED_ext, statusLED_ext]

if __name__ == '__main__':
    keyboard.go()