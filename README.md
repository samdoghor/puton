# MBS

MBS is a sports betting app that uses the Martingale system with smart algorithms to adjust bet amounts, customizable limits, win/loss thresholds, detailed analytics, and advanced security features. It improves the traditional Martingale system for fewer losses and increased winning streaks. [Read More](MARTINGALE.MD)

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

- Create a database with necessary tables by running:

```bash Copy code
flask db upgrade
```

- Finally, run the app:

```bash Copy code
python src/server.py
```

### [Click here to see how to use app](APP.md)

## Data source

Unavailable for now

## Contributing

See the [CONTRIBUTING](CONTRIBUTING.md) file for details on how to contribute.

## Contact

To contact me, email [talkto@samdoghor.com](mailto:talkto@samdoghor.com)

## Disclaimer

While the Martingale betting system may be a popular strategy, it is crucial to approach its usage with responsibility and caution. The following disclaimer highlights important considerations for gamblers:

- Responsible Gambling: Gambling should always be approached responsibly. It is essential to understand the potential risks associated with any betting system, including the Martingale system. Exercise self-control and set personal limits on your gambling activities, including your bankroll and the amount of time spent gambling.

- Age and Legal Restrictions: Before engaging in any form of gambling, ensure that you are of legal age as stipulated by the laws of your country or jurisdiction. It is crucial to abide by the regulations and restrictions set forth by your local authorities and gambling establishments.

- Personal Financial Situation: The Martingale system, like any betting strategy, carries financial risks. It is crucial to assess your personal financial situation and determine an appropriate bankroll for your gambling activities. Never wager more than you can afford to lose, as there is no guarantee of winning with the Martingale system or any other betting strategy.

- Losses and Risk: While the Martingale system can offer short-term wins, it is vital to understand that no betting system can guarantee consistent profits. A losing streak can result in substantial financial losses, especially if the required bet sizes exceed your bankroll or the table limits imposed by the casino. It is crucial to approach gambling with a realistic mindset, acknowledging the possibility of losses.

- No Liability: As the user of the Martingale system or any other betting strategy, you acknowledge that the outcomes of your gambling activities are solely your responsibility. No one can be held accountable or responsible for any losses incurred while using the Martingale system or any other betting strategy. It is essential to make informed decisions, exercise caution, and acknowledge the risks involved in gambling.
