syms x n a0 an bn cn f func s

hold on;

title('Обратная задача');

%находим коэффициенты
an = (1/pi) * int((x-1)^3 * cos(n*x), x, -pi, pi);
bn = (1/pi) * int((x-1)^3 * sin(n*x), x, -pi, pi);

%формируем функцию
cn(x, n) = (an - i * bn)/2;
func = (an^2+bn^2)^0.5 * exp(i * atan(bn/an) * x);
f(x,n) = func;

for i=-pi:0.01:pi %строим график на Ox от -pi до pi
s = 0;
for n = 1:1:20 %находим 20ю частичную сумму
s = s + f(i, n);
end;
plot(i, s);
end;