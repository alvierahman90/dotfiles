# prompt
PS1='\[\e[1;33m\]${HOSTNAME:0:2} $(echo $PWD | sed -e "s#$HOME#~#" | rev | cut -d '/' -f -2 | rev)\[\e[0;00m\] '

# desktot specfic stuff
[ "$HOST" = "desktot" ] && echo "Disk stats: " && df -h | head -n 1 && df -h -xfuse.rclone -xtmpfs -xdevtmpfs | tail -n +2 | rev | uniq -f 1 | rev | sort

# dotfile management
DOTFILES_MANAGED=""
[ "$TERM" != "dumb" ] && [ "$HOST" = "desktot" ] && alias gconfig='/usr/bin/git --git-dir=$HOME/Documents/projects/dotfiles.git --work-tree=$HOME'
[ "$TERM" != "dumb" ] && [ "$HOST" = "desktot" ] && gconfig config --local status.showUntrackedFiles no

source ~/.bash_aliases
source ~/.bash_exports

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
