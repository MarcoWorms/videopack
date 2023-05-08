# VideoPack CLI

A command-line interface (CLI) tool to unpack and pack videos into frames and audio using Python and MoviePy.

Unpack video into frames:

```bash
$ videopack unpack input.mp4
```

Repack frames into video:

```bash
$ videopack pack ./frames --fps 60
```

## Installation

1. Download or clone this repository:

   ```
   git clone https://github.com/MarcoWorms/videopack.git
   ```

   Alternatively, download the repository as a ZIP file and extract it.

2. Navigate to the `videopack-cli` directory:

   ```
   cd videopack
   ```

3. Install the package using pip:

   ```
   pip install --user .
   ```

   This will make the `videopack` command available in your terminal.

## Usage
### Unpack a video

To unpack a video into frames and audio, run:

```
videopack unpack input.mp4
```

By default, the frames will be saved in a folder named `frames`, and the audio will be saved as `audio.mp3`. You can specify custom output paths with the `--output` and `--audio_output` options:

```
videopack unpack input.mp4 --output ./frames_renamed --audio_output custom_audio.mp3
```

### Pack frames and audio into a video

To pack a folder of frames and an audio file into a video, run:

```
videopack pack ./new_frames --fps 60
```

By default, the input audio file is `audio.mp3`. You can specify a custom input audio path with the `--audio_input` option:

```
videopack pack ./new_frames --fps 60 --audio_input custom_audio.mp3
```

By default, the output video will be saved as `output.mp4`. You can specify a custom output path with the `--output` option:

```
videopack pack ./new_frames --fps 60 --output output_renamed.mp4
```

For more information and options, run:

```
videopack --help
```

## Dependencies

- [MoviePy](https://github.com/Zulko/moviepy)

## License

[![](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
