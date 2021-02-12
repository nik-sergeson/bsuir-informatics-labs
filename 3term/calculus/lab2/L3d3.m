clf;
syms x y LeftPart RightPart InHequation; % Инициализация
syms Title Message;
syms x_new y_new;
%	Нахождение решения
LeftPart = 'D2y-5*Dy+6*y';
RightPart = '13*sin(3*x)';
InHequation = [LeftPart, '=', RightPart];
y = simplify(dsolve(InHequation, 'x'));
Title = ['Phase portrait:', char(InHequation)];
Message = ['y = ', char(y)]; 
dy=diff(y,'x');
Message2 = ['y = ', char(dy)];
x_new= meshgrid([ -2 : 0.1 : 2 ]);
y=subs(y,'x',x_new);
dy=subs(dy,'x',x_new);
y_new = subs(y, 'C2', val);
dy_new = subs(dy, 'C2', val);
y_new = subs(y_new, 'C3', val);
dy_new = subs(dy_new, 'C3', val);
y_new = real(double(subs(y_new, x_new)));
dy_new = real(double(subs(dy_new, x_new)));
surf(y_new,dy_new,x_new);

