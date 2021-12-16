# Hey... Welcome to CoderMohit.
# In this Video I'll create QR Code Generator.

# Firstly we need a module named as - MyQr
# So install it by using pip

# Now import that module

from MyQR import myqr

# TO generate a Normal QR Code

myqr.run('https://techycodes.tech/', save_name='TechyCodes.png')
# Here we have to put the Url that we want to convert it in QR

# This code is for Basic QR Code Generator

# if you want to generate a Customized QR Code then follow me .

# Firstly you need this image or you can take any image.

# i have taken this image..

myqr.run(words='https://techycodes.tech/',picture='test-image.jpg',
         colorized=True, save_name='Customized-QR-Code.png')

# now Run this code by right click then select current file name.
# So this is how you can create any type of QR code with every URLS.

# if you like this tutorial then Share this video and subscribe this channel.


# Code Link in Description.
