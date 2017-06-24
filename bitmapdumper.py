#!python
#bitmapdumper.py
# Dumps bytes from bitmap
import sys

# For ePaper E2215CS062 size is 208 x 112 pixels
# Code has been modified to work only with exactly 208 x 112 pixel image in 
# Image needs to be created from the bottom up.
# Image text needs to be mirrored left/right then rotated clockwise 90 degrees

FILE_SOURCE = "logo.bmp"

# Skip header information
HEADER_SIZE = 14
LINE_SIZE   = 26

header = []

if len(sys.argv) > 1:
	if sys.argv[1] in ["-h","--help"]:
		print "USAGE: python bitmapdumper.py [src.bmp] > output.c"
		print "   Outputs bytes of bitmap image"
		print "   Image must be Monochrome 208 x 112 pixels"
		print "   Cut and paste generated code into source file"
		exit()


if len(sys.argv) >= 2:
	FILE_SOURCE = sys.argv[1]

try:
	file = open(FILE_SOURCE,'rb')
except:
	print "Problem with filename: %s" % FILE_SOURCE
	exit()

# Read header
try:
	for count in range(0, HEADER_SIZE):
		byte = file.read(1)
		header.append(ord(byte))
finally:
	pass

#Show header
print "HEADER: %c%c" % (chr(header[0]), chr(header[1]))
# Calculate size
datasize = header[5]
datasize = (datasize*256) + header[4]
datasize = (datasize*256) + header[3]
datasize = (datasize*256) + header[2]
# Calculate offset
offsetsize = header[13]
offsetsize = (offsetsize*256) + header[12]
offsetsize = (offsetsize*256) + header[11]
offsetsize = (offsetsize*256) + header[10]

print "SIZE: %i bytes" % (datasize)
print "OFFSET: %i bytes" % (offsetsize)


# Read rest of header to start of pixel data
try:
	for count in range(HEADER_SIZE, offsetsize):
		byte = file.read(1)
		header.append(ord(byte))
finally:
	pass

# Look at next header info
# Calculate pixel width
pixelwidth = header[HEADER_SIZE+7]
pixelwidth = (pixelwidth*256) + header[HEADER_SIZE+6]
pixelwidth = (pixelwidth*256) + header[HEADER_SIZE+5]
pixelwidth = (pixelwidth*256) + header[HEADER_SIZE+4]
# Calculate pixel height
pixelheight = header[HEADER_SIZE+11]
pixelheight = (pixelheight*256) + header[HEADER_SIZE+10]
pixelheight = (pixelheight*256) + header[HEADER_SIZE+9]
pixelheight = (pixelheight*256) + header[HEADER_SIZE+8]

print "IMAGE: %i x %i pixels" % (pixelwidth, pixelheight)
print ""

LINE_SIZE = (pixelwidth/8)+2

LINE_SIZE = 14

###---------------------------------------------------------------------
# FORMAT FOR CODE
###---------------------------------------------------------------------

print "byte _buffer [] = { // Cedric Computer Engineering Splash Screen"

# Read each line and output only valid bytes formatted for pasting into code
count = 0
total = 0
reset = 0
try:
	byte = file.read(1)
	while byte != "":
		if count < LINE_SIZE:
			# New line?
			if reset == 0:
				print "   ",
				reset = 1
			# Reverse bit values
			n = ~ord(byte) & (0xFF)
			print "0x%02X," % (n),
			total += 1
		count += 1
		# Print new line where appropriate
		if count >= LINE_SIZE:
			# Exclude next two pad bytes
			if count >= LINE_SIZE+2:
				print ""
				count = 0
				reset = 0
		# Output byte
		byte = file.read(1)
finally:
	file.close()
	if reset == 1:
		print ""

print "};"
print ""

print "TOTAL: %i bytes" % (total)
print "TOTAL: %i pixels" % (total*8)
