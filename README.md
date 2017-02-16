# Mandelbrot

## The Magic Equation

Imagine a God-like entity creating the Universe just before the
Big Bang. The only way of controlling this creation is by imposing
a set of physical laws from which everything else will follow.
The world around us may be chaotic, but it has a remarkable underlying
consistency when one considers things like DNA, plants and creatures.

Now imagine an infinite 2D universe created from a much simpler
set of laws. The Mandelbrot Set (named after Benoit Mandelbrot)
defines one such universe using an beautifully simple equation:

    Z -> Z * Z + C
  
When this equation is used in a certain way, it creates a world
full of exotic shapes known as fractals. The similarities with
our own world are uncanny. Bugs, sea-horses and plants are only
the tip of the iceberg. If your computer was powerful enough,
you could zoom in forever and make facinating new discoveries.
All of this from an innocuous little equation!

Who said Math was boring?

Which brings me to the whole point of this exercise for aspiring
programmers.

## System Requirements

We tested this prgram on Windows 7, but there is no reason why it
shouldn't work reliably on other platforms. Before running the
program on Windows, you will need to install Python 3.2 (standard
32-bit version with IDLE) and then Pygame 1.9.2a0.wn32-py3.2.

Unfortunately Pygame is no longer actively maintained even though
it still works reliably on modern OSes. 

The program has two windows: the console and view window.
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
detail using a Maximum Iterations Count = 256

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
Using the Complex version also has the benefit of underlying
the algorithm's simplicity

## Coordinates

View coordinates in the Complex plane are floating-point
numbers. The Real part (X) increases towards the right and
the Imaginary part (Y) increases towards the top. The view
rectangle is specified by CENTER coordinates, width and
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
5. Add random/noise/unpredictability element to the core equation.
