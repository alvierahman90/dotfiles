inoremap <silent> <leader>c <Esc>:w<Enter>:!render --silent % & <Enter><Enter>a
map <silent> <leader>c :w<Enter>:!render --silent % & <Enter><Enter>
map <silent> <leader>z :!zathura %.pdf & <Enter><Enter>
inoremap <silent> <leader>z <Esc> :!zathura %.pdf &<Enter><Enter>a
nmap <leader>n <Plug>(grammarous-move-to-next-error)
nmap <leader>g :GrammarousCheck<Enter>
