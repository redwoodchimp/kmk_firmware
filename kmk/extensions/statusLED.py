import digitalio

from kmk.extensions import Extension

class statusLED(Extension):
    def __init__(
        self,
        numLockPin=None,
        capsLockPin=None,
        scrollLockPin=None
    ):  
        self.numLockPin = numLockPin
        self.capsLockPin = capsLockPin
        self.scrollLockPin = scrollLockPin

        self.enabled = []
        self.enabledOld = []

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        if self.numLockPin is not None:
            self.numLockLED = digitalio.DigitalInOut(self.numLockPin)
            self.numLockLED.direction = digitalio.Direction.OUTPUT

        if self.capsLockPin is not None:
            self.capsLockLED = digitalio.DigitalInOut(self.capsLockPin)
            self.capsLockLED.direction = digitalio.Direction.OUTPUT

        if self.scrollLockPin is not None:
            self.scrollLockLED = digitalio.DigitalInOut(self.scrollLockPin)
            self.scrollLockLED.direction = digitalio.Direction.OUTPUT
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        if sandbox.last_received_report is not None:
            #First bit is num lock
            #Second is caps lock
            #Third is scroll lock
            
            #I don't think this is ideal but it works
            bits = bin(sandbox.last_received_report[0])[2:]
            byte = '0' * (4 - len(bits)) + bits
            
            self.enabled = [int(byte[i]) == 1 for i in range(4)]

            if self.enabled != self.enabledOld: #only update when something changes
                self.enabledOld = [i for i in self.enabled]

                if self.numLockPin is not None:
                    self.numLockLED.value = self.enabled[3]

                if self.capsLockPin is not None:
                    self.capsLockLED.value = self.enabled[2]

                if self.scrollLockPin is not None:
                    self.scrollLockLED.value = self.enabled[1]            
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return