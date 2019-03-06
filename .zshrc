source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
for file in $HOME/.zsh/config/*
do
	source "$file"
done
