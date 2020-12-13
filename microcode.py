#!/usr/bin/env python3

import sys
from textwrap import dedent

######################
#### control bits ####
######################

# Do# - Data-bus output selector.
#       0b00: none
#       0b01: Program ROM
#       0b10: Reserved
#       0b11: Register-B
# Dl# - Data-bus load selector.
#       0b00: none
#       0b01: Instruction pointer
#       0b10: Register-A
#       0b11: Register-B
# Ao# - Address-bus output selector.
#       0b0: none
#       0b1: Instruction pointer
# MCl - Instruction load (microinstruction register load)
# Abs - Register-A bus select
#       L: Data-bus
#       H: Address-bus
# ADc - ALU/ADD carry
# ADo - ALU/ADD ouput
# PCr - Program-counter reset
# RAo - Register-A output
# RFl - Flags-Register load
# Flc - Load instruction pointer only if flags carry bit is set.  (jump-if-carry)

Do0, Do1, Do2, Do3 = 0b00, 0b01, 0b10, 0b11
Dl0, Dl1, Dl2, Dl3 = 0b00 << 2, 0b01 << 2, 0b10 << 2, 0b11 << 2
Ao0, Ao1 = 0b0 << 4, 0b1 << 4
MCl = 0b1 << 5
Abs = 0b1 << 6
ADc = 0b1 << 7
ADo = 0b1 << 8
PCr = 0b1 << 9
RAo = 0b1 << 10
RFl = 0b1 << 11
Flc = 0b1 << 12

INC_IP = Do0|Dl1|Ao1|ADc|ADo # increment instruction pointer
NEXT = Ao1|MCl # execute next instruction

spec = [
    (
        'reset => 0x{0:1x}',
        [Do0|Dl1, Do0|Dl2, Do0|Dl3, NEXT|PCr],
    ),
    (
        'nop => 0x{0:1x}',
        [INC_IP, NEXT],
    ),
    (
        'load a, {{value}} => 0x{0:1x} @ value`4',
        [INC_IP, Do1|Dl2|Ao1, INC_IP, NEXT],
    ),
    (
        'load b, {{value}} => 0x{0:1x} @ value`4',
        [INC_IP, Do1|Dl3|Ao1, INC_IP, NEXT],
    ),
    (
        'inc a => 0x{0:1x}',
        [RAo|Dl2|Abs|ADc|ADo|RFl, INC_IP, NEXT],
    ),
    (
        'mov a, b => 0x{0:1x}',
        [RAo|Dl3, INC_IP, NEXT],
    ),
    (
        'mov b, a => 0x{0:1x}',
        [Do3|Dl2, INC_IP, NEXT],
    ),
    (
        'jmp {{value}} => 0x{0:1x} @ value`4',
        [INC_IP, Do1|Dl1|Ao1, NEXT],
    ),
    (
        'jc {{value}} => 0x{0:1x} @ value`4',
        [INC_IP, Do1|Dl1|Ao1|Flc, NEXT|Flc, INC_IP, NEXT],
    ),
]

microcode = []
ruledef = []

for i, v in enumerate(spec):
    rule, uops = v
    microcode.append("{:d}: {:s}".format(i*16, ' '.join([str(v) for v in uops])))
    ruledef.append("\t" + rule.format(i))

print("Microcode:", file=sys.stderr)
print("\n".join(microcode))

print(file=sys.stderr)

print("Assembler definition:", file=sys.stderr)
print(dedent("""
      #bits 4
      #bankdef prg { #addr 0x0, #size 0x10, #outp 0x0 }
      #bank prg
      """).strip())
print("#ruledef")
print("{")
print("\n".join(ruledef))
print("}")
