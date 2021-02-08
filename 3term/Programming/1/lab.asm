.model small
.stack 100h
.data
	a dw 1h
	b db 2h
	c dw 3
	d dw 4
	e dw 5
	f db 6
	min dw 0
	max dw 0
.code
start:
	mov AX,0 
	mov AL,1
	imul b
	cmp AX,a
	jl le1th2
	mov AX,a
	
	le1th2:
		cmp AX,c
		jl wrax
		mov AX,c
	wrax: mov min,AX
	
	mov AX,0 
	mov AL,f
	imul f
	mov BX,AX
	mov AL,f
	mov AH,0
	imul BX
	
	cmp AX,d
	jg gr1th2
	mov AX,d
	
	gr1th2:
		cmp AX,e
		jg wrgrax
		mov AX,e
	wrgrax: mov max,AX
	imul min
	
	mov ah,1
	int 21h
end start
