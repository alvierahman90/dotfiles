inoremap <buffer> <silent> <leader>c <Esc>:w<Enter>:!render --silent % & <Enter><Enter>a
map <buffer> <silent> <leader>c :w<Enter>:!render --silent % & <Enter><Enter>
map <buffer> <silent> <leader>z :!zathura %.pdf & <Enter><Enter>
inoremap <buffer> <silent> <leader>z <Esc> :!zathura %.pdf &<Enter><Enter>a
nmap <buffer> <leader>n <Plug>(grammarous-move-to-next-error)
nmap <buffer> <leader>g :GrammarousCheck<Enter>
