# cursepacker

Downloads a cursepack from a pack URL...

## Use

```
python3 cursepacker.py <pack download url>
```

This will extract the pack to the `<nameofpack>/minecraft` directory and download all the mod files required for the pack.

Simply install forge (in general) and point the vanilla launcher "game directory" at the `<nameofpack>/minecraft` directory.

## Example

SkyFactory 4: Visit the page here: https://www.curseforge.com/minecraft/modpacks/skyfactory-4/files/2767759 (this is the 4.1.0 version latest available, but use the URL for your pack) and right click and "Copy Link Location" on the big "Download" button.

got to your console and run the command 
```
python3 cursepacker.py https://www.curseforge.com/minecraft/modpacks/skyfactory-4/download/2767759
```
in a parent directory of where you want the resulting download to live (this command is the URL associated with the file location above)

It will download all the mods and files.

Finally, go to the vanilla launcher, and with an appropriate forge version installed, create a new "Installations":
  1. Name it
  2. Select the right forge version from the "Version" list
  3. Point "Game Directory" at the path you downloaded the pack to above
  4. Click create
  5. Click the play button alongside your new instance
  



