
1. Create a virtual enviroment(env) and install all packages that will be needed. Make sure you are in "Attendance_Tracking_System_Using_Computer_Vision"
   -> python -m venv env

2. Activate your virtual enviroment
  On Linux
  -> source env/bin/activate 
  On Windows
  -> env\Scripts\activate
  On windows using git bash
  ->source env/Scripts/activate

3. Then now can install Django
  -> pip install Django

 4.Use the requirement.txt file to install those packages
  -> pip freeze > requirements.txt

5. Create all your models with the following commandes
  -> python manage.py makemigrations

6. Initialise your and create your data base
  -> python manage.py migrate

7. Launch the Django app 
  -> python manage.py runserver

8. Copy the ip adresse and paste it in the link description  

9.Navigate through the app by clicking on the desire button corresponding with what you wish to do.

NB : Register, Login, Logout buttons are note yet functional, they automatically redirect to the home page 

    
                                            