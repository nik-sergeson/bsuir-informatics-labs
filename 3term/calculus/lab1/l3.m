%Проверка выполнения признака сходимости Д'аламбера
%Ряд n^n/((n!)^2), n=1,2,...
syms R func n;
func=(n^n/((gamma(n+1))^2));
R=double(limit(subs(func,n+1)/subs(func,n),n,inf));
if(R<1)
    disp('Ряд сходится');
elseif(R>1)
    disp('Ряд рассходится');
else
    disp('Признак ответа не дает');
end;
%Результат:Ряд сходится
