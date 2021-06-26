'''
Simple Class where bytearrays can be stored
then be used for oled animations

Each list has a bytearray followed by a number which is used as a delay 
for how long the previous frame should stay on the screen. 
If there is only one item then the number isn't used, but there should still be a number there.
Setting the delay to 0 removes the delay from that previous frame
This function is deprecated
'''
class arrays():

    def __init__(self):
        self.borpa = [
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@ \x10\x10\x10\x10\x10\xf0\x10\x10\x10\xd0\xf0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@@  \x10\x08\x04\x03\x00\x00\x00\x00\x00\x00\x00\x80A""\x1f%$$$4<\x1c\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80`\x10\x08\x04\x02\x01\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80O0  @@\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xe3\xe0\xe0\xe0\xe0\xc0\xc0\xc2\xc5\xc8\xd4\xd4\xd5\xd5\xd5\xd5\xd5\xd5\xd5\x95\x94\x92\x92\x92\xd2\xd1\xfd\x05\x05\x05\x05\x04\x04\x05\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@  \xd000\xb0\xd0\xd0   @\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe00\x0c\x02\x01\x00\x00\x00\x00\x00\x03\x06\x04\x05\x07\x19&BB>\x18\xc3|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80`\x18\x87\xc0@@@@@@@@`  0\x10\x10\x10\x10\x10\x10\x10\x10\x1f    @\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xe3\xe0\xc0\xc1\xc3\x82\x82\x86\xc5\xc5\xc5\xc5\xc5\xc5\xe5\xe5\xc5\xc5\xc5\xc5\xc5\xc5\xc5\xc5\xc5\xc5\xc5\xc5\xe7\xfe\xc2\x02\x02\x02\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@ \xa0\xa0\xa0   \x10\x10\x10    @\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0 \x10\x08\x0f\x00\x0e\x11...\x11\x0e\x00\x00\x18$BZZ"\x1c\x00\x03\x1c\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0\xa0\x91\x9e\x90\x88\x88\x88\x88\x88\x88\x90\x90\x90\x90\x90\x90\x90\x90\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\x9f\x90\xa0\xa0 @\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc3\xe2\xdc\xc4\xc4\xc4\xc4\xc4\xc2\xc2\xc2\xc2\xc2\xc2\xe2\xe4\xe4\xe4\xe4\xc4\xc4\xc4\xc4\xc4\xc4\xc4\xc4\xc4\xc4\xc2\xc2\xe2\xe2\xfd\xe5\x83\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@@ \x10\x90\xd0\xd0PPP\xd0  @@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<F\x81\x18<DD9\x03\x07\x04\x04\x06\x03\x00\x00\x00\x00\x00\x01\x06\x1cp\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@@  \xa0\xbf\xa0\x90\x90\x90\x90\x10\x10\x10\x10\x10  @@@@@@@@@\x81\x0f8@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x05\x04\x85\xe5\xfd\xe5\xe2\xc2\xc2\xc2\xc2\xc2\xc4\xc5\xc5\xc5\xe5\xe5\xe5\xe5\xe5\xe5\xe5\xe5\xc5\xc5\xc5\xc5\xc4\xc6\xc3\xe0\xe0\xe1\xe6\xf8\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00@\xe0\xf0\x10\x10\x10\x10\xf0\x10\x10\x10\x10 @\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x1c<$$$$%\x1e""A\x80\x00\x00\x00\x00\x00\x00\x00\x03\x04\x08\x10  @@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@@  0o@@@@@@@@@@@@@@@\x80\x01\x02\x04\x08\x10 \xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x05\x04\x04\x05\x05\x05\xc5\xfd\xe9\xea\xca\xca\xca\xca\xca\xc5\xc5\xc5\xe5\xe5\xe5\xe5\xe5\xe5\xe5\xe4\xe3\xf0\xf0\xe0\xe0\xe0\xe0\xe3\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00@\xe0\xf0\xf0\x90\x10\x10\x10\xf0\x10\x10\x10  @\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x1c<4$$$%?""A\x80\x00\x00\x00\x00\x00\x00\x00\x03\x04\x08\x10  @@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@@@  0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x04\x08\x10 \xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x05\x04\x04\x05\x05\x05\x05\xf5\xcf\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe3\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@ \x10\x10\x10\x10\x10\x10\x10\x100@@@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000L\x83\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x06\x18`\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@@  \xe0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x10`\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x05\x04\x85\xe5\xfd\xc7\xc3\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc1\xc6\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@@`     \x10\x10\x10\x10    @\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0 \x10\x08\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1c\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xe0\x11\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x10 \xe0 \xa0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x82\xe2\xde\xc1\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\xc0\xc0\xc0\xc0\xff\x82\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@`\x10\x10\x10\x10\x10\x10\x10\x10  @\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x0c\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x83|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0`\x18\x0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xf0\xa0 `@@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xe3\xe0\xe0\xc0\xc0\x80\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe3\xef\xf5\xc5\x05\x04\x05\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@ \x10\x10\x10\x10\xf0\x10\x10\x10\x10\xd0\xf0\xe0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@@  \x10\x08\x04\x03\x00\x00\x00\x00\x00\x00\x00\x80A""\x1f%$$$4<\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80`\x10\x08\x04\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xf0  @@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xe3\xe0\xe0\xe0\xe0\xf0\xf0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\xc0\xc0\xe3\xfd\x05\x05\x05\x05\x04\x04\x05\x05\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01],   
        ]

        self.borpa2 = [
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@ \x10\x10\x10\x10\x10\xf0\x10\x10\x10\xd0\xf0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@@  \x10\x08\x04\x03\x00\x00\x00\x00\x00\x00\x00\x80A""\x1f%$$$4<\x1c\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80`\x10\x08\x04\x02\x01\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80O0  @@\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xe3\xe0\xe0\xe0\xe0\xc0\xc0\xc2\xc5\xc8\xd4\xd4\xd5\xd5\xd5\xd5\xd5\xd5\xd5\x95\x94\x92\x92\x92\xd2\xd1\xfd\x05\x05\x05\x05\x04\x04\x05\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 1.01], 
        ]

        self.aperture = [
            [bytearray(b'@\xff\xff\xff?\x1f\x0f\x0f\x07\x03\x03\x87\x8d\x8d\x99\xb9\xf1\xe1\xe1\xc1\x81\x81\x07\x7f\xff\xc7\x07\x0f\x1f?\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x07\x06\x06\x06\x83\xe3\xf3\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\xc0\xe08\x1c\xc7\xe3\xe3\x03?\xff\xff\xff\xff\xff?\x03\x03sss3\x03\x87\xff\xff\xff\xff\x0f\x03\x0333333\xf3\xff\xff\xff\x0f\x03\x03sss3\x03\x87\xff\xff\xff\xff\xf3\xf3\xf3\x13\x03\x83\xf3\xf3\xf3\xf3\xff\xff\x1f\x03\x03\xf3\xff\xff\xff\xff\x0f\x03\x83\xff\xff\xff\xff\x0f\x03\x03sss3\x03\x87\xff\xff\xff\xff\x0f\x03\x0333333\xf3\xff\xff\xe0x\x1c\x0f\x03\x01?\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe7\xe3\xf0xx\xf9\xf9\xf9\xe0\xe0g\xff\xff\xff\xe7\xe0\xe0\xfe\xfe~\xfe\xff\xff\xff\xff\xff\x7fg`\xe0\xe6\xe7\xe7\xe7\xe7g\x7f\x7f\xff\xe7\xe0\xf0\xff\x7f~x`\xe1\xe7\xff\xff\xff\xff\x7f\xff\xe7\xe0\xe0\xff\x7f\x7f\x7f\x7f\x7f\xff\xf0\xe0\xe0cgg\xe3\xe1\xf0\xf8\xff\x7f\x7f\x7f\xe7\xe0\xf0\xff\xff\xfep\xe0\xe1\xe7\xff\x7f\x7fg`\xe0\xe6\xe7\xe7ggg\x7f\xff\xff\xff\xff\xfc\xf8\xf0\xe0\xe0\xc3\xff\xf8\x80\x81\x03\x03\x07\x0f\x0f\x199\xb1\xe1\xe1\xc0\xc0\xe0\xf0\xf8\xfc\xfe\xff\xff\xff\xff\xff\xf0\xf7\xf7\xf7\xff\xff\xff\xf1\xfa\xfa\xfa\xf1\xff\xff\xff\xf8\xf0\xf5\xf4\xfa\xff\xff\xff\xff\xf8\xf7\xf7\xf7\xf8\xff\xff\xff\xff\xf0\xfd\xfd\xf2\xff\xff\xff\xff\xf1\xfa\xfa\xfa\xf1\xff\xff\xff\xff\xff\xf0\xff\xff\xff\xff\xff\xf8\xf7\xf7\xf7\xf8\xff\xff\xff\xff\xf0\xfd\xfd\xf2\xff\xff\xff\xff\xff\xf0\xff\xff\xff\xff\xf0\xf5\xf5\xf5\xff\xff\xff\xff\xf4\xf5\xf5\xf1\xff'), 0],
        ]

        self.apertureInv = [
            [bytearray(b'@\x00\x00\x00\xc0\xe0\xf0\xf0\xf8\xfc\xfcxrrfF\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf9\xf9\xf9|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\xc7\xe38\x1c\x1c\xfc\xc0\x00\x00\x00\x00\x00\xc0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\x0c\x0c\x0c\xec\xfc|\x0c\x0c\x0c\x0c\x00\x00\xe0\xfc\xfc\x0c\x00\x00\x00\x00\xf0\xfc|\x00\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x1f\x87\xe3\xf0\xfc\xfe\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1c\x0f\x87\x87\x06\x06\x06\x1f\x1f\x98\x00\x00\x00\x18\x1f\x1f\x01\x01\x81\x01\x00\x00\x00\x00\x00\x80\x98\x9f\x1f\x19\x18\x18\x18\x18\x98\x80\x80\x00\x18\x1f\x0f\x00\x80\x81\x87\x9f\x1e\x18\x00\x00\x00\x00\x80\x00\x18\x1f\x1f\x00\x80\x80\x80\x80\x80\x00\x0f\x1f\x1f\x9c\x98\x98\x1c\x1e\x0f\x07\x00\x80\x80\x80\x18\x1f\x0f\x00\x00\x01\x8f\x1f\x1e\x18\x00\x80\x80\x98\x9f\x1f\x19\x18\x18\x98\x98\x98\x80\x00\x00\x00\x00\x03\x07\x0f\x1f\x1f<\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x0f\x08\x08\x08\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x07\x0f\n\x0b\x05\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x0f\n\n\n\x00\x00\x00\x00\x0b\n\n\x0e\x00'), 0],
        ]

        self.apertureLoading = [
            [bytearray(b'@\x00\x00\x00\xc0\xe0\xf0\xf0\xf8\xfc\xfcxrrfF\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf9\xf9\xf9|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\xc7\xe38\x1c\x1c\xfc\xc0\x00\x00\x00\x00\x00\xc0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\x0c\x0c\x0c\xec\xfc|\x0c\x0c\x0c\x0c\x00\x00\xe0\xfc\xfc\x0c\x00\x00\x00\x00\xf0\xfc|\x00\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x1f\x87\xe3\xf0\xfc\xfe\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1c\x0f\x87\x87\x06\x06\x06\x1f\x1f\x98\x00\x00\x00\x18\x1f\x1f\x01\x01\x81\x01\x00\x00\x00\x00\x00\x80\x98\x9f\x1f\x19\x18\x18\x18\x18\x98\x80\x80\x00\x18\x1f\x0f\x00\x80\x81\x87\x9f\x1e\x18\x00\x00\x00\x00\x80\x00\x18\x1f\x1f\x00\x80\x80\x80\x80\x80\x00\x0f\x1f\x1f\x9c\x98\x98\x1c\x1e\x0f\x07\x00\x80\x80\x80\x18\x1f\x0f\x00\x00\x01\x8f\x1f\x1e\x18\x00\x80\x80\x98\x9f\x1f\x19\x18\x18\x98\x98\x98\x80\x00\x00\x00\x00\x03\x07\x0f\x1f\x1f<\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x0f\x08\x08\x08\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x07\x0f\n\x0b\x05\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x0f\n\n\n\x00\x00\x00\x00\x0b\n\n\x0e\x00'), 0.35],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x06\x06\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\xf8|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 5],
            [bytearray(b'@\x00\x00\x00\xc0\xe0\xf0\xf0\xf8\xfc\xfcxrrfF\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf9\xf9\xf9|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x87\xe3\xf0\xfc\xfe\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x07\x0f\x1f\x1f<\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 0.35],
            [bytearray(b'@\x00\x00\x00\xc0\xe0\xf0\xf0\xf8\xfc\xfcxrrfF\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf9\xf9\xf9|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\xc7\xe38\x1c\x1c\xfc\xc0\x00\x00\x00\x00\x00\xc0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\x0c\x0c\x0c\xec\xfc|\x0c\x0c\x0c\x0c\x00\x00\xe0\xfc\xfc\x0c\x00\x00\x00\x00\xf0\xfc|\x00\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x1f\x87\xe3\xf0\xfc\xfe\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1c\x0f\x87\x87\x06\x06\x06\x1f\x1f\x18\x00\x00\x00\x18\x1f\x1f\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x18\x1f\x1f\x19\x18\x18\x18\x18\x18\x00\x00\x00\x18\x1f\x0f\x00\x00\x01\x07\x1f\x1e\x18\x00\x00\x00\x00\x00\x00\x18\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x0f\x1f\x1f\x1c\x18\x18\x1c\x1e\x0f\x07\x00\x00\x00\x00\x18\x1f\x0f\x00\x00\x01\x0f\x1f\x1e\x18\x00\x00\x00\x18\x1f\x1f\x19\x18\x18\x18\x18\x18\x00\x00\x00\x00\x00\x03\x07\x0f\x1f\x1f<\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 0.35],
            [bytearray(b'@\x00\x00\x00\xc0\xe0\xf0\xf0\xf8\xfc\xfcxrrfF\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf9\xf9\xf9|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\xc7\xe38\x1c\x1c\xfc\xc0\x00\x00\x00\x00\x00\xc0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\x0c\x0c\x0c\xec\xfc|\x0c\x0c\x0c\x0c\x00\x00\xe0\xfc\xfc\x0c\x00\x00\x00\x00\xf0\xfc|\x00\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x1f\x87\xe3\xf0\xfc\xfe\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1c\x0f\x87\x87\x06\x06\x06\x1f\x1f\x98\x00\x00\x00\x18\x1f\x1f\x01\x01\x81\x01\x00\x00\x00\x00\x00\x80\x98\x9f\x1f\x19\x18\x18\x18\x18\x98\x80\x80\x00\x18\x1f\x0f\x00\x80\x81\x87\x9f\x1e\x18\x00\x00\x00\x00\x80\x00\x18\x1f\x1f\x00\x80\x80\x80\x80\x80\x00\x0f\x1f\x1f\x9c\x98\x98\x1c\x1e\x0f\x07\x00\x80\x80\x80\x18\x1f\x0f\x00\x00\x01\x8f\x1f\x1e\x18\x00\x80\x80\x98\x9f\x1f\x19\x18\x18\x98\x98\x98\x80\x00\x00\x00\x00\x03\x07\x0f\x1f\x1f<\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x0f\x08\x08\x08\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x07\x0f\n\x0b\x05\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x0f\n\n\n\x00\x00\x00\x00\x0b\n\n\x0e\x00'), 0.35],
            [bytearray(b'@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x06\x06\x0e\x1e\x1e>~~\xf8\x80\x008\xf8\xf0\xe0\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\xf8|\x1c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03?\x1f\xc7\xe38\x1c\x1c\xfc\xc0\x00\x00\x00\x00\x00\xc0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\x0c\x0c\x0c\xec\xfc|\x0c\x0c\x0c\x0c\x00\x00\xe0\xfc\xfc\x0c\x00\x00\x00\x00\xf0\xfc|\x00\x00\x00\x00\xf0\xfc\xfc\x8c\x8c\x8c\xcc\xfcx\x00\x00\x00\x00\xf0\xfc\xfc\xcc\xcc\xcc\xcc\xcc\x0c\x00\x00\x1f\x87\xe3\xf0\xfc\xfe\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1c\x0f\x87\x87\x06\x06\x06\x1f\x1f\x98\x00\x00\x00\x18\x1f\x1f\x01\x01\x81\x01\x00\x00\x00\x00\x00\x80\x98\x9f\x1f\x19\x18\x18\x18\x18\x98\x80\x80\x00\x18\x1f\x0f\x00\x80\x81\x87\x9f\x1e\x18\x00\x00\x00\x00\x80\x00\x18\x1f\x1f\x00\x80\x80\x80\x80\x80\x00\x0f\x1f\x1f\x9c\x98\x98\x1c\x1e\x0f\x07\x00\x80\x80\x80\x18\x1f\x0f\x00\x00\x01\x8f\x1f\x1e\x18\x00\x80\x80\x98\x9f\x1f\x19\x18\x18\x98\x98\x98\x80\x00\x00\x00\x00\x03\x07\x0f\x1f\x1f<\x00\x07\x7f~\xfc\xfc\xf8\xf0\xf0\xe6\xc6N\x1e\x1e??\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x0f\x08\x08\x08\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x07\x0f\n\x0b\x05\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x0e\x05\x05\x05\x0e\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x07\x08\x08\x08\x07\x00\x00\x00\x00\x0f\x02\x02\r\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x0f\n\n\n\x00\x00\x00\x00\x0b\n\n\x0e\x00'), 5],
        ]

        self.empty = [
            [bytearray(((32 // 8) * 128)),0]
        ]