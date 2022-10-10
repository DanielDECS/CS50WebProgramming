# Music Player

This is a Music Player web application built using React and Django, it is a way for a group of people to control the music that's being played on Spotify application in unity.

This was the Final Project  of HarvardX's CS50w course.

Full project specification here: https://cs50.harvard.edu/web/2020/projects/final/capstone/


## Distinctiveness and Complexity
The most distinctive features of the final project, compared to the four previous works, is the use of React as a frontend framework and the application's integration with the Spotify API which is also used for user authentication. Django is also configured to operate as an API, using the Django REST Framework. React Material UI component library was used and the grid components made the application responsive.

## Running the App

### Install Required Python Modules

```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

```bash 
cd "capstone"
```
Next run the django web server.
```bash
python manage.py runserver
```
### [Install Node.js](https://nodejs.org/en/)

### Install Node Modules

First cd into the ```frontend``` folder.
```bash
cd frontend
```
Next install all dependicies.
```bash
npm i
```

### Compile the Frontend

Run the production compile script
```bash
npm run build
```
or for development:
```bash
npm run dev
```
### [Spotify API Reference](https://developer.spotify.com/documentation/general/guides/)


## Project Files
```
music
│   README.md                       # You are here
│   requirements.txt                # Project requirements
│   ...
└───api                             # Backend API directory
│   │ 
│   │  models.py                    # Project models
│   │  serializers.py               # Project serializer
│   │  urls.py                      # Define routes for querying project API
│   │  views.py                     # Handle req/res to api
│   │  ...
│
└───frontend                        # Frontend directory
│   │
│   │  babel.config.json            # Babel configurations
│   │  package.json                 # App configurations and dependencies
│   │  urls.py                      # Define routes for frontend
│   │  views.py                     # Handle req/res to frontend
│   │  webpack.config               # Webpack configurations
│   │  ...
│   └───src                         # Frontend source code
│   │   │ 
│   │   │  index.js                 # Js entry point
│   │   │
│   │   └───components              # Directory for React components 
│   │       │
│   │       │  App.js               # React app main file
│   │       │  CreateRoomPage.js    # Create room page component
│   │       │  HomePage.js          # Home page component
│   │       │  MusicPlayer.js       # Music player component
│   │       │  Room.js              # Room page component
│   │       │  RoomJoinPage.js      # Room join page component
│   │       
│   └───static                      # Directory for static resources
│   │   │ 
│   │   └───css                     # Directory for stylesheets 
│   │   │   │
│   │   │   │  index.css            # App stylesheets
│   │   │   
│   │   └───frontend                # Directory for main.js file
│   │   │   ...    
│   │   │
│   │   └───images                  # Directory for images
│   │       ... 
│   │
│   └───templates
│       │ 
│       └───frontend                # Directory for entry point
│           │
│           │  index.html           # App entry point
│     
└───music                           # Main project directory
│   │ 
│   │  settings.py                  # Project settings
│   │  urls.py                      # Define app main routes
│   │  ...
│
└───spotify                         # Spotify API directory
    │
    │  credentials.py               # Spotyfy required credentials
    │  models.py                    # Spotyfy API models
    │  urls.py                      # Define routes for spotify API
    │  util.py                      # Useful functions used
    │  views.py                     # Handle req/res to spotify
    │  ...

```