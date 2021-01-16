# HHLyon #5

# Aim of the project
This POC project was created during the Hacking Health Lyon #5 in January 2021.
The aim of our group was to reduce the patient's medical errance.
The final goal of this project is to build a web app that medical professionals can consult.
It searches the database of rare deseases, and finds the illnesses with the corresponding symptoms.
To be the more precise, the web app could ask questions to the prefessional to reduce the number of results.

# working POC
This POC is working via Django framework. It searches in the database the deseases that match the symptomes.
It then displays the probable rare deseases, and also supplies the reference of the sites where the patient
can seek help.

# To start your virtual environment
mkdir venv; cd venv; python3 -m venv venv;

# To enter virtual env
source bin/activate

# To install all dependencies
pip3 install -r requirements.txt

# To quit virtualenv
deactivate

###

# To start project
cd tilt; python3 manage.py runserver