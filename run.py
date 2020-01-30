#!/usr/bin/env python3

def prompt(string):
    input(string)

def package_installs():
    for pack in ["git", "vim", "tmux", "zsh", "meld", "ripgrep"]:
        prompt("Install {} (sudo apt-get install {})".format(pack, pack))
    prompt("Install fd (sudo apt-get install fd-find / pacman -S fd")

def git_setup():
    prompt("Copy over the gitconfig (cp .gitconfig ~/.gitconfig)")

def zsh_setup():
    prompt('Install oh-my-zsh\n  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
    prompt("Change the prompt to 'agnoster' (vim ~/.zshrc)")
    prompt("Clone zsh-syntax-highlighting\n  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting")
    prompt("Clone zsh-autosuggestions\n  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    prompt("Add 'git', 'wd', 'zsh-syntax-highlighting' and 'zsh-autosuggestions' to plugins (vim ~/.zshrc)")

def vim_setup():
    prompt('Copy over .vimrc (cp .vimrc ~)')
    prompt("""Install pathogen:
    mkdir -p ~/.vim/autoload ~/.vim/bundle && \\
    curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim""")
    prompt("""Install vim-airline:
    git clone https://github.com/vim-airline/vim-airline ~/.vim/bundle/vim-airline""")

if __name__ == "__main__":
    package_installs()
    zsh_setup()
    vim_setup()
    prompt("Set colour scheme to solarized.")
    prompt("Install powerline (TODO)")
    prompt("Setup tmux (TODO)")
    prompt("Create an SSH key (TODO)")
    prompt("Add SSH key to GitHub (TODO)")
