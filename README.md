# Flowers Classification
Flowers Classification using Deep Learning - Udacity Pytorch Challenge

The challenge was to build and train a Neural Network that can classify 102 species of flowers.

The training was done on [this Kaggle kernel](https://www.kaggle.com/youben/flowers-classification-udacity-pytorch-challenge), this repo only contain an app that provide a RESTful API for users to predict flower species from pictures using that trained neural network.

![Image of Flowers](/imgs/Flowers.png)

### How to use it?
First, you need to make sure that there is an API available before using the CLI utility (which-flower.py). At the time of writing this, the API was hosted on 130.211.108.207

Then you need to setup the new IP (or hopefully a domain name) of the API if it has changed by replacing the API_URL variable

The last step is to run it:
```
$ ./which-flower.py globe_flower.png
[+] This flower is a globe-flower

```

###### Note
This is just an example utility


### Running the server app
The server app is the one responsible of all the computations needed to guess which flower is in that image, it's running a trained neural network (a modified [densenet121](https://pytorch.org/docs/0.3.0/torchvision/models.html#id5) network)

In order to run the server app (which is under the server directory), you have two options:

- #### The easy way using Docker
  You will just need to install [Docker](https://docs.docker.com/install/)

  Then run the following command inside the server dir
  ```
  $ docker build -t flower-pred .
  $ docker run -d -p 8080:80 flower-pred
  ```
  The first command will build the docker image and name it 'flower-pred'

  The second command will run a container of the previously created image, this container will be listening on the port 8080, feel free to change that port to have your API listen on another port.

- #### The second option
  Under the server directory, run the following command
  ```
  $ pip3 install -r requirements.txt
  $ python3 app.py
  ```
  It's seems like this one is easier, right? A French saying tells: "les apparences sont souvent trompeuses"
