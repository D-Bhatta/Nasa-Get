# Result of the selected API page

- If no API key, redirect to home page
- Display the result of the particular API
- Take 3 API from NASA to test
- Compute the API result
- Return the API result
- Display the result

## Main tasks

- Create results view: render `api_result.html` page with selected api result as context
- Create urls with path as `<int:id>/`
- Create `api_result.html` template

## Create query functions

- Create a file `apis.py`
- Create a class to query API: class `Nasa`
- Create api query functions for each api in class `Nasa`
- Update module docstrings
- Create class docstrings
- Create function docstrings

## Create context builder class/funtions

- Create an `ContextBuilder` class
- It will take API `result` and `name` as parameters and return a context dictionary using a method
- For each api, create a method to build a `context` dictionary.
- Return context dict in method
- Add a context builder for `APOD`
- Add a context builder for `EPIC`
- Get key from `UserAPIs` model
- Add a context builder for `MRP`
- Add a context builder for `DONKI`
- Add module level docstrings
- Add class docstrings
- Add method docstrings


## Create results view: render `api_result.html` page with selected api result as context

- Get api key from `APIInfo` model
- If it is null, redirect to homepage
- query id,
- query api,
- Use `ContextBuilder` class: create `context`,
- render `api_result.html`

## Create urls with path as `<int:id>/`

- Create urls with path as `<int:id>/`

## Create `api_result.html` template

- Use code from ridge css
- Test
- Replace stuff with `resource` parameters passed to `context` dictionary
- Test
- Refactor as needed
