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
	cat .zpool.list | \
		tail -n +2 | \
		sed -e "s/  */ /g" | \
		cut -d ' ' -f $1 | \
		sed -n "$2p"
}

# status stuff for ZFS, desktop only
if [ "$HOST" = "desktot" ]
then
	cat ~/.zpool.status
	echo ""
	echo Using $(zpool_info 7 2) of storage, leaving $(zpool_info 4 2) free
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
echo "${NC}"
