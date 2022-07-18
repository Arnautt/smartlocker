<!-- LOGO -->
<br />
<h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/Arnautt/smartlocker/logo.png" alt="Logo" width="140" height="110">


</h1>
  <p align="center">
    Python package to lock your computer smarter.
    <br />
  </p>
</p>

<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">How To Use it</a> 
</p>  

## :rocket: About The Project

This small Python package will allow you to lock and unlock your computer
in a smart way, using facial recognition.
It allows you to both automatically lock the screen when you leave your workstation,
as well as unlock the computer when you return.
Without ever typing anything on the keyboard.

> this is a citation


## :wrench: Installation

The first step is to clone the repository, by doing :

```bash
cd my/application/path
git clone lien/git/vers/le/depo
cd my-app-name
```

Then, install a virtual environment and all the necessary packages :


```bash
make build-env
```

You're now ready to use the application.

## :unlock: Usage


1. In order to do face recognition, you must pass to the algorithm some pictures of you, with as many angles as possible. 
Let us guide you by running the following script : 

```bash
make generate-data
```


2. Run the main script and enjoy !


```bash
make main
```

## :question: How does it work 

technologies, classes...

- tech : face_recognition, cv2, 
- optimization, une frame sur deux 
- classes
