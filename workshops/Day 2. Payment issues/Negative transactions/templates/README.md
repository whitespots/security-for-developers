# Improper Input Validation  

This lab shows how an unvalidated variable can damage your company.

## Core idea
You have first account to the bank **`jdoe:1234`** and you have another account **`bsmith:1234`**. You should transfer all money to first account with it's session.

## Build

```commandline
docker build -t negative_transaction_lab . 
```

## Run

```commandline
docker run -it --rm -p 80:5000 negative_transaction_lab
```

## Start hacking

http://127.0.0.1/