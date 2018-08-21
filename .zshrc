GREEN='\033[0;32m'
NC='\033[0m'

echo "${GREEN}"

source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"

export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export BETTER_EXCEPTIONS=1
export VIMRUNTIME="/usr/share/vim/current"

prompt minimal
export GPG_TTY=$(tty)

function zpool_info {
	case "$1" in
		"name") field="1"
			;;
		"size") field="2"
			;;
		"alloc") field="3"
			;;
		"free") field="4"
			;;
		"exapandz") field="5"
			;;
		"frag") field="6"
			;;
		"cap") field="7"
			;;
		"dedup") field="8"
			;;
		"health") field="9"
			;;
		"altroot") field="10"
			;;
		*)
			field="1"
	esac
	cat .zpool.list | \
		tail -n +2 | \
		sed -e "s/  */ /g" | \
		grep "^$2" | \
		cut -d ' ' -f $field
}

function zpool_info_time {
	cat .zpool.list | \
		head -n 1
}

function disk_info {
	case "$1" in
		"filesystem") field="1"
			;;
		"1k-blocks") field="2"
			;;
		"used") field="3"
			;;
		"available") field="4"
			;;
		"usepercentage") field="5"
			;;
		"mountpoint") field="6"
			;;
		*) field="6"
			;;
	esac
	df | sed -e 's/  */ /g' | grep $2$ | cut -d ' ' -f $field
}

# status stuff for ZFS, for computer named 'desktot' only
if [ "$HOST" = "desktot" ]
then
	cat ~/.zpool.status
	echo ""
	echo "Using $(zpool_info cap storage) of zfs pool storage, leaving $(zpool_info free storage) free. It is $(zpool_info frag storage) fragmented."
	for drive in "/home" "/" "/mnt/not_porn"
	do
		if grep -qs "$drive " /proc/mounts; then
			echo "Using $(disk_info usepercentage $drive) of $drive, leaving $(disk_info available $drive) free."
		fi
	done
fi


# dotfile management 
if [ "$HOST" = "desktot" ]
then
	alias config='/usr/bin/git --git-dir=/home/alvie/Documents/projects/dotfiles.git --work-tree=/home/alvie'
fi

if [ "$HOST" = "pi" ]
then
	alias config='/usr/bin/git --git-dir=/root/dotfiles.git --work-tree=/root'
fi

config config --local status.showUntrackedFiles no


alias uarpi="ssh pi 'cd /home/alvie/holdon-bot; git pull; reboot; exit'"
alias xo="xdg-open"
alias pag="ps aux | grep -i"
echo "${NC}"
