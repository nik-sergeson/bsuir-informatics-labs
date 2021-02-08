.model small
.stack 100h
.data
	buf	label byte		
	max	db	255		
	len	db	0	
	source db 255 dup(0)
	words db 255 dup(0)
	inverse db 255 dup(0)
	resultstring db 255 dup(0)
.code
.386
addtoword proc
	push di
	mov di, bx
	nop
	nop
	stosb
	mov bx, di
	pop di
	ret
addtoword endp

pal proc
	push ax
	push dx
	push si
	push di

	lea si, words
	lea di, inverse
	mov cx, 255
	add di, 254
inv:
	cld
	lodsb
	std
	stosb
	loop inv
	
	mov cx, 255
	lea si, words
	lea di, inverse
	cld
	mov ax, 0
	cmp ax, 0
	repz scasb
	dec di
comp:
	lodsb
	push si
	mov dx, ax
	mov si, di
	lodsb 
	mov di, si
	cmp dx, ax
	pop si
	jnz addword
	loop comp
	jmp endpal
addword:
	mov cx, 255
	pop di
	lea si, words
copy:
	lodsb
	cmp ax, 0
	jz space
	stosb
	loop copy
	space:
	mov al, ' '
	stosb
	jmp endnotpal
	endpal:
	pop di
	endnotpal:
	mov ax, 0
	mov cx, 255
	push di
	lea di, words
	rep stosb
	pop di
	lea bx, words
	pop si
	pop dx
	mov dx, 0	
	pop ax
	cmp ax, 0dh
	jz rezult
	ret
pal endp

start:
	mov AX, @data
	mov DS, AX
	cld
	push ds
	pop es
	lea	dx, buf
	mov	ah, 0ah
	int	21h
	lea di, words
	mov bx, di
	lea si, source
	lea di, resultstring
	mov dl, 13
	mov ah, 02h
	int 21h
	mov dl, 10
	mov ah, 02h
	int 21h
cicle:
	xor ax, ax
	lodsb
	cmp	al, 0dh		
	je ifspace
	
	cmp al, ' '
	jz ifspace
	mov dx,1
	call addtoword
	jmp cicle
	ifspace:
	cmp dx,1
	jz callpal
	jnz step
	callpal:
	call pal
	jmp cicle
	step:
	jmp cicle

rezult:
	mov al, '$'
	stosb
	lea dx, resultstring               
	mov ah,09h
	int 21h
	
	mov AH, 4ch
	int 21h
end start
	
