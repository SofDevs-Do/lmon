#!/bin/sh

MACHINEFILE="${1}"

if ! [ -f "${1}" ]; then
    mkdir -p /tmp/lmon
    echo "$(whoami)@127.0.0.1" > /tmp/lmon/temp-machinefile
    MACHINEFILE=/tmp/lmon/temp-machinefile
fi

while read HOST
do
    HOSTPATH=data/"${HOST}/$(date '+%d-%m-%Y')"
    mkdir -p "${HOSTPATH}";
    echo "Collecting from ${HOST}";
    bash cpu-usage.sh "${HOST}" > "${HOSTPATH}"/cpu-usage.csv;
    bash all_normal_users.sh "${HOST}" > "${HOSTPATH}"/all_normal_users.csv;
done < "${MACHINEFILE}"
