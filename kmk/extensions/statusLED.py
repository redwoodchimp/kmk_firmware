import digitalio

from kmk.extensions import Extension

class statusLED(Extension):
    def __init__(
        self,
        capsLedPin=None
    ):
        self.capsLedPin = capsLedPin

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        if self.capsLedPin is not None:
            self.capsLed = digitalio.DigitalInOut(self.capsLedPin)
            self.capsLed.direction = digitalio.Direction.OUTPUT
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        if sandbox.last_received_report is not None:
            #This should only check the bit that corresponds to each key, for caps I beleive it is the second bit
            if sandbox.last_received_report == b'\x01' and self.capsLed.value:
                self.capsLed.value = False
            elif sandbox.last_received_report == b'\x03'and not self.capsLed.value:
                self.capsLed.value = True
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return