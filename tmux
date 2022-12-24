Command list tmux:

Create pane:

CTRL + b and press %
CTRL + b and press "


Create window:

CTRL + b and press C
 Switch window:
  CTRL + b and press 0/1/2/3...
 Rename window:
  CTRL + b and press ,

Sessions:

  View sessions:
    tmux ls
  Select a session:
    tmux attach -t [session_number_name]
  Rename session:
    tmux rename-session -t [session_number_name] [new_session_name]
  Start new session:
    tmux new -s [session_name]
  Kill session:
    tmux kill-session -t [session_number_name]
