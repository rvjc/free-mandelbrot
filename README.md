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


    
