# Youtube-Downloader
A simple Youtube video downloader built using Pytube and Tkinter

Pytube python library was used to provide the main functionalities of the application. Tkinter was used to create the GUI.

Upo launch, the applications asks the user to input the link of the video to be downloaded along with the resolution required.
In case of the following errors,
  1. The link being invalid
  2. The resolution entered is invalid
  3. The required resolution is not available.
  the application notifies the user of the error using an error window. And allows the user to correct them.
  
If the details entered are correct, a confirmation window appears with the details of the video such as the name, size and length.
Then the user can choose either to go back or to download the particular video.

The default download location is the downloads folder in the C drive.

Once the video is downloaded, it is notified to the user via a success message. Upon this the application doesn't close and instead it clears out the fields.
The user can use the application again without restarting.
