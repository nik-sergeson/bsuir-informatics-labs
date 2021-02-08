.model small
.stack 100h
.data
x0 dw 0
y0 dw 0
x1 dw 50
y1 dw 50
delx dw ?
dely dw ?
s1 dw ?
s2 dw ?	 
changeflag dw ?
error dw ?   
x dw 40
y dw 40 
curx0 dw ?
cury0 dw ?
r dw 10 
delta dw ?
.code
Drawpoint PROC 
    push DX
    push CX
    push BX
    push AX
    xor DX,DX
    xor CX,CX
    mov AH,0Ch 
    mov AL,2
    mov BH,0
    mov CX,x0
    mov DX,y0    
    int 10h      
    pop AX
    pop BX
    pop CX
    pop DX  
    ret
Drawpoint ENDP
      
Sign PROC 
    PUSH AX
	PUSH BX
	PUSH CX 
	PUSH DX
	PUSH BP
	MOV BP,SP
	XOR DX,DX
	XOR AX,AX
	mov AX,[BP+12]
	cmp AX,0   
	je NoSign
	test AX,AX
	jns Abovezero 
	mov DX,0
	dec DX
	jmp CompleteSign
	NoSign:
	mov DX,0
	jmp CompleteSign
	AboveZero:
	mov DX,1
	CompleteSign:
	MOV [BP+12],DX
	MOV SP,BP
	POP BP
	POP DX
	POP CX
	POP BX 
	POP AX
	RET
Sign ENDP

Drawline PROC 
   push DX
   push CX
   push BX
   push AX 
   xor AX,AX
   xor BX,BX
   mov AX,x1
   mov BX,x0
   sub AX,BX
   push AX
   call Sign 
   pop DX
   mov S1,DX
   test AX,AX
   jns dxabovezero
   neg AX
   dxabovezero:  
   mov delx,AX
   mov AX,y1
   mov BX,y0
   sub AX,BX  
   push AX
   call Sign 
   pop DX
   mov S2,DX
   test AX,AX
   jns dyabovezero
   neg AX
   dyabovezero:  
   mov dely,AX 
   mov BX,delx
   cmp AX,BX
   ja dyadx
   mov DX,0
   mov changeflag,DX
   jmp endswap
   dyadx:
   mov delx,AX
   mov dely,BX
   mov DX,1
   mov changeflag,DX
   endswap:
   mov AX,delx
   neg AX
   mov error,AX
   xor CX,CX
   mov CX,delx
   xor AX,AX
   xor BX,BX
   xor DX,DX
   drawcycle:    
   call Drawpoint
   mov AX,error
   mov BX,dely
   add BX,BX
   add AX,BX
   mov error,AX 
   test AX,AX
   js errlzero
   mov AX,x0
   mov BX,y0
   add AX,s1
   mov x0,AX
   add BX,s2
   mov y0,BX
   mov AX,error
   mov BX,delx
   add BX,BX
   sub AX,BX
   mov error,AX
   jmp testcycle   
   errlzero: 
   xor DX,DX
   mov DX,changeflag
   cmp DX,1 
   je ycycle
   mov AX,x0
   add AX,s1
   mov x0,AX
   jmp testcycle
   ycycle:
   mov AX,y0
   add AX,s2
   mov y0,AX
   testcycle:
   loop drawcycle
   pop AX
   pop BX
   pop CX
   pop DX  
   ret 
Drawline ENDP  

