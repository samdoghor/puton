# MBS

MBS is a sports betting app that uses the Martingale system with smart algorithms to adjust bet amounts, customizable limits, win/loss thresholds, detailed analytics, and advanced security features. It improves the traditional Martingale system for fewer losses and increased winning streaks.

## Installation

To get started with the app, clone this repository and follow the steps below.

- Duplicate the `example.env` file and rename it to `.env.` Fill in the appropriate information in the .env file.

- Create a virtual environment and activate it:

```bash Copy code
virtualenv env
source env/bin/activate
```

- Install dependencies using pipenv:

```bash Copy code
pipenv install
```

- Expose the Flask app by running the following command:

```bash Copy code
export FLASK_APP=src/server.py
```

- On Mac, use the following command instead:

```bash Copy code
set FLASK_APP=src/server.py
```

- To enable auto-restart when changes are detected, set debug to true:

```bash Copy code
export FLASK_DEBUG=True
```

On Mac, use the following command instead:

```bash Copy code
set FLASK_DEBUG=True
```

- Create necessary tables in the database by running:

```bash Copy code
flask db upgrade
```

- Finally, run the app:

```bash Copy code
python src/server.py
```

## Data source

The statistics, fixtures, and other data used by MBS are obtained from the API-FOOTBALL platform [https://www.api-football.com/](https://www.api-football.com/). This API provides up-to-date information on a wide range of soccer leagues and matches from around the world.

To use the API in your own projects, you will need to sign up for an API key on the API-FOOTBALL website. Once you have an API key, you can set it in the `.env` file under the `API-FOOTBALL-KEY` variable.

## Contributing

See the [CONTRIBUTING](CONTRIBUTING.md) file for details on how to contribute.

## Contact

To contact me, email talkto@samdoghor.com
