# App Features

1. Show a homepage that explains the app
2. Take API key from user
3. Show a page where they can select what API they want to use it for: Choose your API page
4. Show the result of the selected API

## Homepage

- Show a homepage with text about the form
- Display a form input for users to enter their API key
- Store API key for user after encrypting it
- Redirect to API Index page

## API Index page

- Cards are displayed that show all the APIs that a user can access
- Each card has a picture, a heading corresponding to the API name, and a link to selected API page
- The app should show stuff in cards
- Each card should have a picture, a heading, and a link to a page
- The app should take the data to populate the cards from a data base
- Each card will open onto a new page with a particular id

## Result of the selected API page

- If no API key, redirect to home page
- Display the result of the particular API
- Take 3 API from NASA to test
- Compute the API result
- Return the API result
- Display the result

## Future Enhancements

### Non-persistence of data

- Remove all API keys from memory on start to prevent misuse. I don't want to hold onto the data.

### Get the results of API preemptively to save time

- Get the results of all APIs preemptively at app start using threads, to save rendering time

### Authenticate using a token

- Send a token and authenticate using it

### Token and encryption expiry

- Tokens and encrypted keys expire after a while

### Refactor `Nasa` class to add inheritance

- Create parent class for `Nasa` class to inherit from

### Add  other APIs

- Add other APIs from Nasa

### Add a public mission and API to README.md

- Add a mission for the **why**
- Add a public API for usage

## Design: USer stories

**Homepage** will be a singular app. It will take data from user, and store it in a model. It will return something to the user that can be used to authenticate them. It will redirect to the **Choose your API page**.

**Choose your API page** and **Result of the selected API page** will be in another app. They will follow the pattern of Card - -> Item. All possible APIs will be shown to the user as cards. When the user clicks on a card, it will compute an api result and redirect them to a page with the result from the api displayed.

If it is an image, it will display an image, if it is a video, it will embed that video. If it is text, it will show text.
