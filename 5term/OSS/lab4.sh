a=10
let b="$a+5"
echo $b
c=`ls /windows/ | wc -l`
echo $c
arr[0]=0
arr[1]=1
for i in 2 3 4 5 6 7 8 9 10
do
arr[$i]=`expr ${arr[(($i-1))]} + ${arr[(($i-2))]}`
done 
echo "10's Fibonachi number: ${arr[10]}"
maxn()
{
if [ "$1" -gt "$2" ];then
return $1
else
return $2
fi
}

maxn 10 3
echo "max(10,3)=$?"
 a=123
 ( a=321; )
 echo "a = $a" 
