from colors import *
from sys import argv
from utils import *
from player import *
from help import help

DEFAULT_ASCII_CHARS = "@%?+;. "
VERSION = "0.1.0"


def version():
    print(f"{BG_PURPLE} Terminal Video Player Python {RESET}")
    print(f"Version: {PURPLE}{VERSION}{RESET}")

def main():
    options = {
        "use_colors": True,
        "use_blocks": False,
        "fps_multiplier": 1,
        "skip_frames": True,
        "ascii_chars": DEFAULT_ASCII_CHARS,
        "filename": None,
        "inverse_grayscale": False,
        "ascii_background": "black",
        "most_opaque": True,
        "fps_limit": 24,
        "chars_in_blocks": False,
        "bcc": "black",
        "loop": False,
        "hide_status": False,
    }

    # ----- Start parsing args -----
    # Remove program name from arguments
    argv.pop(0)

    # And parse each argument
    while len(argv) > 0:
        arg = argv.pop(0)
        match arg:
            case '--help' | '-h':
                help(options)
                quit(0)

            case '--show-stdin':
                show_stdin()
                quit(0)

            case '--version' | '-v':
                version()
                quit()

            case '--colors' | '-c':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _use_colors = argv.pop(0).lower()

                if not _use_colors in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["use_colors"] = _use_colors == "true"

            case '--loop' | '-l': 
                if len(argv) == 0:  
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _loop = argv.pop(0).lower()

                if not _loop in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["loop"] = _loop == "true"

            case '--hide-status' | '-hs': 
                if len(argv) == 0:  
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _hide_status = argv.pop(0).lower()

                if not _hide_status in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["hide_status"] = _hide_status == "true"


            case '--blocks' | '-b':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _use_blocks = argv.pop(0).lower()

                if not _use_blocks in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["use_blocks"] = _use_blocks == "true"
                options["use_colors"] = True

            case '--most-opaque' | '-mo':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _most_opaque = argv.pop(0).lower()

                if not _most_opaque in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["most_opaque"] = _most_opaque == "true"

            case '--inverse-grayscale' | '-i':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _inverse_grayscale = argv.pop(0).lower()

                if not _inverse_grayscale in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["inverse_grayscale"] = _inverse_grayscale == "true"


            case '--skip-frames' | '-s':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _skip_frames = argv.pop(0).lower()

                if not _skip_frames in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["skip_frames"] = _skip_frames == "true"

            case '--ascii-background' | '-ab':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing value after {arg}, expected 'white', 'black', or 'none'{RESET}")
                    quit(1)
                
                _ascii_background = argv.pop(0).lower()

                if not _ascii_background in ["black", "white", "none"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'white', 'black', or 'none'{RESET}")
                    quit(0)
                options["ascii_background"] = _ascii_background

            case '--chars-in-blocks' | '-cb':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing true or false after {arg}{RESET}")
                    quit(1)
                
                _chars_in_blocks = argv.pop(0).lower()

                if not _chars_in_blocks in ["true", "false"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'true' of 'false'{RESET}")
                    quit(0)
                options["chars_in_blocks"] = _chars_in_blocks == "true"


            case '--block-characters-color' | '-bcc':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing value after {arg}, expected 'white', 'black', or 'terminal'{RESET}")
                    quit(1)
                
                _bcc = argv.pop(0).lower()

                if not _bcc in ["black", "white", "terminal"]:
                    print(f"{RED}Error: {YELLOW}Argument after {arg}, expected 'white', 'black', or 'terminals'{RESET}")
                    quit(0)
                options["bcc"] = _bcc

            case '--fps-multiplier' | '-m':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing value after {arg}{RESET}")
                    quit(1)
                
                try:
                    _fps_multiplier = float(argv.pop(0))
                except:
                    print(f"{RED}Error: {YELLOW}Invalid argument after {arg}, expected float (ex: 1.5){RESET}")
                    quit(0)
                if not _fps_multiplier > 0:
                    print(f"{RED}Error: {YELLOW}Invalid argument after {arg}, value must be superior to 0{RESET}")
                    quit(0)

                options["fps_multiplier"] = _fps_multiplier

            case '--fps-limit' | '-fl':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing value after {arg}{RESET}")
                    quit(1)
                
                try:
                    _fps_limit = int(argv.pop(0))
                except:
                    print(f"{RED}Error: {YELLOW}Invalid argument after {arg}, expected integer (ex: 51){RESET}")
                    quit(0)
                if not _fps_limit > 0:
                    print(f"{RED}Error: {YELLOW}Invalid argument after {arg}, value must be superior to 0{RESET}")
                    quit(0)

                options["fps_limit"] = _fps_limit


            case '--ascii-chars' | '-a':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing value after {arg}{RESET}")
                    quit(1)
                
                _ascii_chars = argv.pop(0)

                if not len(_ascii_chars) > 1:
                    print(f"{RED}Error: {YELLOW}At least two characters expected after {arg}{RESET}")
                    quit(0)

                options["ascii_chars"] = _ascii_chars
            

            case '--filename' | '-f':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing value after {arg}{RESET}")
                    quit(1)
                
                options["filename"] = argv.pop(0)

            case _:
                print(f"{RED}Error: {YELLOW}Unknown argument : {PURPLE}{arg}{RESET}")
                quit(1)

    if options["filename"] is None:
        print(f"{RED}Error: {YELLOW}Please specify a video file to play with the -f or --filename option.{PURPLE}{RESET}")
        quit(1)
    

    if not options["use_colors"] and options["use_blocks"]:
        print(f"{RED}Error: {YELLOW}You cannot use blocks without colors.{PURPLE}{RESET}")
        quit(1)


    player = Player(options)


    player.play()


if __name__ == '__main__':
    main()
