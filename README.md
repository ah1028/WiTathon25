# WiTathon25 - Dopamine Menu

## Using Git
In order:
```
git pull
git add .
git commit -m "add message"
git push
```

## Development
Look at StartingPoint for a basic idea, all development and running the server should be done from Development folder

### Database 
![image](https://github.com/user-attachments/assets/37de9eaf-571a-465b-be17-f9b61f087e9e)

UI - Canva
https://www.canva.com/design/DAGhJ7_Te4s/VGk1q5nxcIjKBAy6eTUwKw/edit?utm_content=DAGhJ7_Te4s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Server
Run the command in the terminal to start the local webserver
```py server.py```
Then go to http://localhost:8000/ to view the webpage

## Using Flask
Navigate to the Combining directory in terminal, then run:
```
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```
Hopefully, you will then be able to run
```
py -m flask --app dopamine_menu run
```
And then follow the link in the terminal to the hosted website

Once finished with all work the virtual environment can be deactived by typing ```deactivate``` in the terminal