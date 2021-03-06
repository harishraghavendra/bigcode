"""enums.py

Enumerations from the SFF auto.yml.
"""

class Enumeration(object):
    @classmethod
    def name(klass, value):
        for (k, v) in klass.__dict__.iteritems():
            if v == value:
                return k
        return None

# <auto.start.pyenum(ALL).define>
class SFF_DOM_FIELD_FLAG(Enumeration):
    TEMP = (1 << 0)
    VOLTAGE = (1 << 1)
    BIAS_CUR = (1 << 2)
    RX_POWER = (1 << 3)
    RX_POWER_OMA = (1 << 4)
    TX_POWER = (1 << 5)


class SFF_DOM_SPEC(Enumeration):
    UNSUPPORTED = 0
    SFF8436 = 1
    SFF8472 = 2
    SFF8636 = 3


class SFF_MEDIA_TYPE(Enumeration):
    COPPER = 0
    FIBER = 1


class SFF_MODULE_CAPS(Enumeration):
    F_100 = 1
    F_1G = 2
    F_10G = 4
    F_25G = 8
    F_40G = 16
    F_100G = 32


class SFF_MODULE_TYPE(Enumeration):
    _100G_AOC = 0
    _100G_BASE_CR4 = 1
    _100G_BASE_SR4 = 2
    _100G_BASE_LR4 = 3
    _100G_CWDM4 = 4
    _100G_PSM4 = 5
    _100G_SWDM4 = 6
    _40G_BASE_CR4 = 7
    _40G_BASE_SR4 = 8
    _40G_BASE_LR4 = 9
    _40G_BASE_LM4 = 10
    _40G_BASE_ACTIVE = 11
    _40G_BASE_CR = 12
    _40G_BASE_SR2 = 13
    _40G_BASE_SM4 = 14
    _40G_BASE_ER4 = 15
    _40G_BASE_SWDM4 = 16
    _25G_BASE_CR = 17
    _25G_BASE_SR = 18
    _25G_BASE_LR = 19
    _25G_BASE_AOC = 20
    _10G_BASE_SR = 21
    _10G_BASE_LR = 22
    _10G_BASE_LRM = 23
    _10G_BASE_ER = 24
    _10G_BASE_CR = 25
    _10G_BASE_SX = 26
    _10G_BASE_LX = 27
    _10G_BASE_ZR = 28
    _10G_BASE_SRL = 29
    _1G_BASE_SX = 30
    _1G_BASE_LX = 31
    _1G_BASE_ZX = 32
    _1G_BASE_CX = 33
    _1G_BASE_T = 34
    _100_BASE_LX = 35
    _100_BASE_FX = 36
    _4X_MUX = 37


class SFF_SFP_TYPE(Enumeration):
    SFP = 0
    QSFP = 1
    QSFP_PLUS = 2
    QSFP28 = 3
    SFP28 = 4

# <auto.end.pyenum(ALL).define>
