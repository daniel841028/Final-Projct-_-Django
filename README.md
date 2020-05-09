
# JHUstudentRide_Final_Project(WEB)
Final project for Software Carpentry Class. We wrote a WEB in python to show our idea using Django.

About JHUstudentRide:

Welcome to JHUStudentRide! We are excited to have you in our community. It is well-known that the crime rate in Baltimore is extremely high. It is risky to take random rides from non-authorized drivers. Therefore, we hope to offer safe rides for JHU students. We will only accepted JHU students and good-recorded drivers to this community so we need to confirm your identity before offering any service.

In this WEB,   we learned how to setup Django, write App, use	Bootscrape and CSS for styling and write HTML codes. Furthermore, we learned how to collect data in SQLite database. The username, password, trip information, emails are all collected in the database.

How to use?

(1)	You will first visit our JHUstudentRide homepage Then, you have to register for a user account.

(2)	Please filed up the form and be aware of we only accept JHU email. Please do not use other emails. Then, click submit.   After successfully registration, you can log into your account from the homepage.

(3)	If you are a driver, please click on “I’m a Driver”. If you are a user, please click on “Pick me up”.

(4)	Drivers can add new trip by filling up the register for a trip form, including time, departure and destination. Then, drivers will see the registered trip shown in your manage webpage. If the route you offer does not exist anymore, please click on the cancel bottom. This trip will disappear from your manage page. (Note: you cannot cancel the trip if that is not register by you)

(5)	On the other hand, user can see all offered rides in your manage webpage. To see the destination of your trip, please click on the address. The location will be shown on Google Map. Once users see the trip you want to take, you can contact the riders using the email riders offered.

(6)	This website is total free. Please enjoy our service!

How to setup this WEB:

We developed our website on Python 3.7.6. Please check your python version.

(1) First we have to install some packages.

(2) In your terminal please type: pip install django

(3) In your terminal please type: pip install PyMySQL

(4) In your terminal please type: cd desktop

(5) In your terminal please type: cd JHUstudentRide_Final_Project-WEB--master 2

(6) In your terminal please type: cd Final

(7) In your terminal please type: cd carpool

(8) Then, type "python manage.py runserver" to run the surver

(9) Last step type “http://127.0.0.1:8000/index/”  in your browser. Then you can run our WEB

References:

(1)	Django setup tutorial:
https://www.youtube.com/watch?v=Ev5xgwndmfc&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&index=9&fbclid=IwAR1YVXh1dvWRsezzCOnzagyPyHz9AmEwSEicWT57ASo8l3XDfx5bM5oIXo4

(2)	Creating homepage, APP and some often used HTML codes:
https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Home_page?fbclid=IwAR1_aRgbBwWElcpWX64zZdFKd77Y2PeFcsoOhczUAVy4ZxVgVyrqDj_ZEKM

(3)	Bootscrape HTML for formatting our homepage:
https://getbootstrap.com/

(4)	Setup user account and password: https://www.cnblogs.com/derek1184405959/p/8567522.html?fbclid=IwAR0STX3BbvP5cfl1mKFWMh-t4U6KffrJYsqsQ3Q27bb6RNT15G5N8EuvKbk

(5)	Tutorial for styling sidebar and templates:

https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&fbclid=IwAR20fQv82b7qOB6OzrUdULnJFKn7I_M4dm7MjOV-MztAdJbP-jUufOIaBxc

(6)	Codes for setting up tables, CSS, hyperlink, plug images and styling:
https://www.w3schools.com/html/

(7)	How to setup MySQL database:
https://techwithtim.net/tutorials/django/user-registration/

(8)	Uber, Lyft, Moqi mobile carshare app in Appstore
