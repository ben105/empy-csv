# Emporia Download Script

## Concept

Emporia has resources available behind a layer of authentication. Because of the complexity mocking user input into a Flutter app, and because of the lack of supported Emporia APIs, this script exists to do the majority of the leg work.

This package depends on other community packages to communicate with Amazon Web Service endpoints, perform cryptographic hashes and decryption, and to pull OAuth tokens from JWT responses.

In addition to the Python dependencies above, this package contains a Makefile to simplify the build/clean steps and installation commands required by the user.

## Instructions

These instructions assume you are running on a Mac, or at least have zsh installed.

### Step 1

Update the empy file with your credentials. At the moment, the `empy` file has the email/password lines left blank, and you will have to fill this in with the correct values. The lines currently look like this:

```
EMAIL=''
PASSWORD=''
```

### Step 2

Double-click on the `install` file, and this should pop open a terminal and run all the commands for you, no work required on your part.

### Step 3

Write the following AppleScript, which should end up calling this script. It would look like the following:

```
do shell script "/usr/local/bin/empy"
```

This will download a CSV file to your ~/Downloads folder. The CSV is titled with the current date and time to help distinguish it from subsequent downloads.
