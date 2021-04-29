clf;
syms x y LeftPart RightPart InHequation; % Инициализация
syms Title Message;
syms x_new y_new;
%	Нахождение решения
LeftPart = 'D2y+y';
RightPart = '1/sin(x)';
InHequation = [LeftPart, '=', RightPart];
y = simplify(dsolve(InHequation, 'x'));
fprintf('y = ');pretty(y); % Печать решения
%	График решения
Title = ['Integral Curves of Equation:', char(InHequation)];
Message = ['y = ', char(y)]; 
x_new = -2*pi : 0.1 : 2*pi;
for cycle1 = -5 : 1 : 5
val = cycle1;
y_new = subs(y, 'C2', val);
for cycle2 = -5 : 1 : 5
val = cycle2;
y_new = subs(y_new, 'C1', val);
y_new = real(double(subs(y_new, x_new)));
plot(x_new, y_new);
legend(char(Message));
hold on; end;end;
grid on;
title(char(Title));
xlabel('X axis');
ylabel('Y axis');