Drawcircle PROC 
   push DX
   push CX
   push BX
   push AX
   mov AX,0
   mov curx0,AX 
   mov AX,r
   mov cury0,AX
   add AX,AX
   mov BX,3
   sub BX,AX
   mov delta,BX
   circlecycle:
   mov AX,curx0
   mov BX,cury0
   cmp AX,BX
   jl pass
   jmp endcircle
   pass:   
   mov AX,curx0
   add AX,x
   mov x0,AX
   mov AX,cury0
   add AX,y
   mov y0,AX
   call Drawpoint 
   mov CX,x
   mov DX,y
   add CX,cury0
   add DX,curx0
   mov x0,CX
   mov y0,DX
   call Drawpoint
   mov AX,x
   sub AX,curx0
   mov x0,AX
   mov AX,y
   add AX,cury0
   mov y0,AX
   call Drawpoint   
   mov CX,x
   mov DX,y
   sub CX,cury0
   add DX,curx0
   mov x0,CX
   mov y0,DX
   call Drawpoint
   mov AX,x
   add AX,curx0
   mov x0,AX
   mov AX,y
   sub AX,cury0
   mov y0,AX
   call Drawpoint
   mov CX,x
   mov DX,y
   add CX,cury0
   sub DX,curx0
   mov x0,CX
   mov y0,DX
   call Drawpoint
   mov AX,x
   sub AX,curx0
   mov x0,AX
   mov AX,y
   sub AX,cury0
   mov y0,AX
   call Drawpoint 
   mov CX,x
   mov DX,y
   sub CX,cury0
   sub DX,curx0
   mov x0,CX
   mov y0,DX
   call Drawpoint
   cmp delta,0
   jge delazero
   mov AX,curx0
   mov BX,4
   imul BX
   xor DX,DX
   add AX,6
   mov BX,delta
   add BX,AX
   mov delta,BX
   jmp thirdway
   delazero:
   mov AX,curx0
   mov BX,cury0
   sub AX,BX
   mov BX,4
   imul BX
   xor DX,DX
   add AX,10
   mov BX,delta
   add BX,AX
   mov delta,BX
   mov BX,cury0
   sub BX,1
   mov cury0,BX
   thirdway:
   mov BX,curx0
   add BX,1
   mov curx0,BX
   jmp circlecycle
   endcircle:  
   mov AX,curx0
   add AX,x
   mov x0,AX
   mov AX,cury0
   add AX,y
   mov y0,AX
   call Drawpoint 
   mov AX,y0
   sub AX,cury0
   sub AX,cury0
   mov y0,AX
   call Drawpoint   
   mov BX,x0
   sub BX,curx0
   sub BX,curx0
   mov x0,BX
   call Drawpoint
   add AX,cury0
   add AX,cury0
   mov y0,AX
   call Drawpoint 
   pop AX
   pop BX
   pop CX
   pop DX
      ret
   Drawcircle ENDP
start:
    mov AX,@data
    mov DS,AX
    mov AH,0
    mov AL,13h
    int 10h 
    mov BX,20
    mov CX,150
    mov x0,BX
    mov y0,CX
    mov BX,170
    mov CX,150
    mov x1,BX
    mov y1,CX
    call Drawline
    mov BX,170
    mov CX,150
    mov x0,BX
    mov y0,CX
    mov BX,215
    mov CX,100
    mov x1,BX
    mov y1,CX
    call Drawline
    mov BX,215
    mov CX,100
    mov x0,BX
    mov y0,CX
    mov BX,105
    mov CX,100
    mov x1,BX
    mov y1,CX
    call Drawline
    mov BX,105
    mov CX,100
    mov x0,BX
    mov y0,CX
    mov BX,90
    mov CX,110
    mov x1,BX
    mov y1,CX
    call Drawline
    mov BX,90
    mov CX,110
    mov x0,BX
    mov y0,CX
    mov BX,20
    mov CX,110
    mov x1,BX
    mov y1,CX
    call Drawline 
    mov BX,20
    mov CX,110
    mov x0,BX
    mov y0,CX
    mov BX,20
    mov CX,150
    mov x1,BX
    mov y1,CX
    call Drawline
    mov BX,90
    mov CX,110
    mov x0,BX
    mov y0,CX
    mov BX,90
    mov CX,40
    mov x1,BX
    mov y1,CX
    call Drawline 
	mov BX,90
    mov CX,40
    mov x0,BX
    mov y0,CX
    mov BX,20
    mov CX,110
    mov x1,BX
    mov y1,CX
    call Drawline 
	mov BX,90
    mov CX,40
    mov x0,BX
    mov y0,CX
    mov BX,120
    mov CX,40
    mov x1,BX
    mov y1,CX
    call Drawline 
	mov BX,120
    mov CX,40
    mov x0,BX
    mov y0,CX
    mov BX,105
    mov CX,48
    mov x1,BX
    mov y1,CX
    call Drawline 
	mov BX,105
    mov CX,48
    mov x0,BX
    mov y0,CX
    mov BX,120
    mov CX,56
    mov x1,BX
    mov y1,CX
    call Drawline 
	mov BX,120
    mov CX,56
    mov x0,BX
    mov y0,CX
    mov BX,90
    mov CX,56
    mov x1,BX
    mov y1,CX
    call Drawline 
	mov BX,160
    mov CX,120
	mov DX,10
	mov r,DX
    mov x,BX
    mov y,CX
    call Drawcircle 
	mov BX,115
    mov CX,120
	mov DX,10
	mov r,DX
    mov x,BX
    mov y,CX
    call Drawcircle 
    mov ah,4ch
    int 21h
end start  