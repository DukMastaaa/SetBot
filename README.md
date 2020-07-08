# SetBot
A program which plays the card game Set on the website https://setwithfriends.com.

The program watches your screen, determines which tiles in the game make a set, and 
enters in the associated sequence of characters into your keyboard.

Please note that the program reads precise pixel locations on your screen to determine properties 
of the tiles in the game. I have not built this bot with immediate compatibility across multiple 
devices. Instructions to get the bot working for you are listed below.

Big thanks to cortex#9689 for helping with tile recognition.

SetBot in action: https://youtu.be/rNeaEW2lWs8

## How to use it
Once everything's been set up properly, start a new game in Set with Friends and set the display to dark mode. 
Then, run `capture.py` and switch to the browser window. The bot will work its magic from then on. You will need 
to restart the bot (by running `capture.py` again) after the end of every game.

An error message such as `min() arg is an empty sequence` indicates that there's most likely something 
wrong with the pixel positions SetBot has for your specific screen. Try the setup process again.

## How to set it up
Here's a setup guide to get SetBut up and running on your computer.

1. Install the `cv2`, `mss`, `numpy` and `keyboard` libraries to your computer. This can be done using `pip`.
2. Open https://setwithfriends.com, create a new game and start it.
3. Screenshot your whole monitor screen.
4. Open `constants.py`.
5. Use a suitable image editing program to find the coordinates of the top-left pixel of the top-left tile.
Change `UL_CORNER_X` and `UL_CORNER_Y` in `constants.py` to these coordinates.
6. Measure the distance (in pixels) of the bounding boxes of each tile (this includes the space between each 
rounded rectangle). Change `TILE_WIDTH` and `TILE_HEIGHT` in `constants.py` to your measurements.
7. Create a folder named "tiles" in the *same directory* as the other files.
8. Hopefully you're fast at playing Set, because this is going to take a while. I recommend getting a friend 
to help. You'll need to start a new game (in dark mode) and run `image_saver.py` around every 4 turns.
After each time you run the file, add some random letter to the start of the file path `tiles/{i}{j}.png` 
so `image_saver` doesn't overwrite the images you've already got.<br>
This grabs every tile on the screen, processes the image to be greyscale and saves it to the `tiles` folder.
9. Now, remove all duplicate images from the `tiles` folder (i.e. remove images which show the same tile 
as another in the folder).
10. In `constants.py`, take a look at the constants with values from 4-12. Manually rename each of the 
(hopefully unique) images in `tiles`, identifying each one of them by a series of three integers 
from `constants.py`. This should be in the format `<shape>_<shading>_<number>`. See the `tiles` folder 
I've provided for examples.
11. All set up! 

### Disclaimer
Please use this program at your own discretion. Don't cheat with others. I'm not responsible if you choose to do that.
