#!/bin/bash

echo '先停止tomcat...'
ps aux |grep tomcat |grep -v 'grep tomcat' |awk '{print $2}'|sudo xargs kill -9
wait

echo '成功停止!开始替换class文件'
cd /usr/local/apache-tomcat-8.0.15/webapps/ROOT/WEB-INF/classes/com
rm -rf winhong/
unzip ling.zip
wait
echo '解压成功'
rm -f ling.zip

