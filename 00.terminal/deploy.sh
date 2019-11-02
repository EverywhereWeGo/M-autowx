#!/bin/bash

destpath="/opt/wangchong"
host="172.24.5.242"
port="3222"
username="root"
password="rGk/UAgZVvU="

src_file="${outputDirectory}"
dest_file="${destpath}/${project.name}"

while getopts ":cdrlh" opt
do
    case ${opt} in
        c)
            clean=true
            ;;
        d)
            deploy=true
            ;;
        r)
            restart=true
            ;;
        l)
            log=true
            ;;
        h)
            echo "usage:-c -d -r -l lib cofig *.jar / (_* to all) ·"
            exit 1
            ;;
        ?)
            echo "存在非法参数"
            echo "usage:-c -d -r -l lib cofig *.jar / (_* to all) ·"
            exit 1
            ;;
    esac
done
#通过shift $(($OPTIND - 1))的处理，$*中就只保留了除去选项内容的参数，
#可以在后面的shell程序中进行处理
shift $(($OPTIND - 1))
#如果需要上传文件则必须有多余的参数
if [[ "true" = ${deploy} ]]; then
remaining_parameters="$*"
if [[ $# -eq 0 ]];then
echo "参数错误:未传文件名"
echo "usage:-c -d -r -l lib cofig *.jar / (_* to all) "
exit 1
fi
fi




#清空目标文件夹
clean(){
if [[ ${#dest_file} -gt `expr ${#destpath}+1` ]] ;then
exe="ssh -p ${port} ${username}@${host} rm -rf ${dest_file}/*"
myecpect "${exe}"
fi
}

#上传文件
deploy(){
if [[ "_*" = "$1" ]];then
echo asdf
exe="bash -c \"scp -r -P ${port} ${src_file}/* ${username}@${host}:${dest_file}/\""
#直接打印变量的话*会被替换，加双引号解决问题
myecpect "${exe}"
else
for i in $*
do
exe="bash -c \"scp -r -P ${port} ${src_file}/$i ${username}@${host}:${dest_file}/\""
#直接打印变量的话*会被替换，加双引号解决问题
myecpect "${exe}"
done
fi
}


#重启
restart(){
exe="ssh -p ${port} ${username}@${host} chmod 777 ${dest_file}/bin/*.sh && ${dest_file}/bin/restart.sh"
myecpect "${exe}"
}

#查看日志
log(){
exe="ssh -p ${port} ${username}@${host} tail -f ${dest_file}/log.log"
myecpect "${exe}"
}

myecpect(){
expect << EOF
set timeout -1
spawn $1
 expect {
 "(yes/no)?"
  {
    send "yes\n"
    expect "*assword:" { send "$password\n"}
  }
 "*assword:"
  {
    send "$password\n"
  }
}
expect eof
EOF
}



if [[ "true" = ${clean} ]]; then clean ; fi
if [[ "true" = ${deploy} ]]; then deploy ${remaining_parameters} ; fi
if [[ "true" = ${restart} ]];then restart ; fi
if [[ "true" = ${log} ]];then log ; fi






