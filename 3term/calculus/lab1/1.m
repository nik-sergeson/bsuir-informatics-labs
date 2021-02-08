%Подсчет суммы числового ряда
%Ряд 2/(n*(n+1)*(n+2)), n=1,2,...
syms S L n;
S=symsum((2/(n*(n+1)*(n+2))),n,1,n);
L=limit(S,n,inf);
disp('Сумма числового ряда:');
disp(L);
%Результат:0.5