# Nasa-Get

A Django app that displays results from querying NASA's public APIs.

## Table of Contents

- [Nasa-Get](#nasa-get)
  - [Table of Contents](#table-of-contents)
  - [How to use](#how-to-use)
  - [Project Status](#project-status)
  - [Additional Information](#additional-information)
    - [Screenshots](#screenshots)
      - [Main App screen](#main-app-screen)
      - [API index screen](#api-index-screen)
      - [API results screen](#api-results-screen)
    - [Links](#links)
    - [Notes](#notes)

## How to use

- Click on the [app link](https://d5625.pythonanywhere.com/home/)
- Get a new API key from NASA and enter it there
- Click on any of the APIs available

The results along with useful information about the API will be displayed.

## Project Status

Project is currently under active development.

## Additional Information

### Screenshots

#### Main App screen

![Homepage](/images/Screenshot%202020-10-23%20095504.png)

#### API index screen

![API index screen](/images/Screenshot%202020-10-23%20095608.png)

#### API results screen

![API results screen](/images/Screenshot%202020-10-23%20100832.png)

### Links

- [Link to app](https://d5625.pythonanywhere.com/home/)

### Notes

- I created a layered architecture of python classes to query NASA's Open APIs and extract useful information from it
- I fine-tuned architecture design such that only 2 functions and a database entry need to be to add a new API to the app
- I developed a view to accept user API key and securely store them in a database
- I created a page to display API information automatically in a responsive card view
