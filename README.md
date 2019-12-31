# korean-english-names

## Installation

1. Clone this repo:

    ```bash
    git clone https://github.com/...
    ```

    Then cd into it:

    ```bash
    cd korean-english-names
    ```

2. Create and activate a virtualenv:

    ```bash
    python3 -m virtualenv venv  (If this does not work, try: `virtualenv -p python3 venv`)
    . venv/bin/activate (`venv\Scripts\activate` for Windows)
    ```

3. Use pip to install all the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

<!-- 4. Reset the database to create tables.

    ```bash
    ./manage.py initdb
    ```

    If you get the error "TypeError: OAuthRemoteApp requires consumer key and secret", you need to set your OK_KEY and OK_SECRET environment variables. -->

1. Run the server:

    ```bash
    python3 server.py
    ```

2. Point your browser to http://localhost:5000