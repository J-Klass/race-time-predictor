# Race Time Predictor

## Development

### Requirements

Make sure you have Python, Pipenv, Node.js, and Yarn installed.


### Installation

1. Clone the repository: `git clone [repo-url]`
2. Install all dependencies: `pipenv install --dev` and `yarn install`
3. Set up the pre-commit hooks: `pipenv run init`


### Configuration

Obtain your [credentials for accessing the Strava API](https://developers.strava.com). Rename the [`.env.example`](.env.example) file to `.env.development` and fill in your Strava app credentials:

```
VUE_APP_CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

The Flask server now has access to both environment variables; the Vue client only to the client ID (hence the `VIEW_APP_` prefix). 


### Start

You can now run the app:

1. Execute `yarn start` to bundle the Vue app
2. Run `FLASK_ENV=development pipenv run start` to start the back end and serve the Vue app


## Credits

* Runner icon in logo: [Freepik](https://www.flaticon.com/authors/freepik)
* Loading spinner: [SpinKit](http://tobiasahlin.com/spinkit/)
* Color icons on start page: [Icons8 Flat Color Icons](https://github.com/icons8/flat-color-icons)
* Error and terminal icons: [Boxicons](https://boxicons.com)
