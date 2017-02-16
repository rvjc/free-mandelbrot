############################################################
#
# Mandelbrot 1.0 Copyright (C) RVJ Callanan 2012
#
# This is FREE software, licensed under the GNU GPLv3
# See: <http://www.gnu.org/licenses/>.
#
############################################################

#
# COMPLEX OR REAL CALCULATIONS?
#
# Python's ability to process Complex Numbers is so fast that
# there is little benefit to using the Mandelbrot algorithm for
# the Real Plane (see Wikipedia article on the Mandelbrot Set).
# Using the Complex version also has the benefit of underlying
# the algorithm's simplicity
#
# NOTE ABOUT COORDINATES
#
# View coordinates in the Complex plane are floating-point
# numbers. The Real part (X) increases towards the right and
# the Imaginary part (Y) increases towards the top. The view
# rectangle is specified by CENTER coordinates, width and
# height (X,Y,W,H).
#
# Screen coordinates are in integer pixels relative to (0,0)
# at the top left of the window. The X value increases towards
# the right of the screen BUT the Y value increases towards
# the bottom. The zoom rectangle consists of the screen
# coordinates of the starting and end points of the zoom drag.
# When both coordinates are identical, this implies a zoom
# rectangle width and height of ONE (zero widths and heights
# are not possible in this instance).

############################################################
# IMPORTS
############################################################

import pygame; from pygame.locals import *
import sys, os
from math import *
from colorsys import *

############################################################
# CONSTANTS
############################################################

MAX_DEPTH   = 256           # Max Mandelbrot iterations
SW          = 600           # Screen Width
SH          = 400           # Screen Height
AR          = SW/SH         # Aspect Ratio

PRECISION   = 0.01          # Compaction precision (1%)
MAX_DP       = 16           # Max decimal places used

REF_X       = -0.75         # Start X coordinate
REF_Y       = 0.0           # Start Y coordinate
MIN_WIDTH   = 1E-15         # Minimum view width
MAX_WIDTH   = 4.5           # Maximum view width
MIN_HEIGHT  = MIN_WIDTH/AR  # Minimum view height
MAX_HEIGHT  = MAX_WIDTH/AR  # Maximum view height

MIN_X = REF_X - MAX_WIDTH/2
MAX_X = REF_X + MAX_WIDTH/2
MIN_Y = REF_Y - MAX_HEIGHT/2
MAX_Y = REF_Y + MAX_HEIGHT/2

ALL_EVENTS = [ QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION ]

WORLDVIEW = [REF_X, REF_Y, MAX_WIDTH, MAX_HEIGHT]

VIEW0 = [-0.090,          0.964,          0.165,          0.110       ]
VIEW1 = [-1.25079,        0.02242,        0.00065,        0.00043     ]
VIEW2 = [-0.7698,         0.1095,         0.0042,         0.0028 ]
VIEW3 = [-0.74627,        0.12041,        0.00039,        0.00026     ]
VIEW4 = [0.3231,          -0.0354,        0.0092,         0.0061      ]
VIEW5 = [-1.94081,        0.00088,        0.00082,        0.00055     ]
VIEW6 = [-0.5261,         0.5067,         0.0216,         0.0144      ]
VIEW7 = [0.35496,         0.34629,        0.00028,        0.00019     ]
VIEW8 = [-1.7491005,      0.0003483,      0.0000255,      0.0000170   ]
VIEW9 = [-1.785693031,    0.000000869,    0.000000315,    0.000000210 ]

DESC0   = "Thorny Branches"
DESC1   = "Exotic Island"
DESC2   = "Jelly Fish"
DESC3   = "Sea Horses"
DESC4   = "Fan of Elephants"
DESC5   = "Spindly Bug"
DESC6   = "Potted Plants"
DESC7   = "Claw Spiral"
DESC8   = "Spiky Tail"
DESC9   = "Brocolli Junction"
        
############################################################
# Global Variables
############################################################

ViewRect    = None      # Current view of the Mandelbrot Set 
ZoomRect    = None      # Current zoom drag rectangle
Dragging    = False     # Zoom drag in progress
Closing     = False     # Closing view screen
Quitting    = False     # Quitting program itself

Palette     = None      # Color palette
Map         = None      # Two dimensional screen map

