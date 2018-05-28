source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"

export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export BETTER_EXCEPTIONS=1

prompt agnoster
export GPG_TTY=$(tty)

cat ~/.zpool.status
echo ""
cat ~/.zpool.list

echo ""
echo ""

alias config='/usr/bin/git --git-dir=/home/alvie/Documents/projects/dotfiles.git --work-tree=/home/alvie'
config config --local status.showUntrackedFiles no

alias uarpi="ssh pi 'cd /home/alvie/holdon-bot; git pull; sudo reboot; exit'"
