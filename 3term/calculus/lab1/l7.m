%Обоснование равномерной сходимости функионального ряда по определению
%Ряд (-1)^n*x^n/(6*n-8), n=1,2..
syms x eps func n;
hold on;
eps=0.1;
rn = 1/(6*(n+1)-8);
sol = solve(rn - eps);
N = floor(sol) + 1;
x =0:1/10:1;
plot(x,double(symsum((-1).^n.*x.^n/(6*n-8),n,1,inf))+eps,'-.r');
plot(x,double(symsum((-1).^n.*x.^n/(6*n-8),n,1,inf))-eps,'-.r');
plot(x,double(symsum((-1).^n*x.^n/(6*n-8),n,1,inf)),'-*k');
for i = 1:1:5
    plot(x, double(symsum((-1).^n.*x.^n/(6*n-8), n, 1, N)), '-b');
    N = N + 1;
end;