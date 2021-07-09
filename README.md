# War-Simulation
This is going to be expanded to be a general war simulator. Check back for a longer description
This was built from a project I made for a coding class where you play as Bar Kochba and try to defeat the Romans. I've uploaded the source code for every version.

I've maintained a changelog along with tentative planned updates:

v 1.00
first bar kochba release and compilation (Basically identical to where I left off at end of the coding class)

v. 1.1
Adds Music "Bar Kochba was his name" (Hebrew)

v.1.2
Improve translation of Bar Kochba song - done
add pause at the end after winning or losing - done
add option to turn off music - done
fix bug where trying to stop music makes it start again - fixed by changing how music is played
go back to title screen upon finish - done
add start stuff into start function and game into game function (make more organized) - done
Fix bug where game crashes cause random_enemy variable refered to in a class outside the game function is local -done by making some variables global 
Add an icon and version info to exe - done
fix not playing on loop by default - fixed by changing music to pause and unpause
fix bug where after replay if press 3 exits game - What went wrong was that I had to restart the game function in the mixer I thought it was doing that and it wasn't
fix bug where pressing 2 at start screen crashes the app - fixed

v. 2.0
Remodel engine entirely to be generic and store campaigns in XML file - not fully generic yet still dependent on the xml file I made but some groundwork is laid
fix bug where xml file not being processed right by bs (beautiful soup) library - fixed
fix bug where imported xml strength causes error cause of types - fixed by making self.strength an int for calculation in enemy attack engine
fix bug where using xml health causes crash cause of comparison between string and int and float and int - fixed by converting everything to intergers
move music to music folder - done

v.2.1
add ability to use other xml files styled in the exact same way - done
fixed type errors by BeautifulSoup misreading xml files by importing everything (besides names) as an int - done
v. 2.2
allow user to chose another soundtrack add in modssound folder


Planned updates

V. 3.0
add all unofficial campaigns in mods folder
fix issue of user music having to be in root folder - done
Make Xml engine entirely generic

V. 4.0
Add defense to game engine (I meant to implement this never did
add yerushalmi and bavli on how Bar kochba died in sources
Make graphical
Allow users to add custom music

V.5.0 
add formal battles mechanism
