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

## Create results view: render `api_result.html` page with selected api result as context

- Get api key from `APIInfo` model
- If it is null, redirect to homepage
- query id,
- get api link,
- query api,
- see what kind of resource it sends,
- create object `resource` with resource type and resource  link,
- create context,
- render `api_result.html`

## Create urls with path as `<int:id>/`

- Create urls with path as `<int:id>/`

## Create `api_result.html` template

- Use code from ridge css
- Test
- Replace stuff with `resource` parameters passed to `context` dictionary
- Test
- Refactor as needed
