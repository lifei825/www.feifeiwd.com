#!/usr/bin/env sh

cl1=$1

cl=${cl1:=startweb}

if [ $cl == 'startweb' ];then
	echo start web ...
	supervisord  -c /etc/supervisord.conf
else
	exec $@
fi