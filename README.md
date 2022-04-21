# Chatbot

## Member Info

Yuwei Tang    21442946

Weiming Mai  21422885

## Chatbot Feature Introduction

Traditional and regular social activities cannot be carried out routinely because to the covid 19 epidemic and the social locking down. As a result, people are attempting to socialize via internet platforms. To stay in touch with their pals, people employ a variety of cloud services.

This project creates and deploys a Telegram-based chatbot robot. People can use this robot to query a list of TV series they want to watch, get extensive information about TV shows, and exchange posters from their favorite shows. Use Firebase's cloud database to store the requested data, and the REST API supplied by tvmaze to perform snapshots and data exchanges. We deployed our program using Microsoft's Azure platform and containerized it using Docker.

 

 

|      |                                                              |      |                                                              |
| ---- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
|      | ![手机的屏幕截图  描述已自动生成](README.assets/clip_image003.png) |      | ![手机屏幕的截图  描述已自动生成](README.assets/clip_image004.png) |
|      |                                                              |      |                                                              |


A lot of the time, we don't know what a TV show is called. We usually just remember a few letters or a portion of a name. We can acquire a list of prospective TV shows by typing a few letters using tvmaze's api, which allows us to do fuzzy search for names. In the chatbot, we utilize the inlinebutton to display the list in the dialogue box as a list. At the same time, we save the data we find in our FIREBASE database to make future queries easier and the system run faster.



We'll select the key information we want to display as callback data and feed it to each button when we construct the list. When the button is pressed, we can use the callback data to track the relatively vast and complex information in the database, such as genre and posters. The exact information of the TV show we clicked in the dialog box is then displayed.

![图形用户界面, 网站  描述已自动生成](README.assets/clip_image006.png)

The database reduces the time it takes for our system to function, retrieves the information we need from a large online public database, and boosts the system's flexibility and scalability. It provides quick information support for our system, much like a dynamic cache. We can distribute larger messages, such as posters from TV shows we uncover, and send messages to bots, owing to database support.

![截图里有图片  描述已自动生成](README.assets/clip_image008.png)

## Deployment Procedure

The app is hosted on Azure, we create two containers to run two independent chat bot for two users.

## References

[Azure]: https://app.diagrams.net/?src=about

