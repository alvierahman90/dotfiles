source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"

export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export BETTER_EXCEPTIONS=1

# prompt cloud "alvie" 
export GPG_TTY=$(tty)

cat ~/.zpool.status

echo ""
echo ""

alias config='/usr/bin/git --git-dir=/home/alvie/Documents/projects/dotfiles.git --work-tree=/home/alvie'
config config --local status.showUntrackedFiles no

alias uarpi="ssh pi@192.168.1.109 'cd /home/pi/holdon-bot; git pull; sudo reboot'"
