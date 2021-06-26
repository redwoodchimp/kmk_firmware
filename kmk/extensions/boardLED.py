import board
import digitalio

from kmk.extensions import Extension

class boardLED(Extension):
    def __init__(
        self,
        ledPin
    ):
        self.ledPin = ledPin

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        self.led = digitalio.DigitalInOut(self.ledPin)
        self.led.direction = digitalio.Direction.OUTPUT
        self.led.value = True
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        self.led.value = False
        return

    def on_powersave_disable(self, sandbox):
        self.led.value = True
        return