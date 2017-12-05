
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
![](https://blog.thethings.io/wp-content/uploads/2017/08/sipy-hardware-thethingsio.png)

The SiPy is a multi-network (Sigfox, WiFi and BLE) development platform. It is programmable with MicroPython and the Pymakr IDE for fast IoT application development, easy programming in-field and extra resilience with network failover. The best blend of speed to deployment and access to new LPWAN networks rolling out across Europe, USA, Africa and India. You can also configure the SiPy in FSK mode to send packets directly from SiPy to SiPy. This way you can create the network configuration of your choice and then use another SiPy as central Nano-Gateway to forward the data to the cloud via WiFi. The module is CE, FCC, IC and RCM certified!

The button on the sigfox PyMaker was used to siumulate both cars passing and other objects like bikes and people passing by.
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
![](https://netgauges.net/wordpress/wp-content/uploads/2016/02/freeboard_logo-300x105.jpg)

mLab is a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers.

mLab took the datasent from the sigfox backend and put them into a NoSQL datbase. This process was done through mLabs [Restful API.](http://docs.mlab.com/data-api/)

![](https://raw.githubusercontent.com/lukehalley/PycomCarpark/master/screenshots/mlab.png)

## Persistence

**MongoDB** & **Mongoose** was used for persistance. **MongoDB** is a free and open-source cross-platform document-oriented database program. **Mongoose** is a **MongoDB** object modeling tool designed to work in an asynchronous environment. All information about all Instruments and Users were stored in the database.

**mLab** was used to store data in the cloud. mLab is a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers.

## Deployment
![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/AmazonWebservices_Logo.svg/2000px-AmazonWebservices_Logo.svg.png)

Instrum.io was deployed using **Amazon Web Services**. Amazon Web Services is a subsidiary of Amazon.com that provides on-demand cloud computing platforms to individuals, companies and governments, on a paid subscription basis with a free-tier option available for 12 months.

Unfortunatly due to this being a paid service the web application isnt currently availble to the access.

## Version Control
![](https://sunlightmedia.org/wp-content/uploads/2017/02/github-bb449e0ffbacbcb7f9c703db85b1cf0b.png)
For version control, Github was used. I broke the development of the application into **stories** and commited to my repository each time a story was completed.

## Problems
*Wouldnt it count anything going out?* 

The devices sensor would be limited to a certain range to prevent this

## Developer Experience
I ensured a high standard of developer experience by adding comments into my project's files which explains the functions of the code and its use. I also ensured all commits to GitHub were informitive and easy to understand.

## References
Skeleton code was created by following David Drohans ["Web App Development 2"](https://ddrohan.github.io/wit-wad/) tutorials).

Design of the website was created using [AdminBSBMaterialDesign](https://github.com/gurayyarar/AdminBSBMaterialDesign), a fully responsive and free admin template. It is developed with Bootstrap 3.x Framework and Google Material Design of powers. Note: A small amount off custom CSS was added and edited in order to suit the application.

NPM packages used: [MongoDB](https://www.npmjs.com/package/mongodb), [Mongoose](https://www.npmjs.com/package/mongoose) and [Node](https://www.npmjs.com/package/node)