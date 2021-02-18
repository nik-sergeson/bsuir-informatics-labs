.model small
.386
.stack 200h
.data
	a DD 0
	b DD 0  
	h DD 0
	eps DD 0
	funcvalue DD 0
	seriesvalue DD 0
	countvalue DD 0
	somenum DD 0
	Fxstr DB 'F(x)= $'
	Errorstr DB 'Error $'
	Sxstr DB 'S(x)= $'
	Anstr DB 'a= $'
	Nstr DB 'N= $'
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

SeriesCount PROC
XOR ecx,ecx		;подсчет суммы раяда
FLDZ		;изначально сумма ноль
FSTP seriesvalue	;обнуляем прошлое значение
FLD1
FSTP somenum
MOV ecx,somenum
FLD a	;ряд будем находить реккурентно 
FLD a
FMUL st(1),st(0)	;заносим начальный член
FMUL st(1),st(0)
FSTP st(0)
FLD st(0)
MOV somenum,ecx
FLD somenum
FMUL st(0),st(0)
MOV somenum,01000000100000000000000000000000b	;4
FLD somenum
FMUL st(1),st(0)
FSTP st(0)
MOV somenum,00111111100000000000000000000000b	;1
FLD somenum
FSUB st(1),st(0)
FSTP st(0)
FDIV st(1),st(0)
FSTP  st(0)	;собираем общее значение и сохраняем его 
FLD seriesvalue
FADD st(0),st(1)
FSTP seriesvalue
FSTP st(0)
count_cycle:	;цикл подсчета ряда с заданной точностью
	FLD seriesvalue
	FLD funcvalue	
	FSUB st(0),st(1)	;проверим достижение заданной точности
	FABS
	FLD eps
	FSUB st(1),st(0)
	FSTP st(0)
	FSTP somenum
	FSTP st(0)
	MOV eax,somenum
	TEST eax,eax
	JS end_series_count		;если да-закончим вычисление суммы ряда
	JZ end_series_count
	MOV somenum,ecx
	FLD somenum		;в соотвествии с реккурентным соотношение получаем слагаемое
	FLD1
	FADD st(1),st(0)
	FSTP st(0)
	FSTP somenum
	MOV ecx,somenum
	FLD a
	FMUL st(1),st(0)
	FMUL st(1),st(0)
	FSTP st(0)
	FCHS
	FLD st(0)
	MOV somenum,ecx		;измененную часть считаем заново
	FLD somenum
	FMUL st(0),st(0)
	MOV somenum,01000000100000000000000000000000b	;4
	FLD somenum
	FMUL st(1),st(0)
	FSTP st(0)
	MOV somenum,00111111100000000000000000000000b	;4n-1
	FLD somenum
	FSUB st(1),st(0)
	FSTP st(0)
	FDIV st(1),st(0)
	FSTP  st(0)
	FLD seriesvalue		;полное слагаемое
	FADD st(0),st(1)
	FSTP seriesvalue
	FSTP st(0)
	JMP count_cycle	
end_series_count:
	FSTP st(0)
	RET
SeriesCount ENDP

Solve PROC
;x is in (-1;1)-область сходимости
func_count_cycle:
	FLD a
	MOV somenum,01000000000000000000000000000000b	;2
	FLD somenum 	;посчитаем значение функции по формуле
	FDIV st(1),st(0)	;x/2
	FSTP st(0)
	FLD a
	FLD1
	FPATAN ;арктангенс
	FLD a
	FMUL st(0),st(0)
	FLD1
	FADD st(1),st(0)
	FSTP st(0)
	MOV somenum,01000000000000000000000000000000b	;2
	FLD somenum 
	FDIV st(1),st(0)	;(1+x^2)/2
	FSTP st(0)
	FMUL st(1),st(0)
	FSTP st(0)
	FSUB st(1),st(0)
	FSTP st(0)
	FCHS
	FSTP funcvalue
	CALL SeriesCount	;посчитаем сумму ряда
	MOV countvalue,ecx
	MOV DX,offset Anstr		;выведем полученные значения
	MOV AH,09h
	int 21h 
	FLD a
	CALL outfloat
	CALL NewLine
	MOV DX,offset Fxstr
	MOV AH,09h
	int 21h 
	FLD funcvalue
	CALL outfloat
	CALL NewLine
	MOV DX,offset Sxstr
	MOV AH,09h
	int 21h 
	FLD seriesvalue
	CALL outfloat
	CALL NewLine
	MOV DX,offset Nstr
	MOV AH,09h
	int 21h 
	fld countvalue
	CALL outfloat
	CALL NewLine
	CALL NewLine
	FLD a	;перейдем к следующему значение переменной
	FLD h
	FADD st(1),st(0)
	FSTP st(0)
	FST a
	FLD b
	FSUB st(1),st(0)
	FSTP st(0)
	FSTP somenum	;проверим, не зашли ли мы за границу
	MOV eax,somenum
	TEST eax,eax
	JNS end_func_count
	JZ end_func_count
	JMP func_count_cycle
end_func_count:	
	RET
Solve ENDP

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
	fstp h
	CALL infloat
	fstp eps
	CALL Solve
	
JMP Test_cycle
	MOV AH,4Ch
	int 21h
end start
