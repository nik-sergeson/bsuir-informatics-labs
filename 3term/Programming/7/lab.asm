cseg segment
assume cs:cseg, ds:cseg,ss:cseg,es:cseg
org 100h
start:
jmp initialize
initializer dw 5677h
key_handler proc far
	pushf
	in AL,60h
	push AX
	cmp AL,01h
	jne notesc
	jmp exitkh
notesc:
	cmp AL,1Eh
	jne notleftarrow
	cmp cs:deltax,1
	jne moveleft
	mov cs:deltax,0
	mov cs:deltay,0
	jmp exitkh
	moveleft:
	mov BX,1
	neg BX
	mov cs:deltax,BX
	mov cs:deltay,0
	jmp exitkh
notleftarrow:
	cmp AL,20h
	jne notrightarrow
	mov BX,1
	neg BX
	cmp cs:deltax,BX
	jne moveright
	mov cs:deltax,0
	mov cs:deltay,0
	jmp exitkh
	moveright:
	mov cs:deltax,1
	mov cs:deltay,0
	jmp exitkh
notrightarrow:
	cmp AL,11h
	jne downarrow
	cmp cs:deltay,1
	jne moveup
	mov cs:deltax,0
	mov cs:deltay,0
	jmp exitkh
	moveup:
	mov BX,1
	neg BX
	mov cs:deltax,0
	mov cs:deltay,BX
	jmp exitkh
downarrow:
	cmp AL,1Fh
	jne nomoving
	mov BX,1
	neg BX
	cmp cs:deltay,BX
	jne movedown
	mov cs:deltax,0
	mov cs:deltay,0
	jmp exitkh
	movedown:
	mov cs:deltay,1
	mov cs:deltax,0
exitkh:
	nomoving:
	pop AX
	call dword ptr cs:[i9h_old]
	iret
key_handler endp

timer_handler proc far
	push AX
	push BX
	push CX
	push DX
	push 0A000h
	pop ES
	cmp cs:deltax,0
	jne xnotnull
	jmp xnull
xnotnull:
	mov AX,cs:deltax
	test AX,AX
	jns rightmov
	xor BX,BX
	mov CX,200
checkleft:
	cmp byte ptr es:[bx],2
	je noleftavail
	add BX,320
	loop checkleft
	jmp validleft
noleftavail:
	mov cs:deltax,0
	mov cs:deltay,0
	jmp enddraw
validleft:
	xor BX,BX
	mov CX,319
leftrowcycle:
	push CX
	mov CX,200
leftcolcycle:
	cmp byte ptr es:[bx+1],2
	jne nextnotactive
	mov byte ptr es:[bx],2
	add BX,320
	loop leftcolcycle
	nextnotactive:
	mov byte ptr es:[bx],1
	add BX,320
	loop leftcolcycle
	pop CX
	mov BX,320
	sub BX,CX
	loop leftrowcycle
	mov BX,319
	mov CX,200
	completeleft:
	mov byte ptr es:[bx],1
	add BX,320
	loop completeleft
	jmp enddraw
rightmov:
	xor BX,BX
	mov BX,319
	mov CX,200
checkright:
	cmp byte ptr es:[bx],2
	je norightavail
	add BX,320
	loop checkright
	jmp validright
norightavail:
	mov cs:deltax,0
	mov cs:deltay,0
	jmp enddraw
validright:
	xor BX,BX
	mov BX,319
	mov CX,319
rightrowcycle:
	push CX
	mov CX,200
rightcolcycle:
	cmp byte ptr es:[bx-1],2
	jne rightnextnotactive
	mov byte ptr es:[bx],2
	add BX,320
	loop rightcolcycle
	rightnextnotactive:
	mov byte ptr es:[bx],1
	add BX,320
	loop rightcolcycle
	pop CX
	mov BX,CX
	dec BX
	loop rightrowcycle
	mov BX,0
	mov CX,200
	completeright:
	mov byte ptr es:[bx],1
	add BX,320
	loop completeright
	jmp enddraw
xnull:
	cmp cs:deltay,0
	jne notenddraw
	jmp enddraw
