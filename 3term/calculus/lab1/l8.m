%Обоснование равномерной сходимости функионального ряда
%Ряд x^n/n!, n=1,2..;[-3;3]
syms x eps n;
hold on;
eps=0.5;
x =-3:1/5:3;
plot(x,double(symsum(x.^n/gamma(n+1),n,1,inf))+eps,'-.r');
plot(x,double(symsum(x.^n/gamma(n+1),n,1,inf))-eps,'-.r');
plot(x,double(symsum(x.^n/gamma(n+1),n,1,inf)),'-*m');
N=5;
for i = 1:1:4
    plot(x, double(symsum(x.^n/gamma(n+1), n, 1, N)), '-b');
    N = N + 1;
end;
%N=7