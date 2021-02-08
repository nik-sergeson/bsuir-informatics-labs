%Найти область сходимости функционального ряда
%Ряд 3^n*x^(3*n)*sin(3*x/n^0.5); n=2,3..
syms func converges Lx x interv mfunc1 mfunc2 arsize liman r leftbord rightbord preint;
func=(3^n)*((x^3)^n)*sin(3*x/(n^0.5));
assume(n>=2);
schng=false;
Lx=3*abs((x^3));
mfunc1=1/n^0.5;%ряды для предельного признака
mfunc2=1/n^2;
interv=[];
str='';
preint=solve(Lx-1,x);%находим корни
preint=sort(preint);%сортируем по позрастанию
rightbord=preint(1);%проверяем интервал от бесконечности до первого корня
if(subs(Lx,(double(rightbord)-abs(double(rightbord))/2))<1)
    %проверяем среднее значение интервала
    interv(1,size(interv)+1)=-inf;
    interv(1,size(interv)+1)=rightbord;
end;
leftbord=rightbord;
arsize=size(preint);
for k=2:1:arsize(1)% проверям все интервалы, граничными точками
    %которых являются найденные корни
    rightbord=preint(k);
    if((subs(Lx,((double(leftbord)+double(rightbord))/2))<1))
        interv(1,size(interv)+1)=leftbord;
        interv(1,size(interv)+1)=rightbord;
    end;
    leftbord=rightbord;
end;
if((subs(Lx,(double(leftbord)+abs(double(leftbord))/2))<1))
    %проверяем последний интервал
    interv(1,size(interv)+1)=leftbord;
    interv(1,size(interv)+1)=inf;
end;
arsize=size(interv);
for k=1:1:arsize(2)%проверяем, сходится ли исходный ряд на границах
    %интервалов
    func1=subs(func,x,interv(k));%проверка на знакочередующийся
    func1=simplify(func1);
    if(interv(k)<0)
        schng=true;
    end;
    Liman=double(limit(func1,n,inf));
    if(Liman==0)
        if(schng==true)
            func1=abs(func1/((-1)^n));
            r=double(limit(func1/mfunc2,n,inf));%проврека на
            %абсолютную сходимость
            if((r>0)&isfinite(r))
                converges=true;
            else
                df=diff(func1,n);%проверка Лейбница   
                if (isAlways(df<0)==1)
                    converges=true;
                else
                    converges=false;
                end;   
            end;
             schng=false;
        else
            r=double(limit(func1/mfunc2,n,inf));%проверка обычного ряда
            if((r>0)&isfinite(r))
                converges=true;
            else
                r=double(limit(func1/mfunc1,n,inf));
                if((r>0)&isfinite(r))
                    converges=false;
                end;
            end;
        end;            
    else
        converges=false;
    end;
    if(mod(k,2)==1)%если число стоит на нечетном месте, необходима 
        %открывающая скобка, если на четном-закрывающая
        if(converges==true)
            str=sprintf('%s[%g;',str,(interv(k)));
        else
            str=sprintf('%s(%g;',str,(interv(k)));
        end;
    else
         if(converges==true)
            str=sprintf('%s%g]',str,(interv(k)));
         else
            str=sprintf('%s%g)',str,(interv(k)));
        end;
        if(k<arsize(2))%проверяем, остались ли еще интервалы
            str=sprintf('%sU',str);
        end;
    end;
end;
disp('Область сходимости:');
disp(str);
%Область сходимости:[-0.693361;0.693361)