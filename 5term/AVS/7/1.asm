.model small
.386
.stack 200h
.data
	a DD 0
	b DD 0  
	c DD 0
	somenum DD 0
	res 	dd 0
	Bytestr DB 'Binary: $'
	Errorstr DB 'Error $'
	Overflowstr DB ' overflow$'
	Noroot DB 'No root $'
	Rootstr DB 'Root: $'
	Rootsstr DB 'Roots: $'
	Diffstr DB 'Difference: $'
	Nanstr DB 'Nan$'
	digit DD 10
	loopcount DB 8
	minussign DB 0
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

Solve PROC
	CMP a,0	;проверка на то, является ли линейныйм 
	JE linear
	FLD c	;считаем 4ac
	FLD a
	FMUL st(1), st(0)
	FSTP st(0)
	MOV somenum,01000000100000000000000000000000b	;4
	FLD somenum
	FMUL st(1), st(0)
	FSTP st(0)
	FLD b	;загружаем коэффициен b 
	FMUL st(0),st(0)
	FSUB st(0),st(1)
	FSTP somenum	;получили дискриминант
	MOV eax,somenum
	TEST eax,eax
	JZ one_root		;решение о нахождении корней
	JS no_roots
	FLD somenum
	FSQRT	;находим корни
	FLD b
	FCHS
	FSUB st(0),st(1)
	FLD a
	FDIV st(1), st(0)
	FSTP st(0)
	mov somenum,01000000000000000000000000000000b	;2
	FLD somenum
	FDIV st(1), st(0)
	FSTP st(0)
	FSTP somenum	;нашли первый корень
	MOV eax,somenum
	FLD b	
	fchs
	FADD st(0),st(1)
	FLD a
	FDIV st(1), st(0)
	FSTP st(0)
	mov somenum,01000000000000000000000000000000b	;2
	FLD somenum
	FDIV st(1), st(0)
	FSTP st(0)
	fstp somenum
	MOV ebx,somenum		;нашли второй корень
	FSTP st(0)
	MOV DI,2
	RET
one_root:	;у нас только один корень
	FSTP st(0)
	FLD b	;найдем его по формуле
	FCHS
	FLD a
	FDIV st(1), st(0)
	FSTP st(0)
	mov somenum,01000000000000000000000000000000b	;2
	FLD somenum
	FDIV st(1), st(0)
	FSTP st(0)
	FSTP somenum
	MOV eax,somenum
	MOV DI,1	;количество корней
	RET	
no_roots:
	FSTP st(0)	;корней нет
	MOV DI,0
	XOR eax,eax
	XOR ebx,ebx
	RET
linear:		;уравнение линейное
	CMP b,0		;с ним все просто
	JE no_coff
	FLD c
	FCHS
	FLD b
	FDIV st(1),st(0)
	FSTP st(0)
	FSTP somenum
	MOV eax,somenum
	MOV DI,1
	RET
no_coff:	;только один коэффициент
	CMP c,0
	JNE no_roots
	XOR eax,eax
	MOV DI,1
	RET
Solve ENDP

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

infloat proc    
        push    ax
        push    dx
        push    si
        push    bp
        mov     bp, sp
        push    10
        push    0
in_start:
; В SI признак знака.
        xor     si, si
; Начнём накапливать число. Сначала это ноль.
        fldz
; Вводим первый символ. Это может быть минус.
        mov     ah, 01h
        int     21h
        cmp     al, '-'
        jne     iif1
        inc     si
iif0:   mov     ah, 01h
        int     21h
; Если введена точка, то пора переходить
; к формированию дробной части.
iif1:   cmp     al, '.'
        je      iif2
; Ну а если нет, то проверим, что ввели цифру
		cmp al,13
		JE iif5
        cmp     al, 39h
        ja      iif7
        sub     al, 30h
        jb      iif7
        mov     [bp - 4], al
        fimul   word ptr [bp - 2]
        fiadd   word ptr [bp - 4]
        jmp     iif0
;собрались вводить дробную часть
iif2:   fld1
iif3:   mov     ah, 01h
        int     21h
		cmp al,13 
		JE iif4
        cmp     al, 39h
        ja      iif8
        sub     al, 30h
        jb      iif8
; Иначе сохраняем её во временной ячейке,
        mov     [bp - 4], al
; получаем очередную отрицательную степень десятки,
        fidiv   word ptr [bp - 2]
        fld     st(0)
        fimul   word ptr [bp - 4]
        faddp   st(2), st
        jmp     iif3
iif4:   fstp    st(0)
		JMP iif5
; Итак, на вершине стэка получено введённое число.
iif8:
		fstp st(0)
iif7:
		fstp st(0)
		CALL clrstr
		JMP in_start
iif5:   mov     ah, 02h
        mov     dl, 0Dh
        int     21h
        mov     dl, 0Ah
        int     21h
        test    si, si
        jz      iif6
        fchs
iif6:   leave
        pop     si
        pop     dx
        pop     ax
        ret
infloat endp

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
Test_cycle:
	CALL infloat
	fstp a
	CALL infloat
	fstp b
	CALL infloat
	fstp c
	CALL Solve
	CMP DI,0
	JNE has_root
	MOV DX,offset Noroot
	MOV AH,09h
	int 21h 
	CALL NewLine
	JMP Test_cycle
has_root:
	CMP DI,2
	JE two_roots
	PUSH eax
	MOV DX,offset Rootstr
	MOV AH,09h
	int 21h 
	POP eax
	MOV somenum,eax
	fld somenum
	CALL outfloat
	CALL NewLine
	JMP Test_cycle
two_roots:
	PUSH eax
	MOV DX,offset Rootsstr
	MOV AH,09h
	int 21h 
	POP eax
	MOV somenum,eax
	fld somenum
	CALL outfloat
	CALL NewLine
	MOV somenum,ebx
	fld somenum
	CALL outfloat
	CALL NewLine
JMP Test_cycle
	MOV AH,4Ch
	int 21h
end start
