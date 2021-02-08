%Проверка сходимости знакочередующегося ряда
%Ряд (-1)^n/(n*ln(2*n)), n=3,4,...
syms Liman df func n;
i=-1;
assume(n>=3);
func1=(1/(n*log(2*n)));
disp('Проверка признака Лейбница:');
Liman=double(limit(func1,n,inf));
if(Liman==0)
    df=diff(func1,n);   
    if (isAlways(df<0)==1)
        disp('Признак выполняется');
        disp('Проверка интегрального признака');
        i=int(func1,n,3,inf);
        disp('Подсчет несобственного интеграла:');
        disp(i);
        if(isfinite(double(i)))
            disp('Признак выполняется');
            disp('Сходится абсолютно');
        else
            disp('Признак не выполняется');
            disp('Сходится условно');
        end;
    else
        disp('Требуется дополнительное исследование');
    end;               
else
    disp('Признак не выполняется,ряд расходится');
end;
%Результат:ряд сходится условно