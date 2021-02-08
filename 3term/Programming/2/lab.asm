.model small
.stack 100h
.data
	a DW 9
	b DW 0
	digit DW 10
.code
Insymbol PROC
	PUSH AX
	PUSH BX
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP
	XOR DX,DX
	XOR AX,AX
	In_a:
		MOV AH,01h
		int 21h
		CMP AL,13
		JE In_end
		MOV BL,AL
		SUB BX,48
		MOV AX,DX
		MUL digit
		ADD AX,BX
		MOV DX,AX
		JMP In_a
	In_end:
	MOV [BP+12],DX
	MOV DL,10;;;;
	MOV AH,02h;;;;
	int 21h;;;;
	MOV DL,13;;;;
	MOV AH,02h;;;;;
	int 21h
	MOV SP,BP
	POP BP
	POP DX
	POP CX
	POP BX 
	POP AX
	RET
	Insymbol ENDP
	
	Outsymbol PROC
	PUSH AX
	PUSH BX
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP
	MOV CX,0
	MOV DX,0
	MOV AX,[BP+12]
	Out_a:
		DIV digit
		PUSH DX
		INC CX
		CMP AX,0
		JE Out_end
		MOV DX,0 ;;;;;;;;;;;
		JMP Out_a
	Out_end:
	Print:
		POP DX
		ADD DX,48
		MOV AH,02h
		int 21h
	LOOP Print
	MOV DL,10
	MOV AH,02h
	int 21h
	MOV DL,13
	MOV AH,02h
	int 21h
	MOV AH,01h
	int 21h
	MOV SP,BP
	POP BP
	POP DX
	POP CX
	POP BX 
	POP AX
	RET
	Outsymbol ENDP
PUBLIC Insymbol 
PUBLIC Outsymbol
start:	
	MOV AX,@DATA
	MOV DS,AX
	CALL Insymbol
	POP a
	CALL Insymbol
	POP b
	MOV DX,0
	MOV AX,a
	DIV b
	PUSH AX
	CALL Outsymbol
	MOV AH,4Ch
	int 21h
end start
