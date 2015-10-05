# Premultiply Images #

Simply premultiply the alpha of images.  It's written in Python but runs quickly because it uses Numpy.

The main problem with this program is that you have to install its dependencies to get it to work.  That can be time consuming and annoying.  Also, Pillow has been known to break its own APIs from time to time.

## Dependencies ##

 - Numpy
 - Pillow (the friendly PIL fork)

`easy_install Pillow`
`easy_install numpy`

Usage:

    python imgpremultiply.py *.png


## Patch request ##

I would accept a patch that detects whether PIL is installed and just runs a slow Python-only version if it is not.  Most people don't need the speed and it just takes longer to install the dependency than the time saved to use it.

