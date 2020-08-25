alias o="open"
alias xo="xdg-open"

alias v="vim"

alias sb="source ~/.bashrc"

alias be="bmon -p eno1"
alias dc="docker-compose"
alias pag="ps aux | grep -v grep | grep -i "
alias lyrics='less "$(echo Music/$(mpc -f "%file%" status | head -n1) | rev | cut -d. -f2- | rev).lrc"'

alias ..="cd .."
alias ...="cd ../.."

alias g="git"
alias ga="git add"
alias gc="git commit -m"
alias gs="git status"
alias gp="git push"

alias ls="ls -h --color=always"
alias sl="ls"
alias la="ll -A"
alias ll="ls -l"
alias lrt="ll -rt"

alias c="cal -3"
alias cy="cal -y"
alias cal="cal -m"
