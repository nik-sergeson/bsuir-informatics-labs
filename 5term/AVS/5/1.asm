.model small
.386
.stack 200h
.data
	a DD 0
	stacknum DW 0
	b DD 0  
	c DD 0
	dcx DW 0
	res 	dd 0
	Bytestr DB 'Binary: $'
	Errorstr DB 'Error $'
	Overflowstr DB ' overflow$'
	Resstr DB 'Result: $'
	Underflowstr DB 'Underflow$'
	Summstr DB 'Summ: $'
	Diffstr DB 'Difference: $'
	Nanstr DB 'Nan$'
	digit DD 10
	loopcount DB 8
	minussign DB 0
	cmfl dw 0
	mfl dw 0	
	expf dw 0	
	mexfl dw 0 	
	tenconst dt 10
	minusconst dt -1
	symb dw 0
	tenpow db 0
	buf db 50 dup (?)
	datain dd 0
	dataout dt 0
	iscorrect db 0
	leftbit dw 0
	first_bit equ 1000000000000000b
.code

Newline PROC        
    ;procedure to create empty line  
    PUSH EDX
    PUSH ECX
    PUSH EBX
    PUSH EAX
	MOV DL,10	;new line symbol
	MOV AH,02h
	int 21h
	MOV DL,13	;carriage return symbol
	MOV AH,02h
	int 21h   
	POP EAX
	POP EBX
	POP ECX
	POP EDX
	RET
Newline ENDP        

CustomMul PROC 
;operands in ax,bx
	XOR SI,SI
	XOR DI,DI
	XOR ECX,ECX
	XOR EDX,EDX
	CMP eax,0
	JNE first_not_null	;проверка первого операнда на равенство нулю
	JMP null_label
first_not_null:
	cmp ebx,0	;проверка второго операнда на равенстов нулю
	JNE second_not_null
	JMP null_label
second_not_null:
	MOV DX,8
	TEST eax,eax	;выясняем знак первого операнда
	JNS get_first_pow
	MOV SI,1
get_first_pow:
	SHL eax,1	;в цикле достаем порядок первого операнда
	CMP DX,0
	JE process_second
	DEC DX
	shl CX,1
	TEST eax,eax	;получаем первый бит
	JNS get_first_pow
	ADD CX,1
	JMP get_first_pow
process_second:
	PUSH CX		;сохраним порядок в стеке
	MOV CX,8
	TEST ebx,ebx	;выясним знак второго операнда
	JNS get_sec_pow
	MOV DI,1
get_sec_pow:
	SHL ebx,1	;воясним степень второго операнда
	CMP CX,0
	JE sync_opers
	DEC CX
	SHL DX,1
	TEST ebx,ebx	;получаем первый бит
	JNS get_sec_pow
	ADD DX,1
	JMP get_sec_pow
sync_opers:
	POP CX  ;воостанавливаем первый порядок
	SHR eax,9
	OR eax,00000000100000000000000000000000b
	SHR ebx,9
	OR ebx,00000000100000000000000000000000b
	ADD CX,DX
	SUB CX,127	;получаем порядок результата
	XOR edx,edx
	MOV c,ebx
	MUL c
	PUSH edx
	AND edx,00000000000000001000000000000000b	;проверяем результат на денормализацию
	CMP edx,0
	JE mul_carry
	inc CX
mul_carry:
	POP edx
	CMP edx,0
	JE no_nums_edx
shift_edx:	;получаем старшую часть результата
	XOR ebx,ebx
	SHR edx,1
	JNC edx_shift_null
	MOV ebx,10000000000000000000000000000000b
edx_shift_null:
	SHR eax,1	;заносим старшую часть на место
	AND eax,011111111111111111111111111111111b
	OR eax,ebx
	CMP edx,0
	JNE shift_edx
no_nums_edx:
	MOV ebx,eax 
	AND ebx,11111111000000000000000000000000b
	CMP ebx,0	;проверка на денормализацию вправо
	JE normal_result_right
	;нормализуем вправо
	SHR eax,1
	JMP no_nums_edx
