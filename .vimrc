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

" Highlighting cursor position
hi clear cursorline
hi clear cursorcolumn
hi cursorline ctermbg=5 ctermfg=7
hi cursorcolumn ctermbg=5 ctermfg=7

augroup CursorLine
	au!
	au VimEnter,WinEnter,BufWinEnter * setlocal cursorline
	au VimEnter,WinEnter,BufWinEnter * setlocal cursorcolumn
	au WinLeave * setlocal nocursorline
	au WinLeave * setlocal nocursorcolumn
augroup END

" 80 margin
let &cc=join(range(81,999),",")
highlight ColorColumn ctermbg=0

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
	set statusline+=%h
	set statusline+=%w
	set statusline+=%r
	set statusline+=%m
	set statusline+=\ ·\ %f
	set statusline+=\ \ 
	set statusline+=%#warningmsg#
	"" set statusline+=%{SyntasticStatuslineFlag()} " syntastic
	set statusline=%{LinterStatus()}
	set statusline+=%*
	set statusline+=%=
	set statusline+=%L
	set statusline+=\ ·\ 
	set statusline+=%c
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

	" Esc
	map ii <Esc>
	imap ii <Esc>
	vmap ii <Esc>
	cmap ii <Esc>

	" navigating between splits
	nnoremap <C-J> <C-W><C-J>
	nnoremap <C-K> <C-W><C-K>
	nnoremap <C-L> <C-W><C-L>
	nnoremap <C-H> <C-W><C-H>

" Let YouCompleteMe run on any filetype
	let g:ycm_filetype_blacklist = {}

" Special
	let wallpaper  = "/home/alvie/Documents/wallpapers/planet_64.png"
	let background = "#311a38"
	let foreground = "#bbbbd4"
	let cursor     = "#bbbbd4"

" Goyo config
	let g:goyo_width=80
	let g:goyo_height='12'

" Syntastic config
	"" let g:syntastic_always_populate_loc_list = 1
	"" let g:syntastic_auto_loc_list = 0
	"" let g:syntastic_check_on_open = 1
	"" let g:syntastic_check_on_wq = 0
	"" let g:syntastic_python_checkers = ['pylint']
	"" 
	"" let g:syntastic_error_symbol = 'E'
	"" let g:syntastic_style_error_symbol = 'S'
	"" let g:syntastic_warning_symbol = 'W'
	"" let g:syntastic_style_warning_symbol = 's'
	"" 
	"" " Toggling Syntastic's Location pane thingymabob
	"" " https://stackoverflow.com/questions/17512794/toggle-error-location-panel-in-syntastic/17515778#17515778
	"" function! ToggleErrors()
	"" 	let old_last_winnr = winnr('$')
	"" 	lclose
	"" 	if old_last_winnr == winnr('$')
	"" 		" Nothing was closed, open syntastic error
	"" 		" location panel
	"" 		Errors
	"" 	endif
	"" endfunction

	"" nnoremap <silent> <leader>s :<C-u>call ToggleErrors()<CR>
	"" inoremap <silent> <leader>s <Esc>:<C-u>call ToggleErrors()<CR>a

" Nofrils theme config
	colo nofrils-dark
	NofrilsFocusNormal
