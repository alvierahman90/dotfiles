source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
for file in $HOME/.zshconfig/*
do
	source "$file"
done
