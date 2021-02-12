#include <stdlib>
#include <string>
#include <stack>
#include <set>
#include <math>
#include "EquSolver.h"
#include "NumberHelper.h"
#include "Table.h"

int EquSolver::Prior(char Symb){
switch (Symb) {
   case '(': return 0;
   case ')':return 0;
   case '+': return 1;
   case '-': return 1;
   case '*': return 2;
   case '/': return 2;
   case '^': return 3;
}
   return 0;
}

char* EquSolver::OBP(char *Equality){
int charpr,j=0;
bool begcell=true;
char symb,symb2,*postform;
bool lastoper=false;
std::stack<char> operat;
postform=(char *)malloc(2*strlen(Equality)*sizeof(char));
strcpy(postform,"");
for(int i=1;i<strlen(Equality);i++){
   symb=Equality[i];
   if(_operations.find<>(symb)==_operations.end()){
      if((symb>='a')&&(symb<='z')){
         operat.push(symb);
      }
      else{
      if(lastoper){
         postform[j]=',';
         j++;
         lastoper=false;
      }
      postform[j]=symb;
      j++;
      }
   }
   else if(operat.empty()){
      operat.push(symb);
      lastoper=true;
   }
   else if(symb=='('){
      operat.push(symb);
      lastoper=true;
   }
   else if(symb==')'){
      lastoper=true;
      symb=operat.top();
      operat.pop();
      while((!(symb=='('))&&(!operat.empty())){
         postform[j]=symb;
         j++;
         symb=operat.top();
         operat.pop();
      }
      if(!operat.empty()){
         if((operat.top()>='a')&&(operat.top()<='z')){
            postform[j]=operat.top();
            operat.pop();
            j++;
         }
      }
   }
   else{
      lastoper=true;
      charpr=Prior(symb);
      while((operat.empty()!=true)&&(charpr<=Prior(operat.top()))){
         symb2=operat.top();
         operat.pop();
         postform[j]=symb2;
         j++;
         }
      operat.push(symb);
   }

}
while(!(operat.empty())){
  symb=operat.top();
  operat.pop();
  if(symb=='('){
     return NULL;
  }
  postform[j]=symb;
  j++;
}
postform[j]='\0';
return postform;
}

double EquSolver::Solve(char* Postform, Table *table){
int j=0,*index;
char ch;
Cell *tempcell;
bool isnumber=false;
double op1,op2,res=0;
std::stack<double> values;
int postlength=strlen(Postform);
char *curoper=new char [11];
if(Postform==NULL)
   return 0;
Postform[postlength]='\0';
for(int i=0;i<postlength;i++){
    ch=Postform[i];
    if(((ch>='A')&&(ch<'=Z'))||((ch>='0')&&(ch<='9'))||(ch==',')){
        if(ch==',')
           continue;
        j=0;
        if(ch>'9'){
           isnumber=false;
        }
        else{
           isnumber=true;
        }
        while(((ch>='A')&&(ch<'=Z'))||((ch>='0')&&(ch<='9'))){
           curoper[j]=ch;
           i++;
           j++;
           ch=Postform[i];
        }
        i--;
        curoper[j]='\0';
        if(isnumber){
            values.push(NumberHelper::DoubleParse(curoper));
        }
        else{
           index=table->GetIndex(curoper);
           tempcell=table->GetCell(index[1]+1,index[0]+1);
           if(NumberHelper::DoubleParse(tempcell->GetData())==0){
              char *temp=tempcell->GetData();
              if(temp[0]=='=')
                 values.push(EquSolver::Solve(EquSolver::OBP(temp),table));
              else
                 return 0;
           }
           else
               values.push(NumberHelper::DoubleParse(tempcell->GetData()));
        }
    }
    else{
       if(values.empty())
           return 0;
       op2=values.top();
       values.pop();
       if((ch>='a')&&(ch<='z')){
          switch(ch){
             case 's':values.push(sin(op2));
             break;
             case 'c':values.push(cos(op2));
             break;
             default: values.push(0);
          }
       continue;
       }
       if(strlen(Postform)==strlen(curoper)+1)
          return op1;
       if(values.empty())
          return 0;
       else
          op1=values.top();
       values.pop();
       switch(ch){
          case '+':res=op1+op2;
          break;
          case '-':res=op1-op2;
          break;
          case '*':res=op1*op2;
          break;
          case '/':res=op1/op2;
          break;
          case '^':res=pow(op1,op2);
       }
       values.push(res);
    }
}
if(!values.empty())
   res=values.top();
delete[] curoper;
return res;
}

