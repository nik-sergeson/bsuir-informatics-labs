.model small
.stack 100h
.data
	a DW 0
	b DW 0
	digit DW 10
.code

Newline PROC
	MOV DL,10
	MOV AH,02h
	int 21h
	MOV DL,13
	MOV AH,02h
	int 21h
	RET
Newline ENDP

Insymbol PROC
	PUSH AX
	PUSH BX
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP
	XOR BX,BX
	XOR DX,DX
	XOR DI,DI
	MOV SI,0
	In_a:
		MOV AH,01h
		int 21h
		CMP AL,13
		JNE  Lab1
		JMP In_end
		Lab1:
		CMP AL,45
		JNE Lab2
		JMP ChgSign
		Lab2:
		CMP AL,8
		JNE Lab3
		JMP BSpace
		Lab3:
		CMP AL,27
		JNE Lab4
		JMP ClrStr
		Lab4:
		CMP AL,48
		JB Incor
		CMP AL,57
		JA Incor
		MOV BL,AL
		SUB BX,48
		MOV AX,DI
		MUL digit
		ADD AX,BX
		MOV DI,AX
		JMP In_a
	ChgSign:
		CMP SI,1
		JE In_a
		MOV SI,1
		JMP In_a
	BSpace:
		MOV DL,0
		MOV AH,02h
		int 21h
		MOV DL,8
		MOV AH,02h
		int 21h
		CMP DI,0
		JNE Normnum
		MOV SI,0
		JMP In_a
	Normnum:
		MOV DX,0
		MOV AX,DI
		DIV digit
		MOV DI,AX
		JMP In_a
	Incor:
		MOV DL,8
		MOV AH,02h
		int 21h
		MOV DL,0
		MOV AH,02h
		int 21h
		MOV DL,8
		MOV AH,02h
		int 21h
		JMP In_a
	ClrStr:
		MOV DL,13
		MOV AH,02h
		int 21h
		MOV CX,79
		Clr:
			MOV DL,0
			MOV AH,02h
			int 21h		
		loop Clr
		MOV DL,13
		MOV AH,02h
		int 21h
		MOV DI,0
		MOV SI,0
		JMP In_a
		
	In_end:
	CMP SI,0
	JE Posit
	NEG DI
	Posit:
		MOV [BP+12],DI	
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
	TEST AX,AX
    JNS Out_a
	MOV SI,1
	NEG AX
	Out_a:
		DIV digit
		PUSH DX
		MOV DX,0
		INC CX
		CMP AX,0
		JE Out_end
		JMP Out_a
	Out_end:
	CMP SI,1
	JNE Print
	MOV DL,45
	MOV AH,02h
	int 21h
	Print:
		POP DX
		ADD DX,48
		MOV AH,02h
		int 21h
	LOOP Print
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
PUBLIC Newline
start:	
	MOV AX,@DATA
	MOV DS,AX
	CALL Insymbol
	POP a
	CALL Newline
	CALL Insymbol
	POP b
	CALL NewLine
	XOR DX,DX
	MOV AX,a
	CWD
	IDIV b
	PUSH AX
	CALL Outsymbol
	MOV AH,01h
	int 21h
	MOV AH,4Ch
	int 21h
end start
