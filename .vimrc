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
Plug 'spolu/dwm.vim'
Plug 'vim-scripts/CycleColor'
Plug 'tpope/vim-fugitive'
Plug 'Valloric/YouCompleteMe'
Plug 'vim-syntastic/syntastic'
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'
Plug 'sjl/gundo.vim'
call plug#end()

let NERDTreeShowHidden=0

set laststatus=2

"let g:lightline = {
      "\ 'colorscheme': 'solarized'
      "\ }
let g:dwm_master_pane_width=84

nmap <1> :NERDTreeToggle<CR>

let &colorcolumn=80
highlight ColorColumn ctermbg=1 

hi clear SpellBad
hi SpellBad cterm=underline

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