Surface     = None      # Display surface
Image       = None      # Currently displayed image

############################################################
# FUNCTIONS
############################################################

def InitMenu():

    # Determines initial view and other options. Returns a
    # valid ViewRect to indicate to MainLoop() to open new
    # view window. If ViewRect is not set when menu returns,
    # this is a signal to MainLoop() to loop around to menu
    # again. Sets Quitting to True to indicate to MainLoop
    # that user has opted to quit.
    
    global ViewRect, Quitting

    ViewRect = None

    print("-----------------------------------------------------------------")
    print("MAIN MENU")
    print("-----------------------------------------------------------------")
    print("Q: Quit")
    print("H: Help")
    print("C: Custom Coordinates")
    print("W: World View (default)")
    print()
    print("Points of Interest")
    print("------------------")
    print("0: " + DESC0)
    print("1: " + DESC1)
    print("2: " + DESC2)
    print("3: " + DESC3)
    print("4: " + DESC4)
    print("5: " + DESC5)
    print("6: " + DESC6)
    print("7: " + DESC7)
    print("8: " + DESC8)
    print("9: " + DESC9)
    print("-----------------------------------------------------------------")
    
    a = input("Enter Option: ")
    print()

    if a.lower() == "q":
        Quitting = True
        
    elif a.lower() == "h":
        HelpMenu()
        
    elif a.lower() == "c":
        ViewRect = GetCoordinates()

    elif a == '0':
        ViewRect = VIEW0
        
    elif a == '1':
        ViewRect = VIEW1
        
    elif a == '2':
        ViewRect = VIEW2
        
    elif a == '3':
        ViewRect = VIEW3
        
    elif a == '4':
        ViewRect = VIEW4
        
    elif a == '5':
        ViewRect = VIEW5
        
    elif a == '6':
        ViewRect = VIEW6
        
    elif a == '7':
        ViewRect = VIEW7
        
    elif a == '8':
        ViewRect = VIEW8
        
    elif a == '9':
        ViewRect = VIEW9
        
    else:
        ViewRect = WORLDVIEW

############################################################

def HelpMenu():

    while True:
        print("-----------------------------------------------------------------")
        print("HELP MENU")
        print("-----------------------------------------------------------------")
        print("1: The Magic Equation")
        print("2: How to Zoom")
        print("3: Performance and Detail")
        print("4: Why Greyscale?")
        print()
        print("X: Exit Help (default)")
        print("-----------------------------------------------------------------")        
        a = input("Enter Option: ")
        print()

        if a == "1":
            Help1()
        elif a == "2":
            Help2()
        elif a == "3":
            Help3()
        elif a == "4":
            Help4()
        else:
            break

############################################################

def Help1():

    print("-----------------------------------------------------------------")
    print("The Magic Equation")
    print("-----------------------------------------------------------------")
    print("Imagine a God creating the Universe just before the Big Bang. His")
    print("only way of controlling his creation was by imposing a set of")
    print("physical laws from which everything else would follow. Our world")
    print("may be chaotic, but it has a remarkable underlying consistency")
    print("when one considers things like DNA, plants and creatures.")
    print()
    print("Now imagine an infinite 2D universe created from a much simpler")
    print("set of laws. The Mandelbrot Set (named after Benoit Mandelbrot)")
    print("defines one such universe using an exceedingly simple equation:")
    print()
    print("               Z -> Z * Z + C")
    print()
    print("When this equation is used in a certain way, it creates a world")
    print("full of exotic shapes known as fractals. The similarities with")
    print("our own world are uncanny. Bugs and sea-horses are only the tip")
    print("of the iceberg. If your computer was powerful enough, you could")
    print("zoom in forever and make facinating new discoveries. All of this")
    print("from an innocuous little equation! Who said Math was boring?")
    print("-----------------------------------------------------------------")
    input("Press ENTER to continue")
    print()

############################################################

def Help2():

    print("-----------------------------------------------------------------")
    print("How to Zoom")
    print("-----------------------------------------------------------------")
    print("Mark the zoom area by holding down the left button of the mouse,")
    print("dragging and releasing. Then click within the zoom area to zoom")
    print("to a new view. Please be patient and observe progress at the top")
    print("of the view window. You can close this window at any time during")
    print("calculation.")
    print()
    print("To clear the zoom area, simply click outside it. It will also be")
    print("cleared if you attempt to zoom beyond the zoom limit.")
    print("-----------------------------------------------------------------")
    input("Press ENTER to continue")
    print()

