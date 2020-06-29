# prompt
PS1='\[\e[1;33m\]${HOSTNAME:0:2} $(echo $PWD | sed -e "s#$HOME#~#" | rev | cut -d '/' -f -2 | rev)\[\e[0;00m\] '

# desktot specfic stuff
#[ "$HOST" = "desktot" ] && echo "Disk stats: " && df -h | head -n 1 && df -h -xtmpfs -xdevtmpfs | tail -n +2 | rev | uniq -f 1 | rev | sort

# dotfile management
DOTFILES_MANAGED=""
[ "$TERM" != "dumb" ] && [ "$HOST" = "desktot" ] && alias gconfig='/usr/bin/git --git-dir=/home/alvie/Documents/projects/dotfiles.git --work-tree=/home/alvie'
[ "$TERM" != "dumb" ] && [ "$HOST" = "desktot" ] && gconfig config --local status.showUntrackedFiles no

# aliases 
alias xo="xdg-open"
alias pag="ps aux | grep -v grep | grep -i "
alias paig="ps aux | grep -iv grep | grep -i "
alias dc="docker-compose"
alias ftc="xclip -selection clipboard -i"
alias tv="ranger ~/Downloads/Torrents/TV.Shows/"
alias ..="cd .."
alias v="vim"
alias sl="ls"
alias lyrics='less "$(echo Music/$(mpc -f "%file%" status | head -n1) | rev | cut -d. -f2- | rev).lrc"'

alias g="git"
alias commit="git commit -m"
alias add="git add"
alias status="git status"

alias ls="ls -h --color=always"
alias ll="ls -l"
alias la="ll -A"

alias cal="cal -m"
alias c="cal -3"
alias cy="cal -y"

source ~/.bash_exports
