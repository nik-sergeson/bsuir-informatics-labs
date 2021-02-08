%начальные условия
syms p;
A=[0 1;-6 5];
t0=0;
Y=[1;1];
func=[0;13*sin(3*p)];
syms lmd t temp x1 x2;
%поиск собств. значений матрицы A
ASymb=sym(A); 
for i=1:1:2
ASymb(i,i)=ASymb(i,i)-lmd;
end;
self_v=solve(det(ASymb));
%формируем матрицы частных решений: решение уравнения (A-v*E)*x=0 11.
E=eye(2,2);
Z=[0;0];
%поиск частного решения X1
K1=A-self_v(1)*E;
tX1=sym(K1)*[x1;x2];
X1=K1\Z;
ta1=K1(1,:)+K1(2,:);
if(ta1(1)*ta1(2)==0)
X1=~double(ta1);
else
X1(1)=1; X1(2)=subs(solve(tX1(1),x2),x1,1); end;
%поиск частного решения X2
K2=A-self_v(2)*E;
tX2=sym(K2)*[x1;x2];
X2=K2\Z;
ta2=K2(1,:)+K2(2,:);
if(ta2(1)*ta2(2)==0)
X2=~double(ta2);
else
X2(1)=1;  X2(2)=subs(solve(tX2(1),x2),x1,1);  
end;
%формируем матрицу F(t) из частных решений X1 и X2
Ft=sym(zeros(2));
Ft(:,1)=X1*exp(self_v(1)*t);
Ft(:,2)=X2*exp(self_v(2)*t);
%упрощаем и выводим
Ft=simplify(Ft);
invft=inv(Ft);
disp('F(t) ='); 
right=Ft*subs(invft,'t',t0)*Y;
left=Ft*int(subs(invft,'t','p')*func,p,t0,t);
disp(right+left);
%F(t) =
  %2*exp(2*t) - exp(3*t) + exp(2*t)*(exp(-2*t)*(3*cos(3*t) + 2*sin(3*t)) - 3) - exp(3*t)*((13*exp(-3*t)*(3*cos(3*t) + 3*sin(3*t)))/18 - 13/6)
 %4*exp(2*t) - 3*exp(3*t) + 2*exp(2*t)*(exp(-2*t)*(3*cos(3*t) + 2*sin(3*t)) - 3) - 3*exp(3*t)*((13*exp(-3*t)*(3*cos(3*t) + 3*sin(3*t)))/18 - 13/6)