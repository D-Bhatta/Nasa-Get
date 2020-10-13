# Homepage

- Show a homepage with text about the form
- Display a form input for users to enter their API key
- Store API key for user
- Redirect to API Index page

## Main tasks

- Modify `base.html` to make it mission ready
- Create a short instruction paragraph below the heading
- Create a form with an input field and a button
- Create a model to store user API
- Create a view that is used to save form data and model and redirect to API Index page
- Redirect to API Index page
- Refactor as needed

## Modify `base.html` to make it mission ready

- Replace current css with Ridge css

## Create a short instruction paragraph below the heading

- Create heading
- Add instruction about what to do with the input field
- Add some sample text there first
- Change it to proper instructions
- Refactor as needed

## Create a model to store user API

- Create a model that can store user API keys
- Create model with name `UserAPIs` with
- Create a `api_key` field as tex
- Make migrations
- Migrate
- Try saving 2 random inputs there
- Refactor as needed

## Create a view that is used to save form data and model and redirect to API Index page

- Create a view that saves form data to model

### Create forms

- Create a `homepage/forms.py` from that saves to model
- Define a variable `api_key` that is a textFeild and define `attrs` with name, id  as `api_input`, placeholder as `API Key`, and type as `password`
- Refactor as needed

### Define views and urls

- Write a function to encrypt API key in utils
- Create a view function that validates form data, encrypts cleaned form data and stores it into model, and renders the **API Index page**.
- Create a dummy page and link to it.
- Change the dummy page to **API Index page**.
- In `urls.py` create link at `key`
- Refactor as needed

## Create a form with an input field and a button

- Add a form element with an using ridge css and django templates, with form directing to the `addkey` link
- Center the stuff
- Add a button as submit
- Refactor as needed
