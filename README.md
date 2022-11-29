# mastermind-api

Mastermind board game

## API

The interface provided by the service is a RESTfull API. The operations are as follows.

### GET /status

Indicate the service has started up correctly and is ready to accept requests.

Responses:

* **200 OK** When the service is ready to receive requests.

### POST /game

Create a new game with a code and max tries.

**Body** _required_ The code and max_tries of the game.

**Content Type** `application/json`

Sample:

```json
{
    "code": "RGBY",
    "max_tries": 10
}
```

Responses:

* **200 OK** When the game is created correctly
* **400 Bad Request** When there is a failure in the request format or the payload, the code is limited to 4 characters.

### POST /board/<game_id>

Add a new guess to a game.

**Body** _required_ The code / guess of the game.

**Content Type** `application/json`

Sample:

```json
{
    "guess": "RGBX"
}
```

Responses:

* **200 OK** When the guess is added correctly
* **400 Bad Request** When there is a failure in the request format, the payload, the game is already finished / guessed or there are no more tries.

### GET /board/<game_id>

Get the board of a game.

Sample Response:

```json
[
    {
        "black_pegs": 0,
        "guess": "RGBY",
        "white_pegs": 4
    },
    {
        "black_pegs": 0,
        "guess": "RGXX",
        "white_pegs": 2
    }
]
```

Responses:

* **200 OK** When the game exists. The results are ordered in descending order by date and time.
* **404 Not Found** When the game exists doesn't exist.

## Use of this project

There is a documented makefile to make your life easier (if you are using OSX or Linux).

In any case, if you use windows you can use the same docker commands that are in the makefile.

Use the following command to build the docker image:
```sh
make dockerize
```

And to start the service:
```sh
make run
```