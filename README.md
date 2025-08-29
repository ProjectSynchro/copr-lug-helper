> ⚠️ **Notice:**  
> This project has migrated to **[Codeberg](https://codeberg.org/Synchro/copr-lug-helper)**. 

### COPR repo for the Star Citizen Linux User Group's lug-helper script.
For more info check out the LUG wiki:  [https://starcitizen-lug.github.io](https://starcitizen-lug.github.io)

### *Greetings, fellow Penguin!*
_**This script is designed to help you manage and optimize Star Citizen on Linux.**_

Zenity menus are used for a GUI experience with a fallback to terminal-based menus where Zenity is unavailable.  
Command line arguments are available for quickly launching functions from the terminal.

Configuration is saved in *$XDG_CONFIG_HOME/starcitizen-lug/*  
Keybinds are backed up to *$XDG_CONFIG_HOME/starcitizen-lug/keybinds/*

## To Install
* Activate the repo with `sudo dnf copr enable jackgreiner/lug-helper`
* Install the LUG Helper with `sudo dnf install lug-helper`

## To Remove
* Remove the lug-helper package with `sudo dnf remove lug-helper`
* Remove the repository with `sudo dnf copr remove jackgreiner/lug-helper`
