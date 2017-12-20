
![Logo](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/media/logo.png)

### Created by Luke Halley
### Student Number: 20071820
### [Github Respository](https://github.com/lukehalley/PycomCarpark)


## Description Of The Project
Pycom Carpark is a project developed using IoT standards and protocols. 

The aim of this project was to develop a small device which would sit at the entrance of any car park and collect count the amount of cars entered.

All the technology used in this project is relatively cheap, which would allow any person with the technical ability to configure it to their needs, use it for their own purpose.


## Technogies Used & Their Purpose
### Pycom With A SiPy Board:
![](https://pycom.io/wp-content/uploads/2017/06/sipySide.png)

The SiPy is a multi-network (Sigfox, WiFi and BLE) development platform. It is programmable with MicroPython and the Pymakr IDE for fast IoT application development, easy programming in-field and extra resilience with network failover. The best blend of speed to deployment and access to new LPWAN networks rolling out across Europe, USA, Africa and India. You can also configure the SiPy in FSK mode to send packets directly from SiPy to SiPy. This way you can create the network configuration of your choice and then use another SiPy as central Nano-Gateway to forward the data to the cloud via WiFi. The module is CE, FCC, IC and RCM certified!

The button on the Pycom board was used to siumulate both cars passing and other objects like bikes and people passing by. 

These values are taken every **10 minutes** for **1 hour** until these 12 values (Cars passed and Others) are averaged and sent to the sigfox backend as a byte array with these two values, the time they were recorded and finally theyre sequence number to ensure consistency (time (time) and sequence number (seqNumber) is provided by the sigfox backend)

### Sigfox:
![](https://www.sigfox.com/themes/sigfox/logo.svg)

Sigfox is a French company founded in 2009 that builds wireless networks to connect low-energy objects such as electricity meters, smartwatches, and washing machines, which need to be continuously on and emitting small amounts of data

The sigfox backend enabled me to take the data that had been sent from my SiPi board and make use of it.

![](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/screenshots/sigfox_callbackSC.png)

### mLab:
![](https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/MLab_company_logo.svg/1280px-MLab_company_logo.svg.png)

mLab is a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers.

mLab took the datasent from the sigfox backend and put them into a NoSQL datbase. This process was done through mLabs [Restful API.](http://docs.mlab.com/data-api/)

![](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/screenshots/mlab.png)

### Freeboard:
![](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/media/freeboard.jpg)

Freeboard is a real-time, interactive dashboard and visualization tool which can be used to create a dashboard in minutes using the intuitive drag & drop interface.

![](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/screenshots/mydash.png)

### Atom & PyMaker:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Atom_editor_logo.svg/2000px-Atom_editor_logo.svg.png)

Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows with support for plug-ins written in Node.js, and embedded Git Control, developed by GitHub.

Pymakr is a plug-in for the Atom IDE that allows you to get your code from your PC to your board.

It’s a fully featured IDE that connects automatically to your Pycom devices via Telnet Server or serial port, runs your code on the fly, manages the internal file system, synchronizes your code instantly and runs it with just one click. It also takes care of firmware upgrades and includes a built in console that interfaces with the MicroPython REPL. Features code completion, static analysis, PEP8 style checking and a built-in interactive prompt.

![](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/screenshots/atom.png)

## Version Control
![](https://sunlightmedia.org/wp-content/uploads/2017/02/github-bb449e0ffbacbcb7f9c703db85b1cf0b.png)
For version control, Github was used. I broke the development of the project into **stories** and commited to my repository each time a story was completed.

## Future Features
* The dashboard could be displayed on a screen of an entrance to a carpark to allow people to know how many car spaces are left.

* Push notications which would warn people if the car park was full of rapidly filling up.

* Visual integration with CCTV cameras which would check if there was cars in space as well as knowing which space they are in.

## Problems
*Wouldnt it count any object going out of the car park?* 

The devices sensor would be limited to a certain range to prevent this

## Developer Experience
I ensured a high standard of developer experience by adding comments into my code which explains the functions of the code and its use. I also ensured all commits to GitHub were informitive and easy to understand.

## References
Any specific code snippets that were used by the SiPy board were retrived from the [Pycom Documentation"](https://docs.pycom.io/).
