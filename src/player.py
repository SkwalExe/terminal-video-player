from colors import *
import cv2 as cv
from utils import *
from time import sleep, time
import pynput

class Player():
    def __init__(self, options):
        self.options = options
        self.last_color = None
        self.last_bg_color = None

        self.width = width

        # If the status is shown, the video height is reduced by 3 to make space for the status
        self.height = height if self.options['hide_status'] else height - 3

        hide_stdin()

    # Return the ainsi escape sequence to set the background color to the pixel's color
    def ainsi_bg_color(self, pixel):
        bg_color = f"\x1b[48;2;{pixel[2]};{pixel[1]};{pixel[0]}m"

        # dont return the sequence if the same background color is already being used
        return "" if bg_color == self.last_bg_color else bg_color

    # Return the ainsi escape sequence to set the text color to the pixel's color
    def ainsi_color(self, pixel):
        color = f"\x1b[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m"

        # dont return the sequence if the same color is already being used
        return "" if color == self.last_color else color

    # Finds a character that coreesponds to the pixel's grayscale
    def get_corresponding_char(self, pixel):
        grayscale = sum(pixel) / 3
        corresponding_char_index = int(grayscale/255*(len(self.options["ascii_chars"]) - 1))
        corresponding_char = self.options["ascii_chars"][corresponding_char_index if self.options['inverse_grayscale'] else -1 - corresponding_char_index]
        return corresponding_char

    def render_frame_ascii(self, frame):
        # The terminal sould be cleared when the frame is displayed
        frame_result = CLEAR_SEQUENCE

        if self.options['ascii_background'] == "white":
            frame_result += f"\x1b[48;2;255;255;255m"
        elif self.options['ascii_background'] == "black":
            frame_result += f"\x1b[48;2;0;0;0m"

        # Set text color to white if colors are not used and black background 
        # to prevent black text over black background
        if not self.options['use_colors']:
            if self.options['ascii_background'] == "black":
                frame_result += f"\x1b[38;2;255;255;255m"
            elif self.options['ascii_background'] == "white":
                frame_result += f"\x1b[38;2;0;0;0m"

        
        for index, row in enumerate(frame):
            for pixel in row:

                if self.options["use_colors"]:
                    frame_result += self.ainsi_color(pixel) + (self.options['ascii_chars'][0] if self.options["most_opaque"] else self.get_corresponding_char(pixel)) * 2
                else:
                    frame_result += self.get_corresponding_char(pixel) * 2

            # Break line only if there are still rows to render
            if index != len(frame) - 1:
                frame_result += "\n"

        return frame_result

    def render_frame_blocks(self, frame):
        # The terminal sould be cleared when the frame is displayed
        frame_result = CLEAR_SEQUENCE


        if self.options['chars_in_blocks']:
            if self.options['bcc'] == "black":
                frame_result += f"\x1b[38;2;0;0;0m"
            elif self.options['bcc'] == "white":
                frame_result += f"\x1b[38;2;255;255;255m"


        for index, row in enumerate(frame):
            for pixel in row:
                frame_result += self.ainsi_bg_color(pixel) + (" " if not self.options["chars_in_blocks"] else self.get_corresponding_char(pixel)) * 2
            # Break line only if there are still rows to render
            if index != len(frame) - 1:
                frame_result += "\n"
    
        return frame_result

    def play(self):
        video = cv.VideoCapture(self.options['filename'])

        if not video.isOpened():
            print(f"{RED}Error: {YELLOW}Unable to open video : {self.options['filename']}{RESET}")
            quit(0)
        
        FPS = video.get(cv.CAP_PROP_FPS) * self.options['fps_multiplier']
        video_width = video.get(cv.CAP_PROP_FRAME_WIDTH)
        video_height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
        frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
        duration = frame_count / FPS


        resize_factor = min(self.width / video_width, self.height / video_height)


        # The delay wanter between two frames to keep the video FPS
        FRAME_WAIT = 1/FPS


        lost = 0
        # If the skipped_frames counter is needed, uncomment this
        # skipped_frames = 0
        current_frame_index = 0
        rendered_frames = 0
        start = time()
        playing = True
        frame = None
        stop = False

        def on_press(key):
            nonlocal playing
            nonlocal stop

            if key == pynput.keyboard.Key.space:
                playing = not playing

            if key == pynput.keyboard.Key.esc:
                stop = True


        with pynput.keyboard.Listener(on_press=on_press) as listener:

            while not stop:
                if not playing:
                    sleep(0.05)
                    continue

                current_frame_index += 1

                # If it is the end of the playback and the loop option is enabled, reset the video
                if current_frame_index >= frame_count and self.options['loop']:
                    current_frame_index = 0
                    video.set(cv.CAP_PROP_POS_FRAMES, 0)


                # If the skip_frames option is enabled, 
                # skip frames if the previous frame took too long to render
                # to keep the playback smooth
                if self.options["skip_frames"] and lost > FRAME_WAIT:
                    lost -= FRAME_WAIT
                    # If the skipped_frames counter is needed, uncomment this
                    # skipped_frames+=1
                    video.read()
                    continue
                
                rendered_fps = rendered_frames / (time() - start)

                # Limit the FPS according to the fps_limit option
                if rendered_fps > self.options["fps_limit"]:
                    video.read()
                    sleep(FRAME_WAIT)
                    continue

                rendered_frames += 1

                start_ts = time()

                success, frame = video.read()


                # If we cannot read the next frame, most likely the video has ended
                if not success:
                    break

                # Resize frame to terminal size
                frame = cv.resize(frame, (int(video_width * resize_factor),
                                int(video_height * resize_factor)))


                frame_result = self.render_frame_blocks(frame) if self.options["use_blocks"] else self.render_frame_ascii(frame)

                if not self.options['hide_status']:
                    frame_result += f"\x1b[0m\nVideo FPS : {FPS} - Rendered FPS : {rendered_fps:.0f}\nPlayer position (in seconds) : {current_frame_index / FPS:.2f}s / {duration:.2f}s"

                print(frame_result, flush=False, end="")

                self.last_color = None

                # The time it took to convert the frame into the text result
                render_time = (time() - start_ts) / 1

                # The delay between two frames, taking into account the time it takes to render the frame
                delay = FRAME_WAIT - render_time

                # If the render took too long to keep up with the FPS,
                # add the delay to the lost time
                if delay < 0:
                    lost += render_time - FRAME_WAIT

                if delay > 0:
                    sleep(delay)
            
        show_stdin()