" Misc
let mapleader = ";"
set number
set relativenumber
set incsearch
set hlsearch
set lazyredraw
set t_Co=256
set undofile
set undodir=~/Documents/.undodir
set nofoldenable
set laststatus=2

runtime! ftplugin/man.vim
packadd! editexisting

" Keeping the cursor in the center of the screen when possible
augroup VCenterCursor
  au!
  au BufEnter,WinEnter,WinNew,VimResized *,*.*
        \ let &scrolloff=winheight(win_getid())/2
augroup END

" Plugins using vim-plug
call plug#begin('~/.vim/plugged')
Plug 'latex-box-team/latex-box'
Plug 'kien/ctrlp.vim'
Plug 'airblade/vim-gitgutter'
Plug 'altercation/vim-colors-solarized'
"Plug 'spolu/dwm.vim'
Plug 'Valloric/YouCompleteMe'
Plug 'vim-syntastic/syntastic'
Plug 'godlygeek/tabular'
Plug 'tpope/vim-markdown'
Plug 'alvierahman90/nofrils'
Plug 'jamestomasino/vim-conceal'
"Plug 'vim-pandoc/vim-pandoc'
Plug 'vim-pandoc/vim-pandoc-syntax'
" Plug 'rhysd/clever-f.vim'
Plug 'machakann/vim-sandwich'
Plug 'justinmk/vim-sneak'
"Plug 'tmhedberg/SimpylFold'
Plug 'rhysd/vim-grammarous'
Plug 'markonm/traces.vim'
Plug 'tpope/vim-surround'
call plug#end()

" Spelling mistakes 
set spell
hi clear SpellBad
hi SpellBad cterm=underline


" Syntastic config
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 0
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['pylint']

let g:syntastic_error_symbol = 'E'
let g:syntastic_style_error_symbol = 'S'
let g:syntastic_warning_symbol = 'W'
let g:syntastic_style_warning_symbol = 's'

" " Toggling Syntastic's Location pane thingymabob
" " https://stackoverflow.com/questions/17512794/toggle-error-location-panel-in-syntastic/17515778#17515778
function! ToggleErrors()
	let old_last_winnr = winnr('$')
	lclose
	if old_last_winnr == winnr('$')
		" Nothing was closed, open syntastic error
		" location panel
		Errors
	endif
endfunction

nnoremap <silent> <leader>s :<C-u>call ToggleErrors()<CR>
inoremap <silent> <leader>s <Esc>:<C-u>call ToggleErrors()<CR>a

" Statusline
function! GitBranch()
	return system("git rev-parse --abbrev-ref HEAD 2>/dev/null | tr -d '\n'")
endfunction

function! StatuslineGit()
	let l:branchname = GitBranch()
	return strlen(l:branchname) > 0?'  '.l:branchname.' ':''
endfunction

set statusline=""
set statusline+=%{StatuslineGit()}
set statusline+=%h
set statusline+=%w
set statusline+=%r
set statusline+=%m
set statusline+=\ ·\ %f
set statusline+=\ \ 
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
set statusline+=%=
set statusline+=%L
set statusline+=\ ·\ 
set statusline+=%c
set statusline+=\ ·\ 
set statusline+=[%{&fileencoding?&fileencoding:&encoding}]
set statusline+=\[%{&fileformat}\] 

" Remapping keys to use vim-sneak
map f <Plug>Sneak_s
map F <Plug>Sneak_S

" Shortcuts for writing markdown
autocmd filetype markdown inoremap <silent> <leader>c <Esc>:w<Enter>:!render --silent % & <Enter><Enter>a
autocmd filetype markdown map <silent> <leader>c :w<Enter>:!render --silent % & <Enter><Enter>
autocmd filetype markdown map <silent> <leader>z :!zathura %.pdf & <Enter><Enter>
autocmd filetype markdown inoremap <silent> <leader>z <Esc> :!zathura %.pdf &<Enter><Enter>a
autocmd filetype markdown nmap <leader>n <Plug>(grammarous-move-to-next-error)
autocmd filetype markdown nmap <leader>g :GrammarousCheck<Enter>

" Let YouCompleteMe run on any filetype
let g:ycm_filetype_blacklist = {}

" Special
let wallpaper  = "/home/alvie/Documents/wallpapers/planet_64.png"
let background = "#311a38"
let foreground = "#bbbbd4"
let cursor     = "#bbbbd4"

" Colors
let color0  = "#311a38"
let color1  = "#C63E81"
let color2  = "#A25696"
let color3  = "#CB4484"
let color4  = "#E44684"
let color5  = "#7884BC"
let color6  = "#7181C0"
let color7  = "#bbbbd4"
let color8  = "#828294"
let color9  = "#C63E81"
let color10 = "#A25696"
let color11 = "#CB4484"
let color12 = "#E44684"
let color13 = "#7884BC"
let color14 = "#7181C0"
let color15 = "#bbbbd4"

" Splits 
" " Navigation
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" CtrlP shortcuts
nmap <leader>p :CtrlPMixed<Enter>

" Esc map
imap ii <Esc>
