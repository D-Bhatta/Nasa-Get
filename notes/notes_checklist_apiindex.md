# API Index page

- Cards are displayed that show all the APIs that a user can access
- Each card has a picture, a heading corresponding to the API name, and a link to selected API page
- The app should show stuff in cards
- Each card should have a picture, a heading, and a link to a page
- The app should take the data to populate the cards from a data base
- Each card will open onto a new page with a particular id

## Main tasks

- Create a new app called `view_api`
- Create models to store info about APIs
- Create view that renders each api in database as a card.
- Register urls for the choose api view
- Create a template page to render apis as cards

## Create models to store info about APIs

- Create a model called `APIInfo`
- Store API name, link, a picture of API result
- Make migrations
- Migrate
- Test and refactor in local
- Choose 4 API, one text, three image/video
- Register models in `admin.py`
- Create 4 `APIInfo` instances
- Refactor as needed

## Create view that renders each api in database as a card

- Get all `APIInfo` instances
- Create `context` dictionary with them
- Render the `api_index.html` page
- Refactor as needed

## Register urls for the choose api view

- Change the dummy page to **API Index page**.
- Register url as `view_api/`
- Create the `templates/api_index.html` file
- Refactor as needed

## Create a template page to render apis as cards

- Use code from ridge css
- Test
- Replace stuff with `APIInfo` instances passed to `context` dictionary
- Test
- Refactor as needed
