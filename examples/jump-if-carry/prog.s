#bits 4
#bankdef prg { #addr 0x0, #size 0x10, #outp 0x0 }
#bank prg
#ruledef
{
	reset => 0x0
	nop => 0x1
	load a, {value} => 0x2 @ value`4
	load b, {value} => 0x3 @ value`4
	inc a => 0x4
	mov a, b => 0x5
	mov b, a => 0x6
	jmp {value} => 0x7 @ value`4
	jc {value} => 0x8 @ value`4
}

start:
	load a, 14 ; set register-a to 14
.loop:
	inc a ; increment register-a and set the carry bit if overflow
	jc .end ; jump if the flags carry bit is set
	jmp .loop ; execute the next iteration of the loop
.end:
	jmp .end ; halt
