from platformdirs import PlatformDirs

dirs = PlatformDirs(appname="michi", appauthor="cesasol", version="0.0.0")


# For sprites
dirs.user_data_dir

# For config (selected sprite)
dirs.user_config_dir

# For state (position, current monitor...)
dirs.user_state_dir

# ipc socket
dirs.user_runtime_dir

