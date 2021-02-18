.model small
.stack 200h
.data
	a DW 0
	b DW 0       
	Errorstr DB 'Error $'
	Overflowstr DB ' overflow$'
	Divstr DB 'Result: $'
	Residuestr DB 'Residue: $'
	Bytestr DB 'Binary: $'
	digit DW 10
	loopcount DB 8
	minussign DB 0
.code

Newline PROC        
    ;procedure to create empty line  
    PUSH DX
    PUSH CX
    PUSH BX
    PUSH AX
	MOV DL,10	;new line symbol
	MOV AH,02h
	int 21h
	MOV DL,13	;carriage return symbol
	MOV AH,02h
	int 21h   
	POP AX
	POP BX
	POP CX
	POP DX
	RET
Newline ENDP        

Insymbol PROC
    ;procedure to get a number
	PUSH AX		;register back up
	PUSH BX
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP	;getting stack pointer
	XOR BX,BX	;clearing registers
	XOR DX,DX
	XOR DI,DI
	MOV SI,0
	Incycle:
		MOV AH,01h
		int 21h
		CMP AL,13	;check if enter is pressed
		JNE  Label1		;if not, continue
		JMP Inend
		Label1:
			CMP AL,45	;check if nuber is negative
			JNE Label2
			JMP ChgSign
		Label2:
			CMP AL,8	;check if bspace is pressed
			JNE Label3
			JMP BSpace
		Label3:
			CMP AL,27	;check if esc is pressed
			JNE Label4
			JMP ClrStr
		Label4:
			CMP AL,48	;check if digit is correct
			JB Incor
			CMP AL,57
			JA Incor
			MOV BL,AL	;getting digit
			SUB BX,48
			MOV AX,DI	;getting whole number
			MUL digit   
			CMP AX,127 
			JA Noverflow    ;check if overflow happened
			ADD AX,BX  
			CMP AX,127
			JA Noverflow
			MOV DI,AX
			JMP Incycle
	Noverflow:
	    CMP AX,128      
	    JNE Coverflow
	    CMP SI,1
	    JNE Coverflow
	    MOV DI,128    
	    CALL Newline
	    JMP Inend
	    Coverflow:
			MOV DX,offset overflowstr
			MOV AH,09h
			int 21h  
			MOV AH,01h
			int 21h
			JMP Clrstr
	ChgSign:
		CMP SI,1	;change sign label
		JE Incycle		;counting minuses
		MOV SI,1
		JMP Incycle
	BSpace:   
		MOV DL,0	;deleting last character
		MOV AH,02h
		int 21h
		MOV DL,8
		MOV AH,02h
		int 21h
		CMP DI,0
		JNE Dellastdigit
		MOV SI,0
		JMP Incycle
	Dellastdigit:
		MOV DX,0	;deleting last digit
		MOV AX,DI
		DIV digit
		MOV DI,AX
		JMP Incycle
	Incor:
		MOV DL,8	;deleting last character
		MOV AH,02h
		int 21h
		MOV DL,0
		MOV AH,02h
		int 21h
		MOV DL,8
		MOV AH,02h
		int 21h
		JMP Incycle
	ClrStr:
		MOV DL,13	;deleting whole line
		MOV AH,02h
		int 21h
		MOV CX,79
		ClrCycle:
			MOV DL,0
			MOV AH,02h
			int 21h		
		loop ClrCycle
		MOV DL,13
		MOV AH,02h
		int 21h
		MOV DI,0
		MOV SI,0
		JMP Incycle
		
	Inend:
	CMP SI,0	;check if number is negative
	JE Posnumber
	MOV AX,DI
    NEG AX
	MOV DI,AX
	Posnumber:
		MOV SP,BP
		POP BP
		POP DX
		POP CX
		POP BX 
		POP AX   
		MOV AX,DI	;moving result to stack
		RET
Insymbol ENDP
	
Outsymbol PROC
	PUSH AX     ;back up of registers
	PUSH BX     ;operand is in stack
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP
	MOV CX,0
	MOV DX,0 
	MOV minussign,DL
	MOV AX,[BP+12]
	TEST AX,AX
    JNS Outcycle
	MOV DX,1
	MOV minussign,DL
	XOR DX,DX 
	NEG AX
	Outcycle:
		DIV digit	;getting next number and print it
		PUSH DX
		MOV DX,0
		INC CX
		CMP AX,0
		JE Outend
		JMP Outcycle
	Outend:  
		CMP minussign,1
		JNE Print	;check if negative
		MOV DL,45
		MOV AH,02h
		int 21h
	Print:
		POP DX 		;printf cycle
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

