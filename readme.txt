Convert Amazon Data into Volusion Data

These are some custom scripts I wrote to help convert data that was used to create Amazon Listing, into data that was useable for Volusion.
I am not an expert in the data structure for Amzaon but considering it was the data I was given I assume that it is the typical way to structure data for upload into Amazon, and as such I figured the scripts would be useful to others. They are in no way "production ready", but if you know something about Python, you should be able to adapt them for your own needs, and perhaps if others wanted to collaborate we could turn it into a more polished project!

As it is currently set up there are a nuber of steps required to make it work

1) Gather all csv files containing Amazon data into a directory called input/originals (the ones I worked with were in the format found in AmazonDataExample.csv found in this repo
2) Gather all photos into a directory called input/photos-all
3) Download Amavolpy (sort for Amazon, Volusion, Python) into the containing project directory

now your directory structure should look like this

container (call it whatever you want)
--input
----photos-all (containing all photos)
----originals (containing all Amazon data csv files, can be numerous files)


4) I have a process that converts all sales data downloaded from Amzon, into a price list, if you will create your own price list, you will need to disable this feature in the workflow script, and place the pricelist in the output diriectory.
5) now run the workflow.py script ( you may need to make adjustments to some of the parameters to match your directory structure and file names)
if you already have options in your Volusion db you will need to set the option number to the larget option id + 1 (or any number higher than your larget option id)

6) upload the output/options.csv  file to options in Volusion (you may want to first get rid of duplicates using excel)
7) upload output/products.csv into products in volusion (you ay want to first get rid of duplicates using excel)
8) upload output/masters-options.csv into products in Volusion (you ay want to first get rid of duplicates using excel)

9) create a dir called output/photos and another called output/options
10) Picture time .... using volusions photo app (forgot what its called) first run it using children_photos.csv and setting the options dir as the output file
11) run children_photos_renamer.py

12) using volusions photo app (forgot what its called) run it using photos.csv and setting the photos dir as the output file

13) you are ready to upload the photos in photos and the options into options using ftp (you can get the deatails of where they aare found in the volusion help section.

14) i have included a shadowmaker.py to make shadow products if you use sellercloud.com (it is tricky at best but good luck!)

