.model small
.stack 200h
.data
	a DW 0
	b DW 0       
	Overflowstr DB ' Overflow $' 
	Multstr DB 'Result: $'
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

CustomMultipl PROC
;operands  are in al,ah
XOR BX,BX
;result in cl
XOR CX,CX 
XOR SI,SI
XOR DX,DX ;last bit of multiplier in DL 
MOV DH,2
TEST AL,AL
JNS sopergzero 
MOV DH,1   
NEG AL    
sopergzero:  
MOV DL,2
TEST AH,AH
JNS fopergzero
MOV DL,1 
NEG AH
fopergzero:
AND DL,DH
MOV DH,0
MOV DI,DX
MOV CL,AL     
MOV AL,AH
XOR DX,DX
NEG AL	;getting negative first operand
Multplcycle:
	MOV DH,loopcount	;checking if cycle is over
	CMP DH,0
	JE Multplend
	DEC DH
	MOV loopcount,DH
	PUSH CX		;getting penultimate bit of multiplier
	SHR CL,1
	POP CX
	JC patt1x	;choosing pattern
	CMP DL,0
	JE patt00
	ADD CH,AH    ;end of a group of 1
	MOV BL,0
	patt00:		;part of a group of 0
		MOV DL,0
		JMP endxx
	patt1x:
		CMP DL,1	
		JE patt11
		ADD CH,AL	;beginning of a group of 1
		TEST AL,AL
		JZ patt11
		MOV BL,128
	patt11:		;part of a group of 1
		MOV DL,1
	endxx:
		SHR CX,1   
		ADD CH,BL
JMP Multplcycle
Multplend: 
    CMP DI,0
    JNE answgzero
    NEG CX
    answgzero:
	CMP CX,127
	JG Multpl_overfl
	CMP CX,-128
	JGE correct_anws
Multpl_overfl:
	MOV DX,offset overflowstr
	MOV AH,09h
	int 21h 
	MOV CX,0
	MOV SI,2
correct_anws:
	RET
CustomMultipl ENDP

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
	MOV AH,0
	MOV AL,5
	Call CustomMultipl
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
		MOV DX,offset Multstr
	    MOV AH,09h
	    int 21h 
	    POP DX 
	    POP AX      
	    MOV AH,BL
		CALL CustomMultipl
		CMP SI,2
		JE Testcycle
		PUSH CX
		CALL OutSymbol   		  
	    POP CX
		CALL Newline
		CALL BinaryOut      
	JMP Testcycle
	MOV AH,4Ch
	int 21h
end start
