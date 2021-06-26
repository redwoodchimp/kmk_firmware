from adafruit_ssd1306 import SSD1306_I2C

from kmk.extensions import Extension
import kmk.kmktime

from gc import mem_free

''' text ideas
Scan Time = 
WPM       =
Free Mem  =
layer     =
'''
class OLED(Extension):

    def __init__(
        self, 
        i2c,
        width=128, 
        height=32, 
        frames=None,
        enableText=False,
        refeshrate=3
    ):
        self.width = width
        self.height = height

        self.display = self._init_Display(width=width, height=height, i2c=i2c)

        self.enable = True
        self.enableText=enableText

        self.currentFrame = -1
        self.frameCount = 0
        self.framebuffer = frames
        self.refeshrate = refeshrate * 1000

        self.textBlocks = [
            # x   y    title
            [53,  1,  "Mem: "],
            [53,  9,  "Scan: "],
            [53,  18,  "Layer: "],
            [50,  27,  ""],
        ]
        self.enableTextMem = False
        self.enableTextScan = False
        self.enableTextLayer = True
        self.enableTextDebug = False

        self._oledUpdateQueue = False

        #Setting this to true allows for text to be updated every loop if enabled
        self.asyncText = False

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        self._clearDisplay()
        if self.enableText:#This is pretty bad in terms of scalabity, but works for now
            vspace = 8
            currentY = 1
            for i in range(len(self.textBlocks)):
                if i == 0 and self.enableTextMem:
                    self.textBlocks[i][1] = currentY
                    currentY += vspace
                elif i == 1 and self.enableTextScan:
                    self.textBlocks[i][1] = currentY
                    currentY += vspace
                elif i == 2 and self.enableTextLayer:
                    self.textBlocks[i][1] = currentY
                    currentY += vspace
                elif i == 3 and self.enableTextDebug:
                    self.textBlocks[i][1] = currentY
                    currentY += vspace
        if self.framebuffer is not None:
            self.currentFrame = 0
            self.frameCount = len(self.framebuffer) - 1
            self.time = kmk.kmktime.ticks_ms()
            self._updateDisplayTransaction(True, True, self.enableText, sandbox)
            #self._updateBuffer(self.framebuffer[0][0])
            self._updateDisplay()
        else:
            self._updateDisplayTransaction(True, False, self.enableText, sandbox)
        return

    def before_matrix_scan(self, sandbox):
        if self.enable:
            if self.enableTextScan:
                self.beforScan = kmk.kmktime.ticks_ms()
        return

    def after_matrix_scan(self, sandbox):
        if self.enable:
            if self.enableTextScan:
                self.afterScan = kmk.kmktime.ticks_ms()
            if self._oledUpdateQueue:
                self._updateDisplay()
                self._oledUpdateQueue = False
            else:
                if self.asyncText:
                    self._oledUpdateQueue = self._updateDisplayTransaction(self.asyncText, self._updateBufferWithTimeCheck(), self.enableText, sandbox)
                else:
                    self._oledUpdateQueue = self._updateDisplayTransaction(self._updateBufferWithTimeCheck(), self.frameCount > 0, self.enableText, sandbox)
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        self.enable = False
        self._clearDisplay()
        self._updateDisplay()
        return

    def on_powersave_disable(self, sandbox):
        self.enable = True
        return

    def _init_Display(self, width, height, i2c):
        return SSD1306_I2C(width=width, height=height, i2c=i2c)

    def _clearDisplay(self):
        self.display.buffer = bytearray(((self.height // 8) * self.width) + 1)
        self.display.buffer[0] = 0x40 
        self.display.buf = memoryview(self.display.buffer)[1:]

    def _fillDisplay(self):
        self.display.fill(1)
        self._updateDisplay()
    
    def _updateDisplay(self):
        self.display.write_framebuf()
        #self.display.show()

    def calcScanTime(self):
        if self.afterScan is None or self.beforScan is None:
            return -1
        return (self.afterScan - self.beforScan) * 1000

    def _updateBuffer(self, frame):
        #self.display.buffer = frame
        #self.display.buffer = bytearray(1) + bytearray(i for i in frame)
        self.display.buffer = bytearray(i for i in frame)#this works, but it is porbably slow
        self.display.buffer[0] = 0x40
        self.display.buf = memoryview(self.display.buffer)[1:]
  
    def _animateBuffer(self):
        self._updateBuffer(self.framebuffer[self.currentFrame][0])
        self.currentFrame += 1
        if self.currentFrame > self.frameCount or self.currentFrame < 0:
            self.currentFrame = 0
        return True

    def _displayText(self, x, y, text):
        self.display.text(string=text, x=x, y=y, color=1, font_name='/lib/font5x8.bin')

    def _updateBufferWithTimeCheck(self):
        currentTime = kmk.kmktime.ticks_ms()
        if kmk.kmktime.ticks_diff(currentTime, self.time + self.refeshrate) > 0:
            self.time = currentTime
            return True 
        return False

    def _updateDisplayTransaction(self, timecheck, updateBuffer, updateText, sandbox):
        if not timecheck:
            return False
        if updateBuffer:
            self._animateBuffer()
        if updateText:
            if not updateBuffer and self.framebuffer is not None:
                self._updateBuffer(self.framebuffer[self.currentFrame][0])
            elif self.framebuffer is None:
                self._clearDisplay()

            if self.enableTextMem:
                self._displayText(self.textBlocks[0][0], self.textBlocks[0][1], str(self.textBlocks[0][2]) + str(mem_free()))
            if self.enableTextScan:
                self._displayText(self.textBlocks[1][0], self.textBlocks[1][1], str(self.textBlocks[1][2]) + str(self.calcScanTime())[:1] + ' ms')
            if self.enableTextLayer:
                self._displayText(self.textBlocks[2][0], self.textBlocks[2][1], str(self.textBlocks[2][2]) + str(sandbox.active_layers[0]))
            if self.enableTextDebug:
                self._displayText(self.textBlocks[3][0], self.textBlocks[3][1], str(self.textBlocks[3][2]) + str(sandbox.last_received_report))
                
        return updateBuffer or updateText