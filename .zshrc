source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"

export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export BETTER_EXCEPTIONS=1
export VIMRUNTIME="/usr/share/vim/current"

prompt agnoster
export GPG_TTY=$(tty)

# status stuff for ZFS, desktop only
if [ "$HOST" = "desktot" ]
then
	cat ~/.zpool.status
	echo ""
	cat ~/.zpool.list

	echo ""
	echo ""
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
