# Michi

A desktop virtual pet for wayland

- Does not require /dev/input permissions
- Made in rust
- egui
- sprite based, support for multiple sizes based for low and high res
- real time updates
- voice output
- Monitors usage and stats of the pc
  - Reacts to high cpu/ram/gpu
- Voice controled via whisper
- configuration ui
- ipc JSON-RPC via socket
- systemd native
- tiny brain with laya
- written by hand because I need to keep my brain active

## Questions and answers

- Why the brain in python?
  Support for certain models
- Why JSON-RPC?
  I want to be able to build an e-ink
- Why in rust?
  I liked rust before it was vibe-coders land and they are not going to take it from me
- Why the name Michi?
  I like cats
- Why the fuck so many linters rules and formatters?
  I have TDAH and some level of obsessive behaviour
- Why systemd?
  I happen to like systemd unlike most of my peers
