find $1 -mindepth 3 -type d|wc -l>/1/data
echo directs>>/1/data
find $1 -type f|wc -l>>/1/data
echo files>>/1/data
echo $(date)>>/1/data
echo $(hostname)>>/1/data
