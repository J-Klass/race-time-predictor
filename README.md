# Strava Time Predictor

## Development

### Requirements

Make sure you have Python, Pipenv, Node.js, and Yarn installed.


### Installation

1. Clone the repository: `git clone [repo-url]`
2. Install all dependencies: `pipenv install --dev` and `yarn install`
3. Set up the pre-commit hooks: `pipenv run init`


### Configuration

Obtain your [credentials for accessing the Strava API](https://developers.strava.com). Add them to a `config.json` file in the project's root directory:

```json
{
  "clientId": "...",
  "clientSecret": "..."
}
```


### Start

You can now run the app:

1. Execute `yarn start` to bundle the Vue app
2. Run `FLASK_ENV=development pipenv run start` to start the back end and serve the Vue app
