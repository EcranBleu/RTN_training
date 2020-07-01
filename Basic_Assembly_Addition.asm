; basic assembly file that takes 2 digits, adds them together and prints them on the screen via a function

global _start

section .data

	initString db "Please enter the first number:", 0x0a
	initStringL equ $-initString
	secondString db "Please enter the second number:", 0x0a
	secondStringL equ $-secondString
	resultString db "The result of the addition is:", 0x0a
	resultStringL equ $-resultString

section .bss
	
	num1: resb 0x400
	num2: resb 0x400
	num3: resb 0x400

section .text

BasicMath:

	;epilog
	push ebp
	mov ebp, esp


	;print initString
	mov eax, 0x4
	mov ebx, 0x1
	mov ecx, initString
	mov edx, initStringL
	int 0x80

	;read input
	mov eax, 0x3
	mov ebx, 0x2
	mov ecx, num1
	mov edx, 0x400
	int 0x80

	;print secondString
	mov eax, 0x4
	mov ebx, 0x1
	mov ecx, secondString
	mov edx, secondStringL
	int 0x80

	;read second input
	mov eax, 0x3
	mov ebx, 0x2
	mov ecx, num2
	mov edx, 0x400
	int 0x80

	;addition
	mov al, [num1]
	add al, [num2]
	mov [num3], al
	int 0x80

	;print resultString
	mov eax, 0x4
	mov ebx, 0x1
	mov ecx, resultString
	mov edx, resultStringL
	int 0x80

	;print actual result
	mov eax, 0x4
	mov ebx, 0x1
	mov ecx, num3
	mov edx, 0x400
	int 0x80	
	
	;prelog
	mov esp, ebp
	pop ebp
	ret


_start:	

	pushad
	pushfd

	call BasicMath

	popfd
	popad


	;exit program
	mov eax, 0x1
	mov ebx, 0x0
	int 0x80

	

