#!/bin/bash
# Safeguards
set -o nounset
set -o errexit
# Get dir of running script
# From http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
# Variables
server=$1
user=$2
current_password=$3
PREVIOUS=${current_password}
for COUNTER in `seq 10 35`
do
	CURRENT=`./passwdgen.py 12`
	echo "Counter at:"${COUNTER}
	echo "Changing "${PREVIOUS}" to:" ${CURRENT}
	# First change it to the temporary password
	echo -e "${PREVIOUS}\n${CURRENT}\n${CURRENT}" | smbpasswd -s -r ${server} -U ${user}
	PREVIOUS=${CURRENT}
done
# Then change it back
echo "Changing "${PREVIOUS}" to:"${current_password}
echo -e "${PREVIOUS}\n${current_password}\n${current_password}" | smbpasswd -s -r ${server} -U ${user}
exit

