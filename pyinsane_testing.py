from src import abstract as pyinsane

# Set options
name = 'epkowa:net:192.168.1.8'
res = 300
mode = 'Binary'
scan_area = 'Letter'

# Get scanner instance
device = pyinsane.Scanner(name=name)

# Set scanner options
device.options['resolution'].value = res
device.options['mode'].value = mode
device.options['scan-area'].value = scan_area

scan_instance = device.scan(multiple=False)
try:
    while True:
        scan_instance.read()
except EOFError:
    pass
image = scan_instance.get_img()

# Set filename of output image
filename = "{}_{}_{}_python.pdf".format(mode,res,scan_area)

# Save the image file
image.save("/home/isaac/spyder/pyinsane/output/{}".format(filename))
