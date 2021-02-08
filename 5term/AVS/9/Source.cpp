// Lab9.cpp : Defines the entry point for the console application.
//

#include <ctime>
#include <cstdlib>
#include <stdio.h>


int main()
{
	__int8 A[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	__int8 B[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	__int8 C[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	__int16 D[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	__int16 E[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
	printf("A  =   ");
	for (int i = 0; i < 8; i++)
	{
		printf("%d\t", A[i]);
	}

	printf("\n\nB  =   ");
	for (int i = 0; i < 8; i++)
	{
		printf("%d\t",B[i]);
	}

	printf("\n\nC  =   ");
	for (int i = 0; i < 8; i++)
	{
		printf("%d\t", C[i]);
	}
	_asm {
		;A-B
		movq MM0, qword ptr [A]
		movq MM1, qword ptr [B]
		movq MM2, qword ptr [C]
		psubsb MM0,MM1
		paddsb MM0,MM2	;result in MM0
		movq qword ptr [A],MM0
		;converting A 8->16
		movq MM1,qword ptr [A]	;saving result
		pxor MM2,MM2	;xor for test
		pcmpgtb MM2,MM1	;test for null
		movq MM0,qword ptr [A]
		punpcklbw MM0,MM2	;unpack low byes
		movq qword ptr [E],MM0
		movq MM1,qword ptr [A]
		pxor MM2,MM2	;xor for test
		pcmpgtb MM2,MM1	;test for null
		movq MM0,qword ptr [A]
		punpckhbw MM0,MM2	;unpack high bytes
		movq qword ptr [E+8],MM0		
		movq MM0,qword ptr [E]	;add right part
		movq MM1,qword ptr [D]	
		paddsw MM0,MM1
		movq MM1,qword ptr [E+8]	;add left part
		movq MM2,qword ptr [D+8]
		paddsw MM1,MM2
		movq qword ptr [E],MM0	;saving result in E
		movq qword ptr [E+8],MM1
		;emmms	
	}
	printf("\n(A-B)+(C+D)");
	printf("\n\nE  =   ");
	for (int i = 0; i < 8; i++)
	{
		printf("%d\t", E[i]);
	}

	system("Pause");
	return 0;
}

