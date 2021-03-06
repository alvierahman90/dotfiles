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
	set ignorecase
	set bs=2
	set title
	colo default

	runtime! ftplugin/man.vim
	packadd! editexisting

augroup CursorLine
	au!
	au VimEnter,WinEnter,BufWinEnter * setlocal cursorline
	au VimEnter,WinEnter,BufWinEnter * setlocal cursorcolumn
	au WinLeave * setlocal nocursorline
	au WinLeave * setlocal nocursorcolumn
augroup END

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
	"" Plug 'spolu/dwm.vim'
	Plug 'Valloric/YouCompleteMe'
	Plug 'godlygeek/tabular'
	Plug 'tpope/vim-markdown'
	Plug 'robertmeta/nofrils'
	Plug 'jamestomasino/vim-conceal'
	"" Plug 'vim-pandoc/vim-pandoc'
	Plug 'vim-pandoc/vim-pandoc-syntax'
	""  Plug 'rhysd/clever-f.vim'
	Plug 'machakann/vim-sandwich'
	Plug 'justinmk/vim-sneak'
	"" Plug 'tmhedberg/SimpylFold'
	Plug 'rhysd/vim-grammarous'
	Plug 'markonm/traces.vim'
	Plug 'tpope/vim-surround'
	Plug 'w0rp/ale'
	Plug 'junegunn/goyo.vim'
	Plug 'morhetz/gruvbox'
	call plug#end()

" Spelling mistakes 
	set spell
	hi clear SpellBad
	hi SpellBad cterm=underline

" Statusline
	function! GitBranch()
		return system("git rev-parse --abbrev-ref HEAD 2>/dev/null | tr -d '\n'")
	endfunction

	function! StatuslineGit()
		let l:branchname = GitBranch()
		return strlen(l:branchname) > 0?'  '.l:branchname.' ':''
	endfunction

	function! LinterStatus() abort
		let l:counts = ale#statusline#Count(bufnr(''))

		let l:all_errors = l:counts.error + l:counts.style_error
		let l:all_non_errors = l:counts.total - l:all_errors

		return l:counts.total == 0 ? 'No errors' : printf(
			\   '%d warning(s), %d error(s)',
			\   all_non_errors,
			\   all_errors
			\)
	endfunction


	set statusline=""
	set statusline+=%{StatuslineGit()}
	set statusline+=%h " help buffer flag [Help]
	set statusline+=%w " preview window flag [Preview]
	set statusline+=%r " readonly flag [RO]
	set statusline+=%m " Modified plag [+] or [-]
	set statusline+=%#warningmsg#
	"" set statusline+=%{SyntasticStatuslineFlag()} " syntastic
	set statusline+=%{LinterStatus()}
	set statusline+=%*
	set statusline+=%= " left/right separator 
	set statusline+=%L " number of lines in buffer
	set statusline+=\ 
	set statusline+=(%p%%) " percentage through file
	set statusline+=\ ·\ 
	set statusline+=%c " current column
	set statusline+=\ ·\ 
	set statusline+=%f " file path relative to current directory
	set statusline+=\ ·\ 
	set statusline+=[%{&fileencoding?&fileencoding:&encoding}]
	set statusline+=\[%{&fileformat}\] 

" ALE config
	let b:ale_linters = { 'python': ['pylint'] }

	let g:ale_echo_msg_error_str = "ERROR"
	let g:ale_echo_msg_warning_str = "WARNING"
	let g:ale_echo_msg_format = "[%linter%][%severity%] %s"

	let g:ale_sign_error = '!'
	let g:ale_sign_warning = '?'
	let g:ale_sign_style_error = 'S!'
	let g:ale_sign_style_warning = 'S?'

" Maps
	" ALE
	nmap <silent> <leader>n <Plug>(ale_next_wrap)
	nmap <silent> <leader>e <Plug>(ale_previous_wrap)

	" keys to use vim-sneak
	map f <Plug>Sneak_s
	map F <Plug>Sneak_S

	" CtrlP
	nmap <leader>p :CtrlPMixed<Enter>

	" navigating between splits
	nnoremap <C-J> <C-W><C-J>
	nnoremap <C-K> <C-W><C-K>
	nnoremap <C-L> <C-W><C-L>
	nnoremap <C-H> <C-W><C-H>

" Let YouCompleteMe run on any filetype
	let g:ycm_filetype_blacklist = {}

" Goyo config
	let g:goyo_width=100
	let g:goyo_height=25
" vimscrot
	command Screenshot !~/.vim/shell_scripts/vimscrot.sh
" Switch HL / ^$ for faster movement
	noremap H ^
	noremap L $
	noremap ^ H
	noremap $ L

" listchars
	set list
	set listchars=nbsp:_,tab:<·>,extends:>,space:·
	hi clear listchar

" Highlighting cursor position
hi clear cursorline
hi clear cursorcolumn
"hi cursorline ctermbg=2 ctermfg=0
"hi cursorcolumn ctermbg=2 ctermfg=0

" 100 margin
let &cc=join(range(101,999),",")
highlight ColorColumn ctermbg=0

" colorscheme
autocmd vimenter * ++nested colorscheme gruvbox
set background=dark
let g:gruvbox_contrast_dark='soft'