############################################################

def Help3():

    print("-----------------------------------------------------------------")
    print("Performance and Detail")
    print("-----------------------------------------------------------------")
    print("This program tries to find a good compromise between performance")
    print("and detail for normal PC users. When you see wonderful Mandelbrot")
    print("plots on the web, remember that many of them have been generated")
    print("by high-performance computers often working for days at a time")
    print("with incredibly high iteration counts.")
    print()
    print("The Maximum Iterations parameter describes the depth to which the")
    print("Mandelbrot algorithm will descend to search for detail at each")
    print("pixel. This parameter is greater than one million for some of the")
    print("most impressive images. It is also restricted by the computer and")
    print("program's ability to process very high-precision floating-point")
    print("numbers at speed. By keeping the display window small and using")
    print("colors efficiently, this program is able to generate reasonable")
    print("detail using a Maximum Iterations Count = " + str(MAX_DEPTH) + ".")
    print()
    print("A new view is typically rendered in less than a minute although")
    print("this will increase in darker regions.")
    print("-----------------------------------------------------------------")
    input("Press ENTER to continue")
    print()

############################################################

def Help4():

    print("-----------------------------------------------------------------")
    print("Why Greyscale?")
    print("-----------------------------------------------------------------")
    print("The color representation of the values produced by the Mandelbrot")
    print("algorithm is the most subjective aspect. Using the full color")
    print("spectrum with sophisticated post-processing can yield impressive")
    print("results but it takes from the one-dimensional purity, especially")
    print("at low Maximum Iteration counts.")
    print()
    print("Dynamic greyscale color balancing is also employed to show the")
    print("maximum detail for any given view. The overall result is a good")
    print("compromise between speed and detail")
    print("-----------------------------------------------------------------")
    input("Press ENTER to continue")
    print()
              
############################################################

def GetCoordinates():

    print("-----------------------------------------------------------------")
    print("Custom Coordinates")
    print("-----------------------------------------------------------------")
    print("Values are adjusted to practical precisions!")
    print()
        
    x = GetNum("Center X  ", MIN_X, MAX_X)
    y = GetNum("Center Y  ", MIN_Y, MAX_Y)
    w = GetNum("View Width", MIN_WIDTH, MAX_WIDTH)

    print()

    # Generate height automatically
        
    h,dp = Compact(w/AR)
        
    return x,y,w,h

############################################################

def GetNum(desc, min_val, max_val):

    min_val, min_dp = Compact(min_val)
    max_val, max_dp = Compact(max_val)
    
    fmt_min = FmtDp(min_val,min_dp)
    fmt_max = FmtDp(max_val,max_dp)

    while True:

        try:
            
            v = float(input(desc + ": "))
            
            if v < min_val:
                print("Must be greater than " + fmt_min)

            elif v > max_val:
                print("Must be less than " + fmt_max)

            else:
                break

        except:
            
            print("Invalid number, try again!")

    v,dp = Compact(v)

    return v

############################################################

def InitViewVars():

    # Initialises all view variables except ViewRect which
    # will have been generated by the initial menu

    global ZoomRect, Dragging, Closing, Quitting

    ZoomRect = None
    Dragging = False
    Closing = False
    Quitting = False

    InitPalette()
    InitMap()

############################################################

def InitViewWindow():

    global Surface, Image
    
    if sys.platform == 'win32' or sys.platform == 'win64':
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    
    icon = pygame.Surface((1,1))
    icon.set_alpha(0)
    pygame.display.set_icon(icon)

    EnableEvents(ALL_EVENTS)
    
    Surface = pygame.display.set_mode((SW,SH))
    Image = pygame.Surface((SW,SH))

############################################################

def InitMap():

    global Map

    Map = [[0] * SH for x in range(SW)]

############################################################

def InitPalette():

    # Sets up standard colors, initialises balanced colors
    # to match standard colors and sets pixel counts to zero.
    # Currently using a linear greyscale from white to black. 

    global Palette

    Palette = [None] * MAX_DEPTH

    pix = 0
    
    for m in range(MAX_DEPTH):

        v = round(255*m/(MAX_DEPTH-1))

        r = 255 - v
        g = 255 - v
        b = 255 - v

        std = [r,g,b]
        bal = std

        Palette[m] = [std, bal, pix]

