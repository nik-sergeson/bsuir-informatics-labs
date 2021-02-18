BEGIN{
count=0;
count2=0;
}
{
n=split($3,array,"/");
if(array[3]=="2014") {
   meets[array[2],array[1]]=$1" "$2;
}
++count2;
}
{
++count;
print count ":" count2;
}
END{
print "Dan collegues"
for(i in meets){
  split(i,sep,SUBSEP);
  if(meets[sep[1],sep[2]]~/Dan .*/)
    print(meets[sep[1],sep[2]]);  
}
print "2nd name starting with S or G"
for(i in meets){
  split(i,sep,SUBSEP);
  if(meets[sep[1],sep[2]]~/[A-Za-z]+ [SG][a-z]+/){
    split(meets[sep[1],sep[2]],temparr," ");
    print(temparr[2]); 
} 
}

print "Meetings in June"
for(i in meets){
  split(i,sep,SUBSEP);
  if(sep[1]==6){
     print(meets[sep[1],sep[2]]);  
}
}
print count;
}
