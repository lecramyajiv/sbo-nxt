#! /bin/sh

if test -n "$SSH_AGENT_PID"; then
	ssh-agent -k
fi

if test -n "$GPG_AGENT_INFO"; then
	pid=`echo "$GPG_AGENT_INFO" | cut -d: -f2`
	if test -n "$pid"; then
		kill $pid
	fi
fi

