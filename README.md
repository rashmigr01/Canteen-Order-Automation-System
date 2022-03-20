# Canteen-Order-Automation-System
Aim: To digitalise and automate the canteen order system
<br/>Features: 
- Students can open or terminate a monthly account using their roll nos, and all their orders are listed under their account. 
- A monthly bill is generated and emailed to the student’s iitk email id on the last day of every month.
- Regular orders are automated by digitalising the canteen’s menu and an e-bill after every order by a non-monthly customer.
- Ordering from the canteen can also be done remotely by accessing the website. The order queue is made visible to facilitate the picking up of the order and avoid crowding in the canteen.
- Digital payment details are made available in the monthly bill, and the regular order interface for smooth transactions.

## Project Setup
- Clone The repository 
```bash
  git clone https://github.com/rashmigr01/Canteen-Order-Automation-System.git
```
- Create virtual environment 
```bash
  python -m venv env
```
- Activate the Virtual Environment 
```bash
  .\env\Scripts\Activate.ps1
```
- Install all the dependencies 
```bash
  pip install requirements.txt
```
- Navigate to the folder containing the file `manage.py`
- Start the server 
```bash
  python manage.py runserver
```
