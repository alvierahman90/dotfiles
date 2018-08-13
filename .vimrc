set number
set relativenumber
set incsearch
set hlsearch
set lazyredraw
set t_Co=256
set spell
set undofile
set undodir=~/Documents/.undodir
runtime! ftplugin/man.vim

packadd! editexisting

augroup VCenterCursor
  au!
  au BufEnter,WinEnter,WinNew,VimResized *,*.*
        \ let &scrolloff=winheight(win_getid())/2
augroup END

call plug#begin('~/.vim/plugged')
Plug 'latex-box-team/latex-box'
Plug 'scrooloose/nerdtree'
Plug 'kien/ctrlp.vim'
Plug 'airblade/vim-gitgutter'
Plug 'altercation/vim-colors-solarized'
"Plug 'spolu/dwm.vim'
Plug 'vim-scripts/CycleColor'
Plug 'tpope/vim-fugitive'
Plug 'Valloric/YouCompleteMe'
Plug 'vim-syntastic/syntastic'
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'
Plug 'sjl/gundo.vim'
Plug 'alvierahman90/nofrils'
Plug 'jamestomasino/vim-conceal'
"Plug 'vim-pandoc/vim-pandoc'
Plug 'vim-pandoc/vim-pandoc-syntax'
Plug 'tpope/vim-eunuch'
Plug 'dbeniamine/cheat.sh-vim'
" Plug 'rhysd/clever-f.vim'
Plug 'machakann/vim-sandwich'
Plug 'tpope/vim-abolish'
Plug 'justinmk/vim-sneak'
"Plug 'tmhedberg/SimpylFold'
call plug#end()

augroup pandoc_syntax
	au! BufNewFile,BufFilePre,BufRead *.md set filetype=markdown.pandoc
augroup END

let NERDTreeShowHidden=0

set laststatus=2

"let g:lightline = {
      "\ 'colorscheme': 'solarized'
      "\ }
let g:dwm_master_pane_width=84

nmap <1> :NERDTreeToggle<CR>


hi clear SpellBad
hi SpellBad cterm=underline


let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['pylint']


let g:nofrils_alt_heavylinenumbers=1


" statusline
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

map f <Plug>Sneak_s
map F <Plug>Sneak_S

autocmd filetype markdown inoremap ;c <Esc>:w<Enter>:!render --silent % & <Enter><Enter>a
autocmd filetype markdown map ;c :w<Enter>:!render --silent % & <Enter><Enter>

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
