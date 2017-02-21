# Mandelbrot

## The Magic Equation

Imagine a God-like entity creating the Universe just before the
Big Bang. The only way of controlling this creation is by imposing
a set of physical laws from which everything else will follow.
The world around us may be chaotic, but it has remarkable underlying
consistencies when one considers things like DNA, plants and creatures.

Now imagine an infinite 2D universe created from a much simpler
set of laws. The Mandelbrot Set (named after Benoit Mandelbrot)
defines one such universe using a beautifully simple equation:

    Z -> Z * Z + C
  
When this equation is interpreted in a certain way, it creates a
world full of exotic shapes known as fractals. The similarities
with our own world are uncanny. Bugs, sea-horses and plants are
only the tip of the iceberg. If your computer was powerful enough,
you could uncover enough detail to make facinating new discoveries.
All of this from an innocuous little equation!

So who said math was boring? Which brings me to the whole point
of this exercise.

Three of my sons were developing an interest in programming a
few years back and I thought the time was ripe for them to start
getting serious about math. Finding a consuming passion at a
young age is a wonderful thing but it is often at the expense of
other activities which, when left unattended, can limit your
options down the road.

As the entry requirements for Computer Science courses plummet,
aspiring programmers tend to neglect the deeper mathematical
aspects which are invariably bound up with "boring" school work.
Many programmers live to regret this later when the "math ceiling"
is even harder to penetrate and limits their ability to truly
excel at their art. Even a cursory perusal of Programming Q&A web
sites like StackOverflow will bear this out. Of course, the real
fun is always to be found in burrowing down beyond the superfical.
And this is as true of activities like music, car-tinkering and
sports as it is for software development.

One of the downsides of school-work in general, and math in
particular, is that we often have to learn stuff whose benefits
are not immediately apparent. This really sucks for modern
teenagers whose precociousness and impatience surprise even
those of us who were once precocious and impatient teenagers
ourselves ;-) Complex numbers are a classic case in point and are
often presented in a way that terrorises an already angst-ridden
age-group. Complex? Not really (if you delve a little deeper)!
Imaginary numbers? WTF? Square root of minus one? Iota is all
Greek to me!

Well, for this particular field, there is no better way of
winning over young hearts and minds than with Benoit
Mandelbrot's accidental discovery. As the story goes, he
thought his printer was smudging ink (see the World View
screenshot below). But he took it upon himself to investigate
further. And, in doing so, he made what Arthur C. Clarke
described as "one of the most astonishing discoveries in the
entire history of mathematics".

As my youngest son put it: "Maybe the universe is NOT expanding,
but we are getting smaller". Well, this Mandelbotesque thought
experiment by a twelve-year old is not as crazy at it seems!
It is actualy a very intuitive way of visualising our so-called
"expanding" universe where all galaxies appear to be moving away
from each other other at the same rate regardless of our point
of reference.

You too can burrow down and let your imagination run riot.
And if you can master something as simple as a complex number
then the sky — nay, the universe — is the limit :-)

## Screenshots

### World View

![](/WorldView.jpg)

### Exotic Island

![](/ExoticIsland.jpg)

### Claw Spiral

![](/ClawSpiral.jpg)

### Sea Horses

![](/SeaHorses.jpg)

### Spiky Tail

![](/SpikyTail.jpg)

### Fan of Elephants

![](/FanOfElephants.jpg)

### Thorny Branches

![](/ThornyBranches.jpg)

### Jelly Fish

![](/JellyFish.jpg)

### Potted Plants

![](/PottedPlants.jpg)

### Brocolli Junction

![](/BrocolliJunction.jpg)

## System Requirements

At the time of writing (2012), we tested this program on Windows 7,
but there is no reason why it shouldn't work reliably on other
platforms. Before running the program on Windows, you will need to
install Python 3.2 (standard 32-bit version with IDLE) and then
Pygame 1.9.2a0.wn32-py3.2.

Unfortunately Pygame is no longer actively maintained but still
works reliably on modern OSes. 

The program has two windows: the console and view windows.
A simple help system is provided which is self-explanatory.

## How to Zoom

Mark the zoom area by holding down the left button of the mouse,
dragging and releasing. Then click within the zoom area to zoom
to a new view. Please be patient and observe progress at the top
of the view window. You can close this window at any time during
calculation.
 
To clear the zoom area, simply click outside it. It will also be
cleared if you attempt to zoom beyond the zoom limit

## Performance and Detail
   
This program tries to find a good compromise between performance
and detail for normal PC users. When you see wonderful Mandelbrot
plots on the web, remember that many of them have been generated
by high-performance computers often working for days at a time
with incredibly high iteration counts.

The Maximum Iterations parameter describes the depth to which the
Mandelbrot algorithm will descend to search for detail at each
pixel. This parameter is greater than one million for some of the
most impressive images. It is also restricted by the computer and
program's ability to process very high-precision floating-point
numbers at speed. By keeping the display window small and using
colors efficiently, this program is able to generate reasonable
detail within a reasonable amount of time using a Maximum
Iterations Count of 256.

A new view is typically rendered in less than a minute although
this time will increase in darker regions.

## Why Greyscale?
   
The color representation of the values produced by the Mandelbrot
algorithm is the most subjective aspect. Using the full color
spectrum with sophisticated post-processing can yield impressive
results but it takes from the one-dimensional purity, especially
at low Maximum Iteration counts.
 
Dynamic greyscale color balancing is also employed to show the
maximum detail for any given view. The overall result is a good
compromise between speed and detail

## Complex or Real Calculations?

Python's ability to process Complex Numbers is so fast that
there is little benefit to using the Mandelbrot algorithm for
the Real Plane (see Wikipedia article on the Mandelbrot Set).
Using the Complex version also has the benefit of underlining
the algorithm's simplicity

## A Note on Coordinates

View coordinates in the Complex plane are floating-point
numbers. The Real part (X) increases towards the right and
the Imaginary part (Y) increases towards the top. The view
rectangle is specified by its CENTER coordinates, width and
height (X,Y,W,H).

Screen coordinates are in integer pixels relative to (0,0)
at the top left of the window. The X value increases towards
the right of the screen BUT the Y value increases towards
the bottom. The zoom rectangle consists of the screen
coordinates of the starting and end points of the zoom drag.
When both coordinates are identical, this implies a zoom
rectangle width and height of ONE (therefore zero zoom
widths and heights are not possible).

## Challenge

In the best spirit of educational programming, here are a
few challenges for aspiring programmers wanting to move up
the learning curve rapidly:

1. Refactor this code to use a modern graphics framework.
2. Rewrite in C/C++ to enhance speed.
3. Use full colour instead of greyscale.
4. Allow for different color models/interpretations.
5. Add random/noise/unpredictability to the core equation (free will?).
6. Add a save image feature (with coodinates).
7. Add a long-running batch feature to automate zoom and save video.
8. Reflect on the fact that the Creationism is bloody hard work ;-)
