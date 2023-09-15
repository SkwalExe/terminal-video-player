<p align="center">
  <img src="assets/logo.png">
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/SkwalExe/terminal-video-player?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/SkwalExe/terminal-video-player?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/SkwalExe/terminal-video-player?color=blueviolet&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/SkwalExe/terminal-video-player?color=teal&style=for-the-badge">
  <img src="https://img.shields.io/github/issues-pr/SkwalExe/terminal-video-player?color=tomato&style=for-the-badge">

</p>

<p align="center">💠 🎥 Highly customizable terminal video player written in Python using OpenCV. 💠</p>





# Terminal Video Player



![banner](assets/banner.gif)

# How to use

First, clone the repository:

```bash
git clone https://github.com/SkwalExe/terminal-video-player
cd terminal-video-player
```

Then, install the dependencies:

```bash
pip3 install -r requirements.txt
```

Now, you can try the program with the example video provided with the repository:

```bash
python3 src/main.py -f bad-apple-colored.mp4
```

# Options

![help](assets/help.png)

The option list below is not exhaustive. For a complete list of options, see the image above, or run `python3 main.py --help`.

### The -c/--colors option

If true, the video will be played in color, else it will be played in grayscale.

![colors](assets/colors.gif)

### The -i/--inverse-grayscale option

Inverse the opacity of the characters.

![inverse](assets/inverse.gif)

### The -mo/--most-opaque option

If true, use the most opaque character when rendering with colored ascii.

![most-opaque](assets/most-opaque.gif)

### The -cb/--chars-in-blocks option

Also put corresponding characters in colored blocks when the --blocks option is true.

![chars-in-blocks](assets/cb.gif)