from colors import *

def help(defaults):
    print() 
    print(f"{BG_PURPLE} Terminal Video Player{RESET}")
    print(bar)
    print(f"Author: {PURPLE}SkwalExe <Leopold Koprivnik>{RESET}")
    print(f"Github: {PURPLE}https://github.com/SkwalExe{RESET}")
    print(bar)
    print(f"A highly customizable terminal video player made in python.")
    print(bar)
    print(f"Options:")
    print(f"\t{PURPLE}--show-stdin : {YELLOW}If your cursor is not visible after playback, use this option to show it again")
    print(f"\t{PURPLE}-h, --help : {YELLOW}Show this help message and exit")
    print(f"\t{PURPLE}-v, --version : {YELLOW}Show the version number and exit")
    print(f"\t{PURPLE}-f, --filename [true/false]: {YELLOW}Specify the video file to play")
    print(bar)
    print(f"\t{PURPLE}-c, --colors [true/false]: {YELLOW}Show colors [Default: {defaults['use_colors']}]")
    print(f"\t{PURPLE}-b, --blocks [true/false]: {YELLOW}Use colored blocks/pixels instead of characters [Default: {defaults['use_colors']}]")
    print(f"\t{PURPLE}-l, --loop [true/false]: {YELLOW}Loop the video [Default: {defaults['loop']}]")
    print(f"\t{PURPLE}-s, --skip-frames [true/false]: {YELLOW}Skip frames if needed when render takes too long [Default: {defaults['use_blocks']}]")
    print(f"\t{PURPLE}-m, --fps-multiplier [float]: {YELLOW}Increase or decrease the playback speed [Default: {defaults['skip_frames']}]")
    print(f"\t{PURPLE}-hs, --hide-status [true/false]: {YELLOW}Hide the playback status at the bottom of the video [Default: {defaults['hide_status']}]")
    print(f"\t{PURPLE}-a, --ascii-chars [string]: {YELLOW}Use custom characters for 'text playback', from opaque to transparent [Default: {defaults['ascii_chars']}]")
    print(f"\t{PURPLE}-i, --inverse-grayscale [true/false]: {YELLOW}Inverse grayscale, opaque chars become transparent etc [Default: {defaults['inverse_grayscale']}]")
    print(f"\t{PURPLE}-ab, --ascii-background [black/white/none]: {YELLOW}Background color when rendering with ascii [Default: {defaults['ascii_background']}]")
    print(f"\t{PURPLE}-mo, --most-opaque [true/false]: {YELLOW}Use only the most opaque character when rendering with colored ascii [Default: {defaults['most_opaque']}]")
    print(f"\t{PURPLE}-fl, --fps-limit [integer]: {YELLOW}FPS limit to make the render more fluid in the terminal [Default: {defaults['fps_limit']}]")
    print(f"\t{PURPLE}-cb, --chars-in-blocks [true/false]: {YELLOW}Also put corresponding character inside of color blocks [Default: {defaults['chars_in_blocks']}]")
    print(f"\t{PURPLE}-bcc, --block-characters-color [white/black/terminal]: {YELLOW}The color of the chars when -cb is used [Default: {defaults['bcc']}]")
    print(bar)
    print(f"Controls:")
    print(f"\t{PURPLE}Space : {YELLOW}Pause the playback")
    print(f"\t{PURPLE}Esc : {YELLOW}Stop playback and exit")


    print()