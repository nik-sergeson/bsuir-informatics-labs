open(DATA, "</windows/Labs/labs.5term/OSS/stuff.txt");
while(<DATA>){
   @temp=split(/ /,$_);
   $data{"$temp[0] $temp[1]"}=$temp[2];
}
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
$year+=1900;
$mon+=1;
@names=keys %data;
foreach $a (@names){
   @temp=split(/\./,$data{$a});
   if(($temp[0]==$mday) && ($temp[1]==$mon) && ($temp[2]==$year)){
      print "Today is meeting with $a\n";
   }
}
sub HaveMeeting{
   if(exists($data{@_[0]})){
      print "You have meeting with @_[0] on $data{@_[0]}";
   }
   else{
      print "You have no meetings with @_[0]";
   }
}
$colname="Tom Savage";
$meet=HaveMeeting($colname);
sub SearchName{
@names=keys %data;
foreach $a (@names){
   if($a=~/[A-Za-z]+ [SG][a-z]+/){
       print "$a $data{$a}";
   }
}
}
SearchName();
%months=('January'=>1,'February'=>2,'March'=>3,'April'=>4,'May'=>5,'June'=>6,'July'=>7,'August'=>8,'September'=>9,'October'=>10,'November'=>11,'December'=>12);
@names=keys %data;
$mon=<STDIN>;
chomp($mon);
foreach $a (@names){
   @temp=split(/\./,$data{$a});
   if($temp[1]==$months{$mon}){
      print "$a\n";
  }
}
