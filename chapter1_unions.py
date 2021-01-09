from ctypes import *

class barley_amount(Union):
    _fields_ = [
        ('barley_long', c_long),
        ('barley_int', c_int),
        ('barley_char', c_char * 8),
    ]

value = input('Amount of barley:')
barley = barley_amount(int(value))
print('Barley as long %ld' % barley.barley_long)
print('Barley as int %d' % barley.barley_int)
print('Barley as char %s' % barley.barley_char)