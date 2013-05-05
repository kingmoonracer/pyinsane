import src.abstract as pyinsane
import sys

# Set options
name = 'epkowa:net:192.168.1.8'
res = 300
mode = 'Gray'
scan_area = 'Letter'

# Get scanner instance
device = pyinsane.Scanner(name=name)

# Set scanner options
device.options['resolution'].value = res
device.options['mode'].value = mode
device.options['scan-area'].value = scan_area

scan_instance = device.scan(multiple=False)
try:
    PROGRESSION_INDICATOR = ['|', '/', '-', '\\']
    i = -1
    while True:
        i += 1
        i %= len(PROGRESSION_INDICATOR)
        sys.stdout.write("\b%s" % PROGRESSION_INDICATOR[i])
        sys.stdout.flush()

        scan_instance.read()
except EOFError:
    pass
image = scan_instance.get_img()

# Convert the image to mode "1" when doing Binary so the file size is smaller
if (mode == 'Binary'):
    print("Converting image...")
    image = image.convert('1')

# Set filename of output image
filename = "{}_{}_{}_python".format(mode,res,scan_area)

# Save the image file
image.save("output/pdf/{}.pdf".format(filename),"PDF")
image.save("output/tiff/{}.tiff".format(filename),"TIFF")