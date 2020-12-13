# CircuitJS 4-bit CPU

This is a minimalist 4-bit CPU implemented in the infamous
[Paul Falstad's  CircuitJS](https://www.falstad.com/circuit/circuitjs.html)
([source code](https://github.com/sharpie7/circuitjs1)).
It is Turing complete leveraging a jump-with-carry instruction.
With a total of 16 4-bit words (8 bytes) of program ROM and two 4-bit general
purpose registers, and a 4-bit adder … it really packs a punch!
I hope you find this fun and maybe even learn something too.

![Circuit Image](https://github.com/Izzette/circuitjs-computer/blob/master/circuit.png?raw=true)

## How to run

Go to [Paul Falstad's  CircuitJS](https://www.falstad.com/circuit/circuitjs.html),
click on `File` → `Import From Text` and paste the contents of circuit.txt.
This circuit comes with a pre-programmed microcode ROM and program ROM.
You can see the assembly source code in the examples/jump-if-carry directory.

## High-Level block diagram

## Hacking

There's a lot of potential here for more useful instructions without modifying
the circuit at all.
With minor modifications additional arithmetic operations or conditional jumps
should be possible.
There's a lot of free control-word bits and a maximum of 16 micro-operations per
instruction.
The really adventurous could try adding a memory segmentation register to
increase the usably program ROM address space, increasing the architecture to
8-bits, or even adding external IO.

To get started playing with it, install rust/cargo to build
[customasm](https://github.com/hlorenzi/customasm), this will allow you to
compile new assembly source.
Try building the example, then hack it:
```sh
bin/customasm src/examples/jump-if-carry/prog.s
./formatrom.py src/examples/jump-if-carry/prog.bin > prog.txt
```
You can then paste `prog.txt` into the circuits program ROM by right clicking on
it and selecting edit.

To define new instructions, edit `microcode.py` and run it.
It'll output the microcode and the customasm assembler definition.
You can paste the microcode into the MC ROM, and drop the assembler definition
at the top of your assembly file.

## Big Thanks!

Big thanks to [Ben Eater](https://eater.net/) who inspired me to experiment,
[Paul Falstad](https://www.falstad.com) and [Iain Sharp](http://lushprojects.com)
for developing CircuitJS, and to ["Lorenzi"/@hlorenzi](https://github.com/hlorenzi)
for for developing customasm.
