source $HOME/.poetry/env
source "$( poetry env list --full-path | tr -s " " "\012" | head -n 1 )/bin/activate"