normal_result_right:
	MOV ebx,eax		;проверка на денормализацию влево
	AND ebx,11111111100000000000000000000000b
	CMP ebx,0
	JNE normal_result
		;нормализуем влево
	SHL eax,1
	JMP normal_result_right
normal_result:
	CMP CX,254	;проверка на граничные условия
	JGE overflow_label
	CMP CX,0
	JL underflow_label		;потеря значимости
	XOR SI,DI
	SHL SI,8	;собираем первые 9 бит
	OR CX,SI
	SHL ECX,23
	AND eax,00000000011111111111111111111111b
	OR eax,ecx		;собираем все число
	MOV DI,0	;ошибки не было
	RET
nan_label:
	MOV DI,1	;если не число
	MOV DX,offset Nanstr
	MOV AH,09h
	int 21h  
	CALL Newline
	RET
overflow_label:
	CMP eax,0	;любая из бесконечностей
	JNE nan_label
	MOV DI,1
	MOV DX,offset Overflowstr
	MOV AH,09h
	int 21h  
	CALL Newline
	RET
underflow_label:	;потеря значимости
	MOV DI,1
	MOV DX,offset Underflowstr
	MOV AH,09h
	int 21h  
	CALL Newline
	RET
null_label:		;ноль
	XOR eax,eax
	RET
CustomMul ENDP

BinaryOut PROC
	PUSH EAX     ;back up of registers
	PUSH EBX     ;operand is in ax
	PUSH ECX 
	PUSH EDX 
	PUSH EAX  
	XOR ECX,ECX
	XOR EDX,EDX
	MOV DX,offset bytestr
	MOV AH,09h
	int 21h 
	POP EAX
	MOV ECX,32
	Outcycleb:  
		MOV DX,0	
		CMP CX,0
		JE Outcycleb_end
		TEST eax,eax
		JNS next_null
		MOV DX,1
		next_null:
		SHL eax,1
		DEC CX
		ADD DX,48
		MOV AH,02h 
		int 21h
	JMP Outcycleb
	Outcycleb_end:
	CALL NewLine
	POP EDX
	POP ECX
	POP EBX 
	POP EAX
	RET
Binaryout ENDP

clrstr PROC
PUSH eax
PUSH ecx
PUSH edx
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
pop edx
pop ecx
pop eax
clrstr endp

float_input proc ; выход eax - ввод вещественного числа
	xor bx, bx
	xor si,si
	mov mexfl, 0
	lea dx, buf
	mov [buf], 61	;61кол-во символов ограничено тридцатьі
	mov ah, 0ah
	int 21h
	lea si,[buf+2]	;адрес первого значимого символа в строке	
	mov cmfl, 0
	mov mfl, 0
	mov iscorrect, 0
ln0:
	cld 
	lodsb
	cmp al, 101
	jne ln333
	mov expf, 1
	jmp ln2
ln333:
	cmp al,45
	jne ln34
	mov mfl, 1
	jmp ln0
ln34:
	cmp al,46
	jne ln1
	mov cmfl, 1
	jmp ln0	
ln1:
	cmp al, 13
	je ln2
	cmp cmfl, 1
	jne ln0
	inc tenpow
	jmp ln0
ln2:		
	fldz
	lea si,[buf+2]	
step1:
	cld
	lodsb
	cmp al,45
	je step1
	cmp al,46
	je step1
	cmp al, 101
	je step11
	cmp al, 13
	je step2
	cmp al,48
	jb step1
	cmp al,57
	ja step1
	fbld tenconst
	fmul
	mov iscorrect, 1	
	mov byte ptr[symb], al
	sub symb,'0'
	fiadd symb
	jmp step1
step01:
	xor bx, bx
	mov bl, 0
step11:
	cld 
	lodsb
	cmp al,45
	jne ex11
	cmp mexfl, 0
	jne step11
	mov mexfl, 1
	jmp step11
ex11:
	cmp al, 13
	je stepq
	cmp al,38
	jb step11
	cmp al,57
	ja step11
	sub al,'0'
	mov dl, al
	mov al, 10
	mul bl
	add al, dl
	mov bl, al
	jmp step11
stepq:
	cmp mexfl, 1
	je stepz
	jmp step2
stepz:
	add tenpow, bl
	mov bl, 0
