# *🦄 FUEL*
FUEL is a malware written mainly in Python and a bit in C++.</br>
The name comes by combining the name of all the files: Format-22, Unusable-2, Eradication-Typhoon, Lonely-12.</br>
All of these names are inspired from fighter jets, here are all of them:
```
Lockheed Martin-Boeing F-22
Lockheed U-2
Eurofighter Typhoon
Lockheed YF-12
```

NOTE! For important reasons, FUEL is not configured to work as a ``.exe`` which means it can't be used by anyone, this can tho be done by anybody with a very little bit of Python knowledge.

# **☣️ Descriptions**
Here's a breaf description of every FUEL part.

## **⛔ Format-22**
As said before, FUEL is divided in 4 parts, each one serve e very important purpose.</br>
Format-22 is the main FUEL file, it's main purpose is to go through every PC file (scanning C: drive) and check if it is a ``.exe`` file, then overwrites them, making them unusable.</br>
After going through every it check is the user opens a new file, if he does, Format-22 close and deletes the file.</br>
It also serves as a ``file watcher`` it's used for checking if ``Lonely-12`` is running.

Format-22 is also one of the only udetectable files.

## **⛔ Unusable-2**
Unusable-2 is a ``key logger`` which means it is a stealth malware that stays in the computer waiting for the user to type his passwords and important informations.</br>
The way it works is by taking every key the user inputs and adding it to a string, and then after a certain time (that you can modify ``self.time_interval``) it sends an email to you.</br>
For that you need to insert your ``email`` and ``password`` inside the keylogger object creation.

Unusable-22 gets created once ``Format-22`` gets opened and it gets opened every time Windows starts.

NOTE! Unusable-22 is the ``ONLY`` part of FUEL that gets detected by Windows.

## **⛔ Eradicator-Typhoon**
Eradicator-Typhonn, is used for causing a ``BSOD`` (Blue Screen Of Death) and delete every file on the Desktop.</br>
Other than that, it locks the cursor in the middle of the screen.

It gets created when either ``Format-22`` or ``Lonely-12`` get closed.

## **⛔ Lonely-12**
The only Lonely-12's purpose is to check if ``Format-22`` is still running, in fact it is a process/file watcher.</br>
Lonely-12 is very useful, since it and ``Format-22`` form a loop in which none of them can be closed, because it will open ``Eradicator-Typhoon``.

It gets created when ``Format-22`` is opened.

# *⚠️ IMPORTANT ⚠️*
DON'T USE THIS AGAINST ANYONE, THIS IS VERY DANGEROUS AND FOR DEMONSTRATIONAL PURPOSES ONLY!

