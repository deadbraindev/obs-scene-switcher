# OBS Scene Switcher

## Description:
This is a simple Python script for OBS Studio that allows you to automatically switch between scenes at regular intervals. It randomly selects a scene from the available scenes, excluding the current one, and sets it as the active scene.

## How it works:
The script uses OBS Studio's scripting capabilities to access the list of scenes and set the active scene. It allows you to specify the cycle rate in minutes, controlling how often the scene switches occur. The cycle rate can be set between 1 minute and 1440 minutes (1 day).
> [!TIP]
>  It's recommended to add an automatic transition, for example, pre-prepared short video (e.g., with social media links), so that it triggers with each scene switch.

## Features:
- [x] Automatic scene switching at regular intervals.
- [x] Customizable cycle rate in minutes (1 to 1440 minutes).
- [ ] Ability for users to input scenes to be excluded via OBS frontend.
- [ ] Excludes specified scenes from the selection process.

## How to use:
1. Download the `obs-scene-switcher.py` script.
2. Place the script in the OBS Studio scripts folder.
3. In OBS Studio, go to `Tools` > `Scripts`.
4. Click the `+` button and add the `obs-scene-switcher.py` script.
5. Configure the cycle rate in the script properties.
6. Run the script and enjoy automatic scene switching!

> [!NOTE]
> Make sure to have multiple scenes set up in OBS Studio for effective use.

## License:
This script is released under the GNU General Public License v3.0. You can find the full license in the LICENSE file.

Feel free to contribute, report issues, or suggest improvements!

## Usage:
[lofi.today](https://lofi.today) - Vintage Beats & VHS Vibes • 24/7 Relaxation Radio
