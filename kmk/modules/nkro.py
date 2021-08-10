from boot import USBdescriptor
from kmk.handlers.stock import passthrough as handler_passthrough
from kmk.hid import USBHID, HIDReportTypes, HIDUsagePage
from kmk.keys import FIRST_KMK_INTERNAL_KEY, ConsumerKey, ModifierKey, make_key
from kmk.modules import Module

# https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/CircuitPython_MacroPad_NKRO
# QMK Docs https://github.com/qmk/qmk_firmware/blob/master/docs/usb_nkro.txt


class HIDReportSizes:
    KEYBOARD = 24
    CONSUMER = 2


class BitmapKeyboard(USBHID):

    REPORT_BYTES = HIDReportSizes.KEYBOARD
    CONSUMER_REPORT_BYTES = HIDReportSizes.CONSUMER

    MASTER_REPORT_BYTES = REPORT_BYTES + CONSUMER_REPORT_BYTES + 1

    def __init__(self, debug=False):
        self._bitmapkeyboard_debug_enable = debug

        self.create_bytearray()
        self.report_device = HIDReportTypes.KEYBOARD

        super().post_init()

    def create_bytearray(self):
        self.master_report = bytearray(self.MASTER_REPORT_BYTES)

        # Define area for modifiers and bitmap
        self.report = memoryview(self.master_report)[0 : self.REPORT_BYTES]
        self.report_modifier = memoryview(self.report)[0:1]
        self.report_bitmap = memoryview(self.report)[1:]

        # Define area for consumer keys
        self.consumer_report = memoryview(self.master_report)[self.REPORT_BYTES + 1 :]

    def add_modifier(self, modifier):
        if isinstance(modifier, ModifierKey):
            if modifier.code == ModifierKey.FAKE_CODE:
                for mod in modifier.has_modifiers:
                    self.report_modifier[0] |= mod
            else:
                self.report_modifier[0] |= modifier.code
        else:
            self.report_modifier[0] |= modifier

        return self

    def remove_modifier(self, modifier):
        if isinstance(modifier, ModifierKey):
            if modifier.code == ModifierKey.FAKE_CODE:
                for mod in modifier.has_modifiers:
                    self.report_modifier[0] ^= mod
            else:
                self.report_modifier[0] ^= modifier.code
        else:
            self.report_modifier[0] ^= modifier

        return self

    def add_key(self, key):
        if isinstance(key, ConsumerKey):
            return self.add_consumer(key)
        keycode = key.code
        self.report_bitmap[keycode >> 3] |= 1 << (keycode & 0x7)
        if self._bitmapkeyboard_debug_enable:
            print(
                'BitmapKeyboard: keycode debug: {}, {}, {}'.format(
                    keycode >> 3,
                    1 << (keycode & 0x7),
                    bin(self.report_bitmap[keycode >> 3]),
                )
            )

        return self

    def remove_key(self, key):
        if isinstance(key, ConsumerKey):
            return self.remove_consumer(key)

        keycode = key.code
        self.report_bitmap[keycode >> 3] ^= 1 << (keycode & 0x7)

        return self

    def add_consumer(self, consumer):
        for idx, _ in enumerate(self.consumer_report):
            if self.consumer_report[idx] == 0x00:
                self.consumer_report[idx] = consumer.code
                break

        return self

    def remove_consumer(self, consumer):
        for idx, _ in enumerate(self.consumer_report):
            if self.consumer_report[idx] == consumer.code:
                self.consumer_report[idx] = 0x00

        return self

    def clear_all(self):
        for idx, _ in enumerate(self.master_report):
            self.master_report[idx] = 0x00

        return self

    def create_report(self, keys_pressed):
        self.clear_all()

        if self._bitmapkeyboard_debug_enable and len(keys_pressed) > 0:
            print('BitmapKeyboard: {}'.format(keys_pressed))

        consumer_key = None
        for key in keys_pressed:
            if isinstance(key, ConsumerKey):
                consumer_key = key
                break

        reporting_device = self.report_device
        needed_reporting_device = HIDReportTypes.KEYBOARD

        if consumer_key:
            needed_reporting_device = HIDReportTypes.CONSUMER

        if reporting_device != needed_reporting_device:
            self.send()

        self.report_device = needed_reporting_device

        if consumer_key:
            self.add_consumer(consumer_key)
        else:
            for key in keys_pressed:
                if key.code >= FIRST_KMK_INTERNAL_KEY:
                    continue

                if isinstance(key, ModifierKey):
                    self.add_modifier(key)
                else:
                    self.add_key(key)

                    if key.has_modifiers:
                        for mod in key.has_modifiers:
                            self.add_modifier(mod)

        return self

    def send(self):
        self.hid_send()
        return self

    def hid_send(self):
        try:
            if self.report_device == HIDReportTypes.CONSUMER:
                self.devices[self.report_device].send_report(self.consumer_report)
            else:
                self.devices[self.report_device].send_report(self.report)
            return True
        except ValueError as ve:
            print('BitmapKeyboard error:\n{}'.format(ve))
            print('Make sure your boot config is correct')
            return False

    def hid_receive(self):
        # This for HID OUT
        if self.report_device == HIDReportTypes.KEYBOARD:
            return self.devices[self.report_device].last_received_report
        return None


class NKRO(Module):
    def __init__(self, debug=False):
        self._nkro_debug_enable = debug
        self.nkro_enable = True

        if self._nkro_debug_enable:
            print('NKRO Debug enabled')

        self.BitmapKb = BitmapKeyboard(self._nkro_debug_enable)

        '''
        # Can not curretly switch USB devices durring run time
        make_key(
            names=('NKRO_TOG',), 
            on_press=self._nkro_tog, 
            on_release=handler_passthrough
        )

        make_key(
            names=('NKRO_ON',), 
            on_press=self._nkro_on, 
            on_release=handler_passthrough
        )

        make_key(
            names=('NKRO_OFF',), 
            on_press=self._nkro_off, 
            on_release=handler_passthrough
        )
        '''

    def on_runtime_enable(self, keyboard):
        return

    def on_runtime_disable(self, keyboard):
        return

    def during_bootup(self, keyboard):
        self.keyboard = keyboard
        if self.BitmapKb.hid_send():
            keyboard._hid_helper = self.BitmapKb
        else:
            print('Boot config might be incorrect')
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    '''
    def _nkro_tog(self, key, keyboard, *args, **kwargs):
        if self.nkro_enable:
            self._nkro_off(key, keyboard, *args, **kwargs)
        else:
            self._nkro_on(key, keyboard, *args, **kwargs)

    def _nkro_on(self, key, keyboard, *args, **kwargs):
        self.nkro_enable = True
        devices = [
            USBdescriptor.bitmap_keyboard,
            usb_hid.Device.CONSUMER_CONTROL,
        ]
        usb_hid.disable()
        usb_hid.enable(devices)
        self.BitmapKb = BitmapKeyboard(self._nkro_debug_enable)
        self.keyboard._hid_helper = self.BitmapKb

    def _nkro_off(self, key, keyboard, *args, **kwargs):
        self.nkro_enable = False
        devices = [
            usb_hid.Device.KEYBOARD,
            usb_hid.Device.CONSUMER_CONTROL,
        ]
        usb_hid.disable()
        usb_hid.enable(devices)
        self.keyboard._init_hid()
    '''
