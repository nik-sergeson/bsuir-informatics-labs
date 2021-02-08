%Проверка выполнения необходимого признака сходимости
%Ряд 1/(n^2-log(n)), n=1,2,...
syms L func cfunc1 cfunc2 ml1 ml2 n;
func= 1/(n^2-log(n));
cfunc1=1/n^2;
cfunc2=1/n;
L=limit(func,n,inf);
if(L==0)
    disp('Необходимый признак выполняется');
    ml1=double(limit((func/cfunc1),n,inf));
    ml2=double(limit((func/cfunc2),n,inf));
    if (ml1>0)&(ml1~=inf)
        disp('Ряд сходится');
    elseif (ml2>0)&(ml2~=inf)
            disp('Ряд расходится');
    else
        disp('Требуется дополнительное исследование');
    end;
else
    disp('Необходимый признак не выполняется, ряд расходится');
end;
%Результат: Необходимый признак выполняется. Ряд сходится.