notenddraw:
	mov AX,cs:deltay
	test AX,AX
	jns movdown
	xor BX,BX
	mov CX,320
checkup:
	cmp byte ptr es:[bx],2
	je noupavail
	inc BX
	loop checkup
	jmp validup
noupavail:
	mov cs:deltax,0
	mov cs:deltay,0
	jmp enddraw
validup:
	xor BX,BX
	mov CX,199
uprowcycle:
	push CX
	mov CX,320
upcolcycle:
	cmp byte ptr es:[bx+320],2
	jne upnextnotactive
	mov byte ptr es:[bx],2
	inc BX
	loop upcolcycle
	upnextnotactive:
	mov byte ptr es:[bx],1
	inc BX
	loop upcolcycle
	pop CX
	loop uprowcycle
	mov BX, 63680
	mov CX,320
	completeup:
	mov byte ptr es:[bx],1
	inc BX
	loop completeup
	jmp enddraw
movdown:
	mov BX,63679
	mov CX,320
checkdown:
	cmp byte ptr es:[bx],2
	je nodownavail
	dec BX
	loop checkdown
	jmp validdown
nodownavail:
	mov cs:deltax,0
	mov cs:deltay,0
	jmp enddraw
validdown:
	mov BX,63679
	mov CX,198
downrowcycle:
	push CX
	mov CX,320
downcolcycle:
	cmp byte ptr es:[bx-320],2
	jne downnextnotactive
	mov byte ptr es:[bx],2
	dec BX
	loop downcolcycle
	downnextnotactive:
	mov byte ptr es:[bx],1
	dec BX
	loop downcolcycle
	pop CX
	loop downrowcycle
	mov CX,320
	mov BX,319
	completedown:
	mov byte ptr es:[bx],1
	dec BX
	loop completedown
	enddraw:
	pop DX
	pop CX
	pop BX
	pop AX
	iret
timer_handler endp
	deltax dw 0
	deltay dw 0
	is_installed db 0
	i9h_old dd ?
	timer_old dd ?
initialize:
	mov AX,3509h
	int 21h
	cmp word ptr es:initializer,5677h
	jne notinstalled
	inc cs:is_installed
notinstalled:
	cmp byte ptr ds:[80h],2
	jne not_delete
	cmp byte ptr ds:[82h],'q'
	jne not_delete
	cmp cs:is_installed,1
	je unistallation
	mov ax,cs
	mov ds,ax
	mov dx,offset delete_error
	mov AH,9h
	int 21h
	mov ah,4Ch
	int 21h
unistallation:
	push DS
	cli
	mov DX,word ptr es:[i9h_old]
	mov DS,word ptr es:[i9h_old+2]
	mov AX,2509h
	int 21h
	pop DS
	sti
	mov AX,CS
	mov DS,AX
	mov AH, 9h
	mov DX,offset unistallation_successful
	int 21h
	mov AH,4Ch
	int 21h
not_delete:
	cmp cs:is_installed,1
	jne installation
	mov AX,CS
	mov DS,AX
	mov AH,9h
	mov DX,offset already_installed
	int 21h
	int 20h
installation:
	mov AX,3509h
	int 21h
	mov word ptr cs:i9h_old,BX
	mov word ptr cs:i9h_old+2,ES
	mov AX,2509h
	mov DX,offset key_handler
	int 21h
	mov AX,351Ch
	int 21h
	mov word ptr cs:timer_old,BX
	mov word ptr cs:timer_old+2,ES
	mov AX,251Ch
	mov DX,offset timer_handler
	int 21h
	mov AH,49h
	int 21h
	push DS
	mov AX,CS
	mov DS,AX
	mov DX,offset installation_successful
	mov AH,9h
	int 21h
	pop DS
	mov DX,offset initialize
	int 27h
	already_installed db "Handler is already installed,input 'q' after the programm name","$"
	installation_successful db "Installation is successful","$"
	unistallation_successful db "Unistallation is succesfull","$"
	delete_error db "Resident has not been installed earlier","$"
cseg ends
end start