# Mandelbrot

## The Magic Equation

Imagine a God-like entity creating the Universe just before the
Big Bang. His only way of controlling his creation is by imposing
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
rectangle width and height of ONE (zero widths and heights
are not possible in this instance).