CustomDiv PROC
;operands  are in al,ah  
XOR CX,CX 
XOR SI,SI
XOR DX,DX	;residue in ax, result in cx
MOV DH,2   
MOV SI,BX
CMP BX,0	;checking zero operand
JNE no_err
errorflow:
MOV CX,0
MOV AX,0
MOV DX,offset Errorstr
MOV AH,09h
int 21h  
MOV AH,01h
int 21h
CALL NewLine
MOV SI,2
JMP div_err
no_err:
	TEST AX,AX	;saving operands signs
	JNS sopergzero 
	MOV DH,1   
	NEG AX    
sopergzero:  
	MOV DL,2
	TEST BX,BX
	JNS fopergzero
	MOV DL,1 
	NEG BX
fopergzero:
	AND DL,DH
	MOV DH,0
	MOV DI,DX
	XOR DX,DX
	SHL BX,8
Divcycle:
	MOV DL,loopcount	;;checking if cycle is over
	CMP DL,0
	JL Divend
	DEC DL
	MOV loopcount,DL
	SUB AX,BX	;checking if divider is less then dividend
	CMP AX,0
	JGE devidend_greater
	ADD AX,BX	;returning old value of dividend
	SHL CX,1	;updating quotient
	JMP devsh 
	devidend_greater:
	SHL CX,1	;increasing quotient
	ADD CX,1
	devsh:
	SHR BX,1	;shifting divider to right of dividend
	JMP Divcycle
Divend: 
    CMP DI,2
    JE correct_anws		;checking if result is greater zero
	CMP DI,1
	JE inc_answ
	NEG CX
	TEST SI,SI
	JNS dec_answ
	JMP correct_anws
inc_answ:
	TEST AX,AX
	JZ correct_anws
	INC CX
	CMP DI,1
	JNE change_residue
	NEG SI
	JMP change_residue
dec_answ:
	TEST AX,AX
	JZ correct_anws
	DEC CX
	JMP change_residue
change_residue:
	CMP AX,0
	JE correct_anws
	NEG AX
	ADD AX,SI
correct_anws:
	XOR SI,SI
	CMP CX,128
	JL right_suit
	JMP errorflow
	right_suit:
	CMP CX,-129
	JG div_err
	JMP errorflow
div_err:
	RET
CustomDiv ENDP

BinaryOut PROC
	PUSH AX     ;back up of registers
	PUSH BX     ;operand is in ax
	PUSH CX 
	PUSH DX 
	PUSH AX  
	MOV DX,offset bytestr
	MOV AH,09h
	int 21h 
	POP AX
	MOV CX,16
	Outcycleb:   
		SHR AX,1	;getting next number and print it
		MOV BX,0  
		JNC bitzero
		MOV BX,1
		bitzero:
		PUSH BX   
		DEC CX
		TEST CX,CX
		JZ Printbbeg
		JMP Outcycleb
	Printbbeg:
	    MOV CX,16
	Printb:
		POP DX 		;printf cycle
		ADD DX,48
		MOV AH,02h
		int 21h
	LOOP Printb
	CALL NewLine
	POP DX
	POP CX
	POP BX 
	POP AX
	RET
Binaryout ENDP
	
start:	
	MOV AX,@DATA                 
	MOV DS,AX        
Testcycle:         
        MOV AL,8
        MOV loopcount,AL
		CALL Insymbol
		MOV CX,AX 
		MOV BX,AX  
		CALL BinaryOut  
		CALL Insymbol
		MOV DX,AX    
		CALL BinaryOut    
		PUSH AX 
		PUSH DX
		MOV DX,offset Divstr
	    MOV AH,09h
	    int 21h 
	    POP DX 
	    PUSH BX
		POP AX
		POP BX
		CALL CustomDiv
		CMP SI,2
		JE Testcycle
		PUSH CX
		CALL OutSymbol   		  
	    POP CX         
	    CALL NewLine
		PUSH AX
		MOV AX,CX
		CALL BinaryOut
		POP AX
		PUSH AX
		PUSH DX
		MOV DX,offset Residuestr
	    MOV AH,09h
	    int 21h 
		POP DX
	    CALL OutSymbol
	    POP AX
		CALL Newline
		CALL BinaryOut
		CALL NewLine
	JMP Testcycle
	MOV AH,4Ch
	int 21h
end start
