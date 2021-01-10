#!/bin/bash

shopt -s nullglob globstar

case "$1" in
	"")
		prefix=${PASSWORD_STORE_DIR-~/.password-store}
		password_files=( "$prefix"/**/*.gpg )
		password_files=( "${password_files[@]#"$prefix"/}" )
		password_files=( "${password_files[@]%.gpg}" )

		printf '%s\n' "${password_files[@]}"
		;;
	*)
		[[ -n $1 ]] || exit
		coproc (sleep 0.1 && pass show "$1" | { IFS= read -r pass; printf %s "$pass"; } |
			xdotool type --clearmodifiers --file - )
		exec 1>&-
esac