step2:
	cmp tenpow, 0
	je step3
	fbld tenconst
	fdiv 
	dec tenpow
	jmp step2 	
step3:
	cmp bl, 0
	je step35
	fbld tenconst
	fmul
	dec bl
	jmp step3
step35:
	cmp mfl, 1
	jne step4
	fbld minusconst
	fmul	
step4:
	fstp datain 
	mov	ecx, datain
	or ecx, 80000000h
	cmp  ecx, 0FF800000h
	jnz  exitt
	mov	iscorrect, 0
	CALL NewLine
	MOV DI,1
	MOV DX,offset Overflowstr
	MOV AH,09h
	int 21h  
exitt:	
	CALL NewLine
	ret
float_input endp

float_input_correct proc ; выход eax - ввод вещественного числа с проверкой корректности
	
float_input_correct_start:
	call float_input
	cmp iscorrect, 1
	je float_input_correct_end
	
	ffree

	jmp float_input_correct_start
	
float_input_correct_end:
	mov eax,datain
ret
float_input_correct endp


outfloat proc
        push    ax
        push    cx
        push    dx
        push    bp
        mov     bp, sp
        push    10
        push    0
; Проверяем число на знак, и если оно отрицательное,
        ftst
        fstsw   ax	;сохранение регистра состояний
        sahf	;запись содержимого регистра ah в младший байт регистра eflags/flags
        jnc     oof1
; то выводим минус
        mov     ah, 02h
        mov     dl, '-'
        int     21h
        fchs
oof1:   fld1                          
        fld     st(1)                  
; Остаток от деления на единицу даст дробную часть.
        fprem                         
        fsub    st(2), st              
        fxch    st(2)                  
; Сначала поработаем с целой частью. Считать количество цифр будем в CX.
        xor     cx, cx
; Поделим целую часть на десять,
oof2:   fidiv   word ptr [bp - 2]     
        fxch    st(1)                  
        fld     st(1)                
        fprem                         
        fsub    st(2), st             
        fimul   word ptr [bp - 2]      
        fistp   word ptr [bp - 4]     
        inc     cx
        push    word ptr [bp - 4]
        fxch    st(1)                  
        ftst
        fstsw   ax
        sahf
        jnz     oof2
        mov     ah, 02h
oof3:   pop     dx
; Вытаскиваем очередную цифру, переводим её в символ и выводим.
        add     dl, 30h
        int     21h
; И так, пока не выведем все цифры.
        loop    oof3                  
; Итак, теперь возьмёмся за дробную часть
        fstp    st(0)                 
        fxch    st(1)                 
        ftst
        fstsw   ax
        sahf
        jz      oof5
        mov     ah, 02h
        mov     dl, '.'
        int     21h
; и не более 38 цифр дробной части.
        mov     cx, 38
oof4:   fimul   word ptr [bp - 2]     
        fxch    st(1)                 
        fld     st(1)                 
        fprem                         
        fsub    st(2), st              
        fxch    st(2)                  
        fistp   word ptr [bp - 4]      
        mov     ah, 02h
        mov     dl, [bp - 4]
        add     dl, 30h
        int     21h
; Теперь, если остаток дробной части ненулевой
        fxch    st(1)                  
        ftst
        fstsw   ax
        sahf
        loopnz  oof4                 
; Итак, число выведено. Осталось убрать мусор из стэка.
oof5:   fstp    st(0)                  
        fstp    st(0)            
        leave
        pop     dx
        pop     cx
        pop     ax
        ret
outfloat endp

start:	
	MOV AX,@DATA           ;20+    -53  
	MOV DS,AX   
	FINIT 
	MOV eax,1
	SHR eax,1
Test_cycle:
	CALL float_input_correct
	PUSH eax
	CALL BinaryOut	
	CALL float_input_correct 
	CALL BinaryOut
	MOV ebx,eax
	POP eax
	CALL CustomMul
	CMP DI,1
	JE Test_cycle
	mov c,eax
	fld c
	CALL outfloat
	CALL NewLine
	MOV eax,c
	CALL BinaryOut
JMP Test_cycle
	MOV AH,4Ch
	int 21h
end start
