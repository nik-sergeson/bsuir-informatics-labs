.model small
.stack 100h
.data
	file_name db 'input.txt',0
	output_file db 'output.txt',0  
	string dw 80 dup(0) 
	outstr dw 80 dup(0)  
	endline db 13,10,'$' 
	numerator dw 80 dup(0)
	nnumetatot dw 2,4,8,3,6,9,1,1,7
	denominator dw 80 dup(0)
	rows db ?
	cols db ?     
	size db ?
	curopnum dw ? 
	curopden dw ?
	factornum dw 1
	factordenom dw 1   
	needswap db 0
	swaptime db 0   
	digit DW 10
	negvalue db 0
.code
    gcd proc   
    PUSH AX
	PUSH BX
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP    
	xor BX,BX
	mov DX,[BP+12]
	mov CX,[BP+14] 
	cmp CX,0
	je zeronum
	test CX,CX
	jns posit 
	inc BX   
	neg CX
	posit:
	cmp DX,CX
	jg greater
	jmp gcdcycle
	greater:
	mov AX,CX  
	mov CX,DX    
	mov DX,AX
	xor AX,AX
	gcdcycle:
	mov AX,CX 
	mov CX,DX
	xor DX,DX
	idiv CX   
	cmp DX,0
	je endgcd
	jmp gcdcycle   
	endgcd:
	xor DX,DX
	mov AX,[BP+12]
	idiv CX
	mov [BP+12],AX  
	xor DX,DX
	mov AX,[BP+14] 
	test AX,AX
	jns notpos
	neg AX
	mov BX,1
	notpos:
	idiv CX
	cmp BX,1
	jne truenotposit
	neg AX
	truenotposit:
	mov [BP+14],AX  
	jmp backup
	zeronum:
	mov [BP+12],DX
	mov [BP+14],CX
	backup: 
	MOV SP,BP
	POP BP
	POP DX
	POP CX
	POP BX 
	POP AX
	RET
    gcd endp
    
    swap proc   
    PUSH AX
	PUSH BX
	PUSH CX 
	PUSH DX
	push DI
	push SI 
	mov SI,DI
	mov BL,[rows]
	sub BX,CX
	xor AX,AX
	mov AL,[rows]   
	xor DX,DX
	mov DL,[swaptime]     
	movecycle:      
	dec DX
	add SI,AX  
	add SI,AX
	cmp DX,0
	jne movecycle
	swapcycle:
	mov AX,numerator[SI]
	mov CX,numerator[DI]
	mov numerator[SI],CX
	mov numerator[DI],AX 
	mov AX,denominator[SI]
	mov CX,denominator[DI]
	mov denominator[SI],CX
	mov denominator[DI],AX
	dec BX
	cmp BX,0
	je endswap
	add SI,2
	add DI,2
	jmp swapcycle
	endswap:   
	pop SI
	pop DI
	POP DX
	POP CX
	POP BX 
	POP AX
	RET
    swap endp
    
    findsi proc
    push BX
    xor BX,BX
	MOV BL,[cols]
	dec CX
	mov AX,CX
	imul BL
	add AX,CX
	mov BL,2
	imul BL  
	mov SI,AX
	inc CX 
	pop BX 
	RET
    findsi endp   
    
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
	mov AX,DX
	stosb
	Print:
		POP DX
		ADD DX,48  
		mov AX,DX
		stosb
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
    
