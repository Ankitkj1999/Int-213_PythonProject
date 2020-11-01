# Int-213_PythonProject
Int 213 College Python Project. Capstone Supervisor Allocation Portal made using python tkinter. 



![alt_text](https://cdn.freelogovectors.net/wp-content/uploads/2019/02/lpu-logo-lovely_professional_university.png "image_tooltip")


**School of Computer Science and Engineering**


    **Lovely Professional University**
    **Phagwara, Punjab.**
    ** INT  213**

**Capstone Supervisor Allocation Portal for LPU Students Using Python**

**  Submitted To Ishan Kumar (Faculty INT 231) On 2/Nov/2020**


<table>
  <tr>
   <td><strong>Submitted By</strong>
   </td>
   <td><strong>Roll Number</strong>
   </td>
   <td><strong>Reg. Number</strong>
   </td>
   <td><strong>GitHub</strong>
   </td>
  </tr>
  <tr>
   <td>Abhays Vengaldas
   </td>
   <td>32
   </td>
   <td>11914099
   </td>
   <td>Abhayavengaldas
   </td>
  </tr>
  <tr>
   <td>Yashwant Singh
   </td>
   <td>21
   </td>
   <td>11902903
   </td>
   <td>viru-viru
   </td>
  </tr>
  <tr>
   <td>Ankit Kumar
   </td>
   <td>12
   </td>
   <td>       11902813
   </td>
   <td>Ankitkj1999
   </td>
  </tr>
</table>


**Index**



1.  Title…………………………………………… 1
2.  Index…………………………………………..  2
3.  Acknowledgement………………………...…..  3
4. Summary……………………………………….  4
5. Tabel Of Figures………………………………..  4
6.  Introduction…………………………………….  5
7.  Basic Module Division…………………………  6
8.  Reference………………………………………  11
9.  Result…………………………………………..  11

[TOC]



**Acknowledgement**

I _Ankit Kumar_ and my team-mates _Abhaya _and _Yashwant _have taken efforts to complete this project. However, it would not have been possible without the kind support and help of my professor _Ishan Kumar _(Faculty INT-213).

 I would like to extend my sincere thanks to all those who helped regarding the project & also for their support in completing the project. This project helped me and my team members to hone our Python programming skills and learnt how we can use programming in real life. There were a lot of online resources that I referred to while preparing the project.

**        Summary**

**    **

The project titled ‘**Capstone supervisor allocation portal for LPU students using python**’ is a GUI approach to create a software that helps in allocating supervisors to various registered students for their capstone project. 

**Tabel Of Figures**


<table>
  <tr>
   <td>Fig 1
   </td>
   <td>Opening Student’s Window
   </td>
  </tr>
  <tr>
   <td>Fig 2
   </td>
   <td>Student’s Login Window
   </td>
  </tr>
  <tr>
   <td>Fig 3
   </td>
   <td>Student’s New Registeration
   </td>
  </tr>
  <tr>
   <td>Fig 4
   </td>
   <td>Request For Supervisor
   </td>
  </tr>
  <tr>
   <td>Fig 5
   </td>
   <td>Supervisor’s Opening Window
   </td>
  </tr>
  <tr>
   <td>Fig 6
   </td>
   <td>Supervisor’s Login Window
   </td>
  </tr>
  <tr>
   <td>Fig 7
   </td>
   <td>Supervisor’s New Registration
   </td>
  </tr>
  <tr>
   <td>Fig 8
   </td>
   <td>Supervisor’s Home Page
   </td>
  </tr>
</table>


**INTRODUCTION**

In this project we have made a **Capstone Supervisor Allocation Portal**, the technology that we have used is solely **Python Tkinter**._ Tkinter_ is the standard GUI (Graphical User Interface) library for _Python_. _Python _when combined with _Tkinter _provides a fast and easy way to create GUI applications. _Tkinter _provides a powerful object-oriented interface to the Tk GUI toolkit. This project has been divided into two segments: - 



1. **Student Segment **which helps new students register for the supervisor allocation and pre-registered students to login and check the name of their supervisor and their basic details. 
2. **Supervisor Segment **which helps new supervisors to register for his availability and pre-registered supervisors to check the name of allocated students under them and their basic details.

**BASIC MODULE DIVISION**

**Opening Student Window**






![alt_text](https://i.ibb.co/M5DSTMj/home.jpg"image_tooltip")
  Fig 1

This is the first window which opens for the students. It hs three buttons the first one is _login _button, when clicked it opens the login window. The second button is the _New User_ button, when this button is clicked it opens a window for the new registrations. The third is the _Request For Supervisor _button, this takes the student to the _login _window and when the student is logged in the student is taken to the form window which needs to be filled to request a supervisor.

**Student Login Window**



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](https://i.ibb.co/892RbM8/login.jpg "image_tooltip")


Fig 2

Now, this is the _login_ window where the student is taking is the _login _button is pressed. The _login _form requires the _Username _and _Password_ of the already registered student. 

**New Student’s Registration**

![alt_text](https://i.ibb.co/hK6qshf/regform.jpg "image_tooltip")


Fig 3

This is the window which opens when the student presses the _New User_ button in the opening window. This form contains eight fields, so when a student fill this and press the _Registered_ button he or she gets registered and the data is stored in the database

.

**Request For Supervisor**


![alt_text](https://i.ibb.co/dgymfZy/jb.jpg "image_tooltip")


Fig 4

This is the window where the student can request the supervisor. This window appears when the student presses the _Request For Supervisor _button and logins through the _login _form. To request the supervisor the student needs to fill all the needed credentials along with a message regarding the project. Now all the data would be available to the supervisor to see through.

So all these four windows concluded the student segment of the project.

**Supervisor’s Opening Window**



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.jpg "image_tooltip")


Fig 5

This is the opening window for a supervisor. It consists of two buttons the first on is _Login _button which takes the user to login window when presses. And the second button is _New User_ button

which takes the user to the registration window for a new supervisor.

**Supervisor’s Login Window**




![alt_text](https://i.ibb.co/892RbM8/login.jpg "image_tooltip")


Fig 6

This is the _ Login_ window which opens when a supervisor or user clicks the login button. It is same as the login window for the students. An already registered uses need to fill in the _Username _and the _Password _credentials to login.

**Supervisor’s Registration Form**




![alt_text](https://i.ibb.co/hK6qshf/regform.jpg "image_tooltip")


Fig 7

This window is for new Supervisor’s registeration. It opens whenever a user clicks the _New User _button in the opening window. Similar to the Students registration the Supervisor needs to fill all the details and when the register button is pressed the data gets stored in the database.

**Supervisor Home Page**



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.jpg "image_tooltip")


Fig 8

The above window is what appears in frot of the supervisor whenever he or she logins. In this tab the supervisor would be able to see the requests from the students along with his name, UID and a logout button.

This is the basic outline of the project. There will be more modules in the project if needed. These modules will build the basic infrastructure of the projec

**Reference**



1. [GeeksforGeeks.org](https://www.geeksforgeeks.org/)
2. [StackOverflow](https://stackoverflow.com/)
3. [TutorialsPoint](https://www.tutorialspoint.com/index.htm)

**Result**

Conbining all the information mentioned above and some efforts we were able to complete our project. The GitHub link to the project is _[here](https://github.com/Ankitkj1999/Int-213_PythonProject)_.
