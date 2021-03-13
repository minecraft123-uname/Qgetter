# Qgetter
Qgetter can get the headimage and nickname of a QQ user, or the head image of a QQ group by a known QQ ID or QQ group ID.
Qgetter is based on the open Tencent™ QQ headimage and nickname API interface.
Note: If U did not get a satisfactory result, please check does your QQ ID or GROUP ID exists.
--Written by Sun Xiao

Example 1(the examples are made up):\n
	Command: 
		Qgetter -m hi -i 123456789 -s image.jpg
	Output:
		Already saved the head image of 123456789 to image.jpg.
	// Save the headimage of the QQ user with QQ ID 123456789 to image.jpg.

Example 2:
	Command:
  	Qgetter -m hn -i 123456789 -s image2.jpg
  Output:
  	Already saved the head image of 123456789 to image2.jpg.
		The nick name of 123456789: xxx
  // Save the headimage of the QQ user with QQ ID 123456789 to image.jpg, and output the nickname.

Example 3:
	Command:
  	Qgetter -m nk -i 123456789
  Output:
  	The nick name of 123456789: xxx
  // Output the nickname. U need not to use -s/--save option in this situration.
  
Example 4:
	Command:
  	Qgetter -m gh -i 234567890 -s image3.jpg
  Output:
  	Already saved the group image of 861641611 to image3.jpg.
	// Save the headimage of the QQ group with ID 234567890 to image3.jpg.

Note: Qgetter can not get the name of a QQ group yet so far.