############################################################

def ClearPalette():

    # Clears all pixel counts in palette

    global Palette

    for m in range(MAX_DEPTH):
        Palette[m][2] = 0

############################################################

def BalancePalette():

    # Balance/re-balance color palette based on pixel counts
    # already generated for each Mandelbrot value during Pass
    # One of Calc(). Balancing is achieved by identifying the
    # minimum and maximum Mandelbrot values which account for
    # 98% of all pixels on the screen i.e at least 1% are below
    # min threshold and at least 1% are above max threshold.
    # Ignoring 2% of pixels at either extreme reveals enough
    # detail at either extreme while preventing tiny hot spots
    # from skewing the color balance. The min and max values
    # thus obtained are then used to calculate offset and gain
    # parameters for generating balanced colors. The objective
    # is to give the most efficient and informative visual
    # representation for any given view within normal computing
    # constraints. 

    global Palette

    max_d = MAX_DEPTH
    pixels = SW * SH
    
    min_thresh = pixels/100     # 2.5%
    max_thresh = pixels/100     # 2.5%

    min_pixels = 0
    max_pixels = 0
  
    for m in range(0, MAX_DEPTH, 1):

        min_m = m
        min_pixels += Palette[m][2]
        
        if min_pixels >= min_thresh:
            break

    for m in range(MAX_DEPTH-1, -1, -1):

        max_m = m
        max_pixels += Palette[m][2]
        
        if max_pixels >= max_thresh:
            break
   
    # Calculate offset and gain that will render
    # Mandelbrot values using full palette range 

    if max_m == min_m:
        offset = 0
        gain   = 1.0
    else:
        offset = min_m
        gain   = (max_d-1)/(max_m - min_m)
   
    # Now update palette balanced colors

    for m in range(0, MAX_DEPTH, 1):

        b = int(gain * (m - offset))
        if b < 0: b = 0
        if b >= max_d: b = max_d - 1
        
        Palette[m][1] = Palette[b][0]


############################################################

def EnableEvents(events):

    # Enables only the events listed and cleares event queue
    
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(events)
    pygame.event.clear()

############################################################

def Calc():

    # Calculates and renders current view of Mandelbrot Set

    global Map, Closing
    
    PrintView()

    # This is computationally-intensive, so use
    # pre-calculated local variables for efficiency

    max_d = MAX_DEPTH
    
    sw = SW
    sh = SH

    # Get complex coordinates at top left of screen
    # noting that y axis have opposite directions

    cw = ViewRect[2]
    ch = ViewRect[3]
    cx = ViewRect[0] - cw/2
    cy = ViewRect[1] + ch/2

    # Clear pixel counts in Palette

    ClearPalette()

    # PASS ONE - CALCULATE MANDELBROT VALUES
   
    sx_percent = 100/sw
    progress = 0.0

    # Only allow Window QUIT events while calculating
    
    EnableEvents(QUIT)
   
    for sx in range(sw):

        # When each column is completed, this is a good time
        # to check for a window close attempt. Polling events
        # is also necessary to give Pygame a chance to respond
        # internally to operating system events such as windows
        # move. This is also a good time to update progress
        # indicator and increment the percent count. This adds
        # about 10% overhead for the fastest calculations in the
        # lightest regions. But this figure approaches 0% in the
        # darkest regions where calculation time really matters.

        if pygame.event.poll().type != NOEVENT:
            Closing = True
            return

        pygame.display.set_caption("Calculating " +format(progress,".2f")+"%")
        progress += sx_percent

        for sy in range(sh):
        
            re = cx + cw*(sx/sw)
            im = cy - ch*(sy/sh)
            
            z = complex(re,im)
            c = z
            
            for m in range(max_d):
                z = z*z + c
                if abs(z) >= 2.0: break

            # Save value for Pass Two

            Map[sx][sy] = m

            # Update palette pixel count for this value
            
            Palette[m][2] += 1

        #endfor

    #endfor

    # Re-balance palette colors using pixel counts generated
    # in Pass One. These will be used for rendering in Pass Two

    BalancePalette()

    # PASS TWO - RENDER MANDELBROT VALUES

    for sx in range(sw):

        for sy in range(sh):
            
            m = Map[sx][sy]
            Image.set_at((sx,sy),Palette[m][1])
            
        #endfor

    #endfor

    EnableEvents(ALL_EVENTS)
    pygame.display.set_caption("Ready")

############################################################

def Draw():

    # Draws/re-draws the current Mandelbrot set image and
    # overlays the zoom rectangle if present. ZoomRect is
    # an absolute non-normalised rect because it needs to
    # retain start coordinates during dragging. However
    # pygame.draw.rect needs a relative rect whose width
    # and heights are non-negative and non-zero.
    
    Surface.blit(Image,(0,0))
    
    if ZoomRect != None:
        rect = RelRect(NormRect(ZoomRect))
        pygame.draw.rect(Surface,(255,0,0),rect,1)
   
    pygame.display.flip()

############################################################

def AbsRect(r):

    # Converts a screen rectangle in the form (x,y,w,h)
    # to one with absolute coordinates (x1,y1,x2,y2).
    # Note that widths and heights must be non-zero and
    # positive. A width and height of 1 pixel will
    # produce identical start and end coordinates 

    x1 = r[0]
    x2 = r[0] + r[2] - 1
   
    y1 = r[1]
    y2 = r[1] + r[3] - 1
    
    return (x1,y1,x2,y2)

############################################################

def RelRect(r):

    # Converts a screen rectangle in the form (x1,y1,x2,y2)
    # to one with relative coordinates (x,y,w,h). Note that
    # identical start and end coordinates will produce a
    # width and height of 1 pixel. Input rectangle must be
    # normalised.

    x1 = r[0]
    w = r[2] - r[0] + 1
   
    y1 = r[1]
    h = r[3] - r[1] + 1
    
    return (x1,y1,w,h)

############################################################

def NormRect(r):

    # Normalises a rectangle with absolute coordinates so that
    # the returned x1,y1 coordinates are less than x2,y2.

    x1 = r[0]
    y1 = r[1]
    x2 = r[2]
    y2 = r[3]

    if x1 > x2:
        x1,x2 = x2,x1

    if y1 > y2:
        y1,y2 = y2,y1
        
    return (x1,y1,x2,y2)

############################################################

def Compact(r):

    # Converts raw floating point number into most compact
    # decimal form that meets the required precision. Also
    # returns number of decimal places used.

    if r == 0.0:
        return r,0
    elif r < 0:
        neg = True
    else:
        neg = False

    r = abs(r)

    dp = -floor(log10(r))

    while True:
        
        c = round(r,dp)
        
        if abs((c-r)/r) <= PRECISION:
            break
        
        dp = dp + 1
        
        if dp > MAX_DP:
            c = r
            dp = MAX_DP
            break

    if neg: c = -c
    
    return c, dp
 
############################################################

def CompactView():

    # Returns compacted version of view coordinates using
    # maximum precision required across all 4 values
    
    vx,vy,vw,vh = ViewRect

    cx,dpx = Compact(vx)
    cy,dpy = Compact(vy)
    cw,dpw = Compact(vw)
    ch,dph = Compact(vh)

    maxdp = max([dpx,dpy,dpw,dph])

    return [FmtDp(v,maxdp) for v in ViewRect]

############################################################

def PrintView():

    x,y,w,h = CompactView()
   
    print("Center X = ", x)
    print("Center Y = ", y)
    print("Width    = ", w)
    print("Height   = ", h)
    print("-----------------------------------------------------------------")

############################################################

def FmtDp(f,dp = None):

    # Formats floating point value with indicated decimal
    # or MAX_DP if dp argument is not supplied
        
    if dp == None:
        dp = MAX_DP

    return format(f," ." + str(dp) + "f")

############################################################

def WithinZoomRect(x,y):

    # Returns True if x,y location is within zoom rectangle

    n = NormRect(ZoomRect)

    if x < n[0] or x > n[2] or y < n[1] or y > n[3]:
        return False
    else:
        return True

############################################################

def Zoom():

    # Generates new view based on zoom rectangle which is
    # subsequently cleared. Zooming full screen or beyond
    # the zoom limit will retain the current view while
    # clearing the zoom reactangle. Because the zoom
    # rectangle is integer based, it may have slight
    # aspect-ratio errors. For critical floating point
    # calculations, derive height from width using the
    # global aspect-ratio.

    global ViewRect, ZoomRect

    # Map ZoomRect to ViewRect coordinate system
    # which is centered with y increasing upwards

    rz = RelRect(NormRect(ZoomRect))
  
    rx,ry,rw,rh = [float(r) for r in rz]
    
    zw = rw
    zh = rw/AR
    zx = rx - SW/2 + zw/2 
    zy = -(ry - SH/2 + zh/2)

    # Can now generate new view using simple scaling

    vx,vy,vw,vh = ViewRect

    nx = vx + vw*zx/SW
    ny = vy + vh*zy/SH
    nw = vw*zw/SW
    nh = nw/AR

    new_rect = [nx,ny,nw,nh]

    if nw < MIN_WIDTH:
        
        print("Zoom Limit")
        print("-----------------------------------------------------------------")

    elif new_rect != ViewRect:

        ViewRect = new_rect
        Calc()

    #endif

    ZoomRect = None
    Draw()

############################################################

def StartDrag(mx,my):

    global Dragging, ZoomRect

    Dragging = True
    ZoomRect = [ mx, my, mx, my ]
    
    Draw()

############################################################

def UpdateDrag(mx,my):

    # Drags zoom rectangle while preserving aspect ratio
    # and limiting to screen area. Note that the zoom area
    # width is never zero regardless of drag direction

    global ZoomRect

    x1,y1,x2,y2 = ZoomRect

    if mx < 0: mx = 0
    if mx >= SW: mx = SW-1
  
    if my < 0: my = 0
    if my >= SH: my = SH-1

    w = abs(mx - x1) + 1
    h = round(w/AR)

    y2 = y1 + h - 1 if my >= y1 else y1 - h + 1

    if y2 < 0 or y2 > SH-1:
        y2 = 0 if y2 < 0 else SH-1
        h = abs(y2 - y1) + 1
        w = round(h*AR)

    x2 = x1 + w - 1 if mx >= x1 else x1 - w + 1

    ZoomRect = [x1,y1,x2,y2]
    Draw()

############################################################

def EndDrag():

    global Dragging
    
    Dragging = False
    Draw()

############################################################

def ClearZoomRect():

    global ZoomRect

    ZoomRect = None
    Draw()
    
############################################################

def GetEvent():

    # Awaits OS and mouse event for view window. Sleeps
    # while waiting so as not to hog CPU. Allowed events
    # are pre-filtered to minimise wasteful processing.
    # Events are processed one at a time as they arrive
    # off the event queue.
    
    global Closing

    event = pygame.event.wait()
       
    if event.type == QUIT:
        Closing = True
        return

    mx, my = pygame.mouse.get_pos()

    if event.type == MOUSEBUTTONDOWN and event.button == 1:

        if ZoomRect == None:
            StartDrag(mx,my) 
        else:
            if WithinZoomRect(mx,my):
                Zoom()
            else:
                ClearZoomRect()
        return

    if event.type == MOUSEMOTION:
                    
        if Dragging: UpdateDrag(mx,my)   
        return

    if event.type == MOUSEBUTTONUP and event.button == 1:

        if Dragging: EndDrag()
        return

############################################################

def ViewLoop():

    # Initialises view-related variables and opens view window.
    # Generates initial Mandelbrot view and then waits for and
    # processes window events repeatedly until window is closed.

    print("-----------------------------------------------------------------")
    print("Generating Initial View")
    print("-----------------------------------------------------------------")

    InitViewVars()
    InitViewWindow()

    Calc()
    Draw()

    while not Closing: GetEvent()

    pygame.quit()
        
############################################################

def MainLoop():

    # Repeatedly presents initial menu until user finally
    # quits. If valid view coordinates are supplied from
    # the initial menu, enters view loop 

    while True:

        InitMenu()
        if Quitting: break
        if ViewRect != None: ViewLoop()

############################################################
# START OF PROGRAM
############################################################

print("Mandelbrot Viewer 1.0 Copyright (C) RVJ Callanan")
print("This is FREE software released under the GPLv3")
print()

MainLoop()

sys.exit()

############################################################
# END OF PROGRAM
############################################################
