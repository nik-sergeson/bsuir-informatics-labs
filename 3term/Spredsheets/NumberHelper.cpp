#include "NumberHelper.h"
#include <stack>
#include <math>

char* NumberHelper::ToString(int number){
std::stack<int> num;
int i=0;
while(number>0){
   num.push(number%10);
   number=number/10;
}
char* outstr=(char *)malloc(num.size()*(sizeof(char)+1));
for(i;i<num.size();i++){
   outstr[i]=48+num.top();
   num.pop();
}
outstr[i]='\0';
return outstr;
}

int NumberHelper::IntParse(char*  string){
int res=0;
for(int i=0;i<strlen(string);i++){
   res=res*10+string[i]-48;
}
return res;
}

bool NumberHelper::GetNum(char *string)
{
int expcount=0,pointcount=0;
if(string==NULL){
   return false;
}
for(int i=0;i<strlen(string);i++)
{
   if((string[i]<'0')||(string[i]>'9')){
       if((string[i]==69)&&(expcount==0)){
          expcount++;
          continue;
       }
       else if((string[i]==44)&&(pointcount==0)){
          pointcount++;
          continue;
       }
       else
         return false;
   }
}
return true;
}

double::NumberHelper::DoubleParse(char *string){
int i=0,mancount=-1;
double Num=0;
if(GetNum(string)){
   while((string[i]!=44)&&(i<strlen(string))){
       Num=Num*10+((int)string[i]-48);
       i++;
   }
   i++;
   while(i<strlen(string)){
      Num=Num+((int)string[i]-48)*pow(10,mancount);
      --mancount;
   }
}
return Num;
}
