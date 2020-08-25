" compile
inoremap <buffer> <silent> <leader>c <Esc>:w<Enter>:!render --silent "%" & <Enter><Enter>a
map <buffer> <silent> <leader>c :w<Enter>:!render --silent "%" & <Enter><Enter>

" open zathura
map <buffer> <silent> <leader>z :!zathura "%.pdf" & <Enter><Enter>
inoremap <buffer> <silent> <leader>z <Esc> :!zathura "%.pdf" &<Enter><Enter>a

" move to next grammar error
nmap <buffer> <leader>n <Plug>(grammarous-move-to-next-error)

" check for grammar errors
nmap <buffer> <leader>g :GrammarousCheck<Enter>

" create a new (sub)section
imap <leader>h1 <Enter><Enter>#<Space>
imap <leader>h2 <Enter><Enter>##<Space>
imap <leader>h3 <Enter><Enter>###<Space>
imap <leader>h4 <Enter><Enter>####<Space>
imap <leader>h5 <Enter><Enter>#####<Space>
imap <leader>h6 <Enter><Enter>######<Space>
