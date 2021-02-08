syms n x;
hold on;
func = '(x-1)^3';
a0 = int((x-1)^3, -pi,pi) / pi;%Коэффициент a0
assume(n, 'integer');
simplify(sin(2*pi*n) + cos(x));
an = simple(int(sym(func * cos(n*x)), x, -pi,pi) / pi);%Коэффициент an
bn = simple(int(sym(func * sin(n*x)), x, -pi,pi) / pi);%Коэффициент bn
x_new = -pi : pi / 25 : pi;
sum = subs(a0 /2, 'x', x_new);
%Подсчёт частичной суммы
for n = 1 : 1 : 5
sum = sum + subs(an*cos(n*x) + bn*sin(n*x), 'n', n);%Накопление суммы
end;
plot(x_new, subs(sum, x_new));%Печать решения
sum = subs(a0 / 2, 'x', x_new);
for n = 1 : 1 : 20
sum = sum + subs(an*cos(n*x) + bn*sin(n*x), 'n', n);
end;
plot(x_new, subs(sum, x_new),'-ok');
sum = subs(a0 / 2, 'x', x_new);
for n = 1 : 1 : 50
sum = sum + subs(an*cos(n*x) + bn*sin(n*x), 'n', n);
end;
plot(x_new, subs(sum, x_new),'-xk');
%Оформление графика
title(char(['Частичтные суммы ряда ', char(a0 / 2), ' + ', 'sum(', char(an*cos(n*x) + bn*sin(n*x)), ')'])); %Титульная надпись графика
legend('5-ая частичная сумма', '20-ая частичная сумма', '50-ая частичная сумма'); %Легенда графика

%Амплитудный спектр
An = simple((an^2 + bn^2)^0.5);
n = 0 : 1 : 20;
figure;
bar(n, subs(An, n), 0.3);
title(['Амплитудный спектр, An = ', char(An)]);

%Частотный спектр
fin = simple(atan(bn/an));
figure;
bar(n, double(subs(fin, n)), 0.3);
title(['Частотный спектр, fin = ', char(fin)]);