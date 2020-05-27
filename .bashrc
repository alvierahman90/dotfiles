# prompt
PS1='${HOSTNAME:0:2} $(echo $PWD | sed -e "s#$HOME#~#" | rev | cut -d '/' -f -2 | rev) '

# desktot specfic stuff
#[ "$HOST" = "desktot" ] && echo "Disk stats: " && df -h | head -n 1 && df -h -xtmpfs -xdevtmpfs | tail -n +2 | rev | uniq -f 1 | rev | sort

# dotfile management
[ "$HOST" = "desktot" ] && alias gconfig='/usr/bin/git --git-dir=/home/alvie/Documents/projects/dotfiles.git --work-tree=/home/alvie'
gconfig config --local status.showUntrackedFiles no

# aliases 
alias xo="xdg-open"
alias pag="ps aux | grep -v grep | grep -i "
alias paig="ps aux | grep -iv grep | grep -i "
alias tt="cat ~/timetable"
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
alias dc="docker-compose"
alias ftc="xclip -selection clipboard -i"
alias tv="ranger ~/Downloads/Torrents/TV.Shows/"

alias commit="git commit -m"
alias add="git add"
alias status="git status"

# exports
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export BETTER_EXCEPTIONS=1
export VIMRUNTIME="/usr/share/vim/current"
export GOPATH="$HOME/gopath"
export PATH="$PATH:/home/$USER/bin:$GOPATH:$GOPATH/bin:$PATH"
export GPG_TTY=$(tty)