start:
    mov AX, @data
	mov DS, AX
	mov ES, AX  
	mov AH,3Dh
	xor AL,AL
	mov DX,offset file_name 
	int 21h  
	jc exit              
	xor CX,CX
	mov BX,AX
	mov ah,3FH
	mov DX,offset string
	mov CX,80
	int 21h 
	cmp ax,cx;jnz close   
	mov [size],AL
	add bx,ax       
	mov byte ptr string[bx],'$'      
	mov SI,offset string  
	XOR CX,CX    
	xor DX,DX    
	sizeloop1:         
	  xor AX,AX 
	  lodsb
	  cmp AL,' '
	  je endsizeloop1
	  mov CX,AX 
	  sub CX,48
	  mov AL,10
	  mul DL 
	  mov DL,AL
	  add DX,CX
	  jmp sizeloop1
	endsizeloop1:	
	MOV [rows], DL    
	XOR CX,CX    
	xor DX,DX    
	sizeloop2:         
	  xor AX,AX 
	  lodsb
	  cmp AL,' '
	  je endsizeloop2
	  mov CX,AX 
	  sub CX,48
	  mov AL,10
	  mul DL 
	  mov DL,AL
	  add DX,CX
	  jmp sizeloop2	
	endsizeloop2:
	MOV [cols], DL
    XOR AX,AX
	mov BL,[size]
	sub BX,3
	MOV DI,0
	inarr:   
	XOR CX,CX    
	xor DX,DX    
	numloop:    
	  dec BX
	  cmp BX,0
	  je endnum     
	  xor AX,AX 
	  lodsb    
	  push DX
	  push AX
	  mov DX,AX
	  mov AH,02h
	  int 21h
	  pop AX
	  pop DX
	  cmp AL,' '   
	  je endnum    
	  cmp AL,'-'
	  jne notnegative 
	  xor AX,AX        
	  mov AL,1
	  mov [negvalue],AL 
	  jmp numloop
	  notnegative:
	  mov CX,AX 
	  sub CX,48
	  mov AL,10
	  mul DL 
	  mov DL,AL
	  add DX,CX
	  jmp numloop
	  endnum:     
	  mov numerator[DI],DX  
	  mov denominator[DI],1 
	  xor AX,AX
	  mov AL,[negvalue]
	  cmp AL,1
	  jne endenter
	  neg DX
	  mov numerator[DI],DX
	  xor DX,DX
	  mov [negvalue],DL
	  endenter:  
	  mov AX,DI
	  mov DL,2
	  div DL   
	  xor AH,AH
	  mov DL,[rows]
	  div DL   
	  inc AH
	  cmp AH,[rows]
	  jne noenter
	  mov AH,9
	  mov DX,offset endline
	  int 21h     	         
	  noenter:
	  XOR DX,DX
	  ADD DI,2 
	  cmp BX,0
	  je endinarr
	jmp numloop 
	endinarr:  
	xor DX,DX
	xor AX,CX   
	xor BX,DX
	xor CX,CX 
	mov DI,CX 
	detercycle:
	   inc CX  
	   cmp CL,[rows]
	   je enddetcycle
	   call findsi       
	   cmp numerator[SI],0   
	   jne valrow 
	   mov CL,[swaptime]
	   inc CX 
	   mov [swaptime],CL
	   cmp CL,[rows]
	   jne notdetnull
	   xor CX,CX
	   mov [factordenom],CX
	   jmp enddetcycle
	   notdetnull:
	   dec CX     
	   mov DI,SI
	   call swap
	   mov DX,[factornum]
	   neg DX
	   mov [factornum],DX
	   jmp detercycle
	   valrow:   
	   xor AX,AX 
	   mov [swaptime],AL
	   xor DX,DX
	   mov AX,[factornum] 
	   mov BX,numerator[SI]
	   imul BX
	   mov [factornum],AX
	   xor AX,AX
	   xor DX,DX
	   mov AX,[factordenom] 
	   mov BX,denominator[SI]
	   mul BX
	   mov [factordenom],AX  
	   mov BL,[cols]
	   sub BX,CX
	   mov DI,SI
	   normrow:
	   add DI,2   
	   push BX
	   mov AX,denominator[SI]      
	   mov BX,numerator[DI]
	   imul BX
	   mov numerator[DI],AX  
	   pop BX
	   dec BX
	   cmp BX,0
	   ja normrow
	   mov BL,[cols]
	   sub BX,CX
	   mov DI,SI
	   normrow2:
	   add DI,2  
	   push BX
	   mov AX,numerator[SI]
	   test AX,AX
	   jns plussign1
	   neg AX
	   mov BX,numerator[DI] 
	   neg BX
	   mov numerator[DI],BX
	   plussign1:      
	   mov BX,denominator[DI]
	   mul BX
	   mov denominator[DI],AX        
	   pop BX
	   dec BX
	   cmp BX,0
	   ja normrow2
	   mov numerator[SI],1
	   mov denominator[SI],1	
	   add SI,2	
	   mov BL,[cols]
	   sub BX,CX
	   optimrow: 
	   mov AX,numerator[SI]
	   mov DX,denominator[SI]
	   push AX
	   push DX
	   call gcd
	   pop DX
	   pop AX   
	   mov numerator[SI],AX
	   mov denominator[SI],DX
	   dec BX            
	   add SI,2
	   cmp BX,0
	   ja optimrow
	   call findsi
	   mov DI,SI      
	   XOR DX,DX
	   mov DL,[cols]
	   add DI, DX
	   add DI, DX
	   sub DI,CX           
	   sub DI,CX
	   matradd:   ;;;;;;;;;;;;;;;;;;
	   call findsi
	   add DI,CX
	   add DI,CX	
	   mov BL,[cols]
	   sub BX,CX 
	   inc BX   
	   mov AX,numerator[DI]
	   mov DX,denominator[DI]
	   mov [curopnum],AX
	   mov [curopden],DX   
	   xor AX,AX
	   xor DX,DX
	   push CX 
	   rowadd: 
	   push BX
	   mov AX,numerator[DI]  
	   mov BX,denominator[SI]
	   imul BX
	   mov BX,[curopden]
	   imul BX
	   mov CX,AX
	   xor AX,AX
	   mov AX,numerator[SI]
	   mov BX,[curopnum] 
	   imul BX
	   mov BX,denominator[DI]
	   imul BX 
	   sub CX,AX
	   mov numerator[DI],CX
	   xor AX,AX
	   xor DX,DX
	   mov AX,denominator[DI]
	   mov BX,denominator[SI]
	   imul BX
	   mov BX,[curopden]
	   imul BX
	   mov denominator[DI],AX 
	   pop BX  
	   mov AX,numerator[DI]
	   mov DX,denominator[DI];;
	   push AX
	   push DX
	   call gcd
	   pop DX
	   pop AX   
	   mov numerator[DI],AX
	   mov denominator[DI],DX
	   xor CX,CX
	   mov CL,[rows]
	   inc CX
	   add CX,CX
	   mov AX,DI
	   div CL   
	   pop CX
	   cmp AX,CX
	   jne notcentral
	   push CX
	   mov DX,numerator[DI]   
	   cmp DX,0
	   jne notcentral
	   mov CX,2
	   mov [needswap],CL    
	   notcentral:
	   push CX
	   dec BX
	   cmp BX,0
	   je endrowadd
	   add SI,2
	   add DI,2
	   jmp rowadd
	   endrowadd: 
	   mov DL,[needswap]
	   dec DX
	   cmp DX,0
	   jne nocycle
	   mov [needswap],DL 
	   pop CX
	   push CX 
	   push DI      
	   mov DL,[rows]
	   sub DI,DX
	   sub DI,DX 
	   sub DI,DX
	   sub DI,DX
	   add DI,2
	   add DI,CX
	   add DI,CX    
	   xor DX,DX
	   mov DL,1
	   mov [swaptime],DL
	   call swap   
	   xor DX,DX
	   mov [swaptime],DL
	   xor DX,DX
	   mov DX,[factornum]
	   neg DX
	   mov [factornum],DX   
	   pop DI     
	   jmp noswap
	   nocycle: 
	   mov [needswap],DL  
	   noswap:  
	   mov AL,[rows]
	   mov DL,AL
	   mul DL
	   add AX,AX  
	   sub AX,2
	   pop CX
	   push CX
	   cmp AX,DI
	   ja matradd
	   pop CX	     
	jmp detercycle 
	enddetcycle:   
	xor AX,AX
	xor DX,DX       
	mov DL,[rows]
	mov AL,[cols]
	mul DL
	mov CX,AX
	dec CX             
	mov SI,CX
	add SI,CX
	mov AX,[factornum]  
	mov BX,numerator[SI]
	imul BX
	push AX
	mov AX,[factordenom]
	mov BX, denominator[SI]
	mul BX
	push AX
	call gcd
	pop CX
	pop BX     
	xor SI,SI  
	mov DI,offset outstr   
	test BX,BX
	push BX
	call outsymbol 
	pop BX
	mov ah,3Ch           
    mov dx,offset output_file
    xor CX,CX
    int 21h
    mov BX,AX
    mov AH,40h
    mov DX,offset outstr
    mov CL,[size]
    int 21h
	closefile:
	   mov AH,3Eh
	   int 21h  
	MOV AH,01h
	int 21h 
	exit:
	mov ax,4Ch         
    int 21h
end start  