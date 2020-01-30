execute pathogen#infect()

set encoding=utf-8
set nocompatible
filetype on
filetype plugin on
filetype indent on
syntax on

set autoindent
set tabstop=2
set shiftwidth=2
set expandtab
set number
set hlsearch
set cursorline

" Allow hidden buffers (multiple files).
set hidden
set laststatus=2

set incsearch
set hlsearch

autocmd FileType python setlocal tabstop=4 shiftwidth=4 colorcolumn=80
autocmd FileType java setlocal tabstop=4 shiftwidth=4 colorcolumn=100
autocmd FileType cpp setlocal tabstop=2 shiftwidth=2 colorcolumn=80

autocmd BufNewFile,BufReadPost *.md set filetype=markdown
autocmd FileType markdown setlocal spell

" Quicker buffer switching
map gn :bn<cr>
map gp :bp<cr>
map gd :bd<cr>

" Airline stuff
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t\%M'
let g:airline_powerline_fonts = 1
