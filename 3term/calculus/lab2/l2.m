clf;
syms x y Ur Title % инициализация символьных переменных
syms x_new y_new Expr Message
assume(y>0);
Ur = '-4*x*y+2*x*exp(-x^2)*y^0.5'; % задан. прав. части уравнен.
Expr = ['Dy = ', char(Ur)]; % формирование дифффер. уравнения
y = dsolve(Expr, 'x'); % решение дифференциального уравнения
fprintf('y = ');
imy=y(1);
y=y(2);
Message = ['y=', char(y)];
Message2 = ['y=', char(imy)];
pretty(simplify(y)); % печать решения уравнения
grid on; hold on;	% включаем координатную сетку
xlabel('X axis'); % подписываем ось OX
ylabel('Y axis'); % подписываем ось OY
x_new = 0:0.1:5; % формируем сетку значений аргументов
y = subs(y, 'x', x_new); % подставляем аргументы
for cycle = -5 : 1 : 5 % варьируем значения произв. константы
val = cycle;
y_new = subs(y,val); % подставляем	константу
plot(x_new, y_new); % прорисовка интегральной кривой
end;
plot(x_new,imy);
Title = ['Integral Curves of Equation: ', char(Expr)];
title(char(Title)); % титульная надпись графика
legend(char(Message),char(Message2)); % легенда графика
