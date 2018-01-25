# The following lines were added by compinstall
zstyle :compinstall filename '/home/matti/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=6666
setopt autocd extendedglob
bindkey -e
# End of lines configured by zsh-newuser-install

# ------
# Prompt
# ------

# <Copypasta from https://ianloic.com/2011/06/25/git-zsh-prompt/>

setopt prompt_subst
autoload colors zsh/terminfo
colors

function __git_prompt {
  local DIRTY="%{$fg[yellow]%}"
  local CLEAN="%{$fg[green]%}"
  local UNMERGED="%{$fg[red]%}"
  local RESET="%{$terminfo[sgr0]%}"
  git rev-parse --git-dir >& /dev/null
  if [[ $? == 0 ]]
  then
    echo -n "["
    if [[ `git ls-files -u >& /dev/null` == '' ]]
    then
      git diff --quiet >& /dev/null
      if [[ $? == 1 ]]
      then
        echo -n $DIRTY
      else
        git diff --cached --quiet >& /dev/null
        if [[ $? == 1 ]]
        then
          echo -n $DIRTY
        else
          echo -n $CLEAN
        fi
      fi
    else
      echo -n $UNMERGED
    fi
    echo -n `git branch | grep '* ' | sed 's/..//'`
    echo -n $RESET
    echo -n "]"
  fi
}

# </Copypasta>

PS1='%B%F{green}%n@%m%b%f:%F{blue}%~%f$ '
RPS1='$(__git_prompt)'

# ---------------
# Auto Completion
# ---------------

zstyle ':completion:*' menu select

# -------
# Aliases
# -------

alias ls='ls --color'
alias hgrep='history | grep'
