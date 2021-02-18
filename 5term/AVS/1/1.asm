.model small
.stack 200h
.data
	a DW 0
	b DW 0       
	adefault DW 0
	bdefault DW 0
	Overflowstr DB ' Overflow $' 
	Sumstr DB 'Sum: $'
	Differstr DB 'Difference: $'
	Bytestr DB 'Binary: $'
	minussign DB 0
	digit DW 10
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

Customneg proc
	PUSH BX	;getting inverse number
	not AX	;operand is in ax   
	CMP AX,32767
	JNE notlimit
	MOV AX,-32768
	JMP negend
	notlimit:
	mov BX,1
	Call CustomAdd
	negend:
	POP BX
	RET
Customneg ENDP

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
			JS Noverflow    ;check if overflow happened
			ADD AX,BX  
			JS Noverflow
			MOV DI,AX
			JMP Incycle
	Noverflow:
	    CMP AX,32768      
	    JNE Coverflow
	    CMP SI,1
	    JNE Coverflow
	    MOV DI,32768    
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
	CALL Customneg
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
	CALL Customneg
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
	

	
HalfAdder proc           
    PUSH DX
    PUSH CX
    ;operands are in ax,bx
	MOV CX,AX
	XOR CX,BX	;getting summ
	MOV DX,AX
	AND DX,BX	;getting carry
	MOV AX,CX	;summ is in ax
	MOV BX,DX	;carry is in bx       
	POP CX
	POP DX
	RET
HalfAdder ENDP
	
FullAdder proc        
    PUSH DX
	;operands are in ax,bx   
	CALL HalfAdder	;incoming carry in cx
	MOV DX,BX
	MOV BX,CX	;incarry and summ in ax,bx
	CALL HalfAdder
	OR BX,DX	;summ is in ax,carry in bx   
	POP DX
	RET	
FullAdder ENDP
	
CustomAdd proc
    ;operands are in ax,bx     
    PUSH DX              
    PUSH CX
	MOV adefault,AX
	MOV bdefault,BX
	PUSH 2	;2 is for indicate numb's digits in stack
	XOR DX,DX
	XOR CX,CX   
	XOR SI,SI
	MOV a,AX
	MOV b,BX
	Addcycle:	;calculating bits of new number
		MOV AX,a
		MOV BX,b
		TEST AX,AX
		JNZ oprjz	;check if numbers are zero
		TEST BX,BX
		JZ Numcalc
	oprjz:
		SHR AX,1	;getting next bits
		MOV a,AX
		MOV AX,1
		JC axbjz
		XOR AX,AX
	axbjz:
		SHR BX,1
		MOV b,BX
		MOV BX,1
		JC bxbjz
		XOR BX,BX
	bxbjz:
		CALL FullAdder 
		MOV CX,BX      
		PUSH AX		;saving bit of summ
		JMP Addcycle
	Numcalc:  
		PUSH CX
		XOR DX,DX
		XOR CX,CX    
	calcansw:
		POP CX
		TEST CX,2	;check if answer is calculated
		JNZ answrd
		SHL DX,1 
		OR DX,CX 
		JMP calcansw  
	summovfl:      
		MOV DX,offset overflowstr
	    MOV AH,09h
	    int 21h    
	    MOV SI,2       
		CALL NewLine
	    JMP negansw
	answrd:
	    MOV AX,adefault
	    MOV BX,bdefault
	    MOV DI,2	;DI=2 if number is positive, DI=1 if number if negative
	    TEST AX,AX
	    JNS axjgz 
	    MOV DI,1	;first operand less zero
	    axjgz:     
		    TEST BX,BX
		    JNS bxjgz
		    AND DI,1	;DI=0 if operands have different signs
		    JMP bxjlz 
	    bxjgz:
		    AND DI,2 ;10 is for plus, 01 for minus	
	    bxjlz: 
		MOV AX,DX
		TEST DI,DI
		JZ negansw	;checking if summ and operands are the same DIgn
		TEST AX,AX
		JNS posansw
		TEST DI,2    ;negative answer
		JNZ summovfl
		JMP negansw
		posansw:   
		TEST DI,1
		JNZ summovfl
		negansw:  
		POP CX       
		POP DX
		RET              
CustomAdd ENDP    

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
		CALL Insymbol
		MOV CX,AX 
		MOV BX,AX  
		CALL BinaryOut  
		CALL Insymbol
		MOV DX,AX    
		CALL BinaryOut    
		PUSH AX 
		PUSH DX
		MOV DX,offset sumstr
	    MOV AH,09h
	    int 21h 
	    POP DX 
	    POP AX
		CALL CustomAdd  
		CMP SI,2
		JE soverfl 
		PUSH AX
		CALL OutSymbol   		  
	    POP AX 
		CALL Newline
		CALL BinaryOut      
		soverfl: 
		MOV BX,CX
		MOV AX,DX       
		CALL CustomNeg 
		PUSH AX 
		PUSH DX
		MOV DX,offset Differstr
	    MOV AH,09h
	    int 21h 
	    POP DX
	    POP AX
		CALL CustomAdd 
		CMP SI,2
		JE Testcycle 
		PUSH AX
		CALL OutSymbol	
		POP AX
		CALL NewLine
		CALL BinaryOut
		CALL NewLine
	JMP Testcycle
	MOV AH,4Ch
	int 21h
end start
