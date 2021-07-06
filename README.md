# pet-desiese-detection-Computer-vision
PETNOSTICS PEE ANALYSING

Instructions for application develpoment:


1.	IPHONE APPLICATION DEVELOPMENT: 
	iPhone apps using Python. PyMob™ is a technology which
	allows developers to create Python-based mobile apps where 	the app specific python code is compiled via a 	compiler 	tool and converts them into native source codes for each 	platform like iOS. 

	KIVY can also tackle IOS decription given below in 2.

2.	ANDROID APPLICATION DEVELOPMENT: 
	Kivy is a free and open source Python library for developing 	mobile apps and other multitouch application software with a 	natural user interface(NUI). It is distributed under the 	terms of the MIT License, and can run on Android, iOS, 	GNU/Linux, OS X, and Windows.
3.	LAYOUT of application:
	Draw Two straight parallel vertical lines on the screen for 	strip detection. Because the strip can only be detected if 	it is fully stright and in the middle of screen. with margin 	from below and above.... As SHOWN IN FIG.1
	I.E.

			 ______________________
			 |				|
			 |				|
			 |	   ______		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    |	  |		|
			 |	    -----		|
			 |				|
			 ----------------------
				    FIG.1		

4.	BRIGTNESS of images:
	The image of stirp should be taken in bright light so the 	color can be detected more clearely and accuratly.

5.	Background of images:
	The image should be taken with lighter background meaning
	the pictre of strip should be taken on white paper or white 	background.... AND no distraction should be placed near 	image so that image contains only strip and white 	background. NO OTHER DISTRACTION...


-----------------------------------------------------------------


INSTRUCTION ON RUNNING THE PYTHON CODE

1.	The code of strip detection is named "shapedetection.py"
2.	Run the code of "shapedetection.py" and then call the 	function "shape_detect(path)" with giving the "path of 	image" or "image name" if image is saved in same folder.. 	like.......... 
		
	"import shapedetection
	 shape_detect('7.jpg') "


3.	This code will output image "DETECTED.JPG" with ever color 	detected with its value i.e. if the strip is default(meaning 	clean strip with out the pee) or some value of each test 	i.e. neg or other thing.


-----------------------------------------------------------------



THE PROJECT FOLDER CONTAINS 

1.	IMAGES FILES WHICH CAN BE LOADED
2.	CODE/SCRIPT FILE NAME "shapedetection.py"
3.	FOLDER NAME "data" WHICH CONTAINS CSV FILES THAT CONTAINS 	THE TEST COLORS NEEDED FOR COLOR MATCHING AND IS USED BY 	"shapedetection.py".
4.	FOLDER NAME "DETECTED IMAGES" WHICH CONTAINS STRIP DETECTED 	IMAGES ONE IS ON MANUALLY MODIFIED STRIP I.E.(17.JPG) WHICH 	DETECT THE VALUES OF TESTS AND OTHER IS ON DEFAULT IMAGE 	I.E. (7.JPG)
5.	CHEAT SHEET.JPG WHICH WAS USED FOR DISEASE COLOURS.

_________________________________________________________________

