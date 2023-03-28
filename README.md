# Youtube-Downloader

A simple Youtube video downloader built using Pytube and Tkinter which can be used in Windows and Linux systems.

Pytube library was used to provide the main functionalities of the application. Tkinter was used to create the GUI.

Upon launch, the applications asks the user to input the link of the video to be downloaded along with the resolution required.
In case of the following errors,

1. The link being invalid
2. The resolution entered is invalid
3. The required resolution is not available.
   the application notifies the user of the error and allows the user to correct them.

If the details entered are correct, a confirmation window appears with the details of the video such as the name, size and length.
Then the user can choose either to go back or to download the particular video.

The default download location is the downloads folder.

Once the video is downloaded, it is notified to the user via a success message. The user can use the application again without restarting.

</br>

## Launch

The application can be launched via the command line or using an executable file

</br>

### Executable file

To generate the executable file, `PyInstaller` is required. Install it using `pip install pyinstaller`.
After installing open the command line in the application directory and use `pyinstaller --onefile Youtube_Downloader.py`. After the process finishes, the executable can be found inside the `dist` directory.

</br>

### Command line

To run the application from the command line, `pytube` and `tkinter` is required in the python environment.
Use `pip install tkinter pytube` to install them.
Then use your prefered interpreter to run the `Youtube_Downloader.py` to launch.
