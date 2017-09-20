#!/bin/bash

LIU_ID="matlu703"
HOST="remote-und.ida.liu.se"
HDIR="/home/$LIU_ID/Documents/"
LDIR="$(pwd)/remote_und_$LIU_ID/"

echo "Mounting $HDIR @ $HOST to local directory " $LDIR
mkdir $LDIR
sshfs $LIU_ID@$HOST:$HDIR $LDIR
while true; do
	read -p "Unmount (Y)? " y
	case $y in
		[Yy]* ) break;
	esac
done
echo "* Cleaning up..."
while true; do
	if fusermount -u $LDIR; then
		rm -rfi $LDIR
		echo "* Done."
		break
	else
		read -p "Could not unmount, try again? (N) " n
		case $n in
			[Nn]* ) echo "* Did not remove folder" $LDIR
							break
		esac
	fi
done