# prompt
PS1='\[\e[1;33m\]${HOSTNAME:0:2} $(echo $PWD | sed -e "s#$HOME#~#" | rev | cut -d '/' -f -2 | rev)\[\e[0;00m\] '

# desktot specfic stuff
#[ "$HOST" = "desktot" ] && echo "Disk stats: " && df -h | head -n 1 && df -h -xtmpfs -xdevtmpfs | tail -n +2 | rev | uniq -f 1 | rev | sort

# dotfile management
DOTFILES_MANAGED=""
[ "$TERM" != "dumb" ] && [ "$HOST" = "desktot" ] && alias gconfig='/usr/bin/git --git-dir=/home/alvie/Documents/projects/dotfiles.git --work-tree=/home/alvie'
[ "$TERM" != "dumb" ] && [ "$HOST" = "desktot" ] && gconfig config --local status.showUntrackedFiles no

source ~/.bash_aliases
source ~/.bash_exports

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/alvie/.sdkman"
[[ -s "/home/alvie/.sdkman/bin/sdkman-init.sh" ]] && source "/home/alvie/.sdkman/bin/sdkman-init.sh"
