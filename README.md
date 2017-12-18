# initiator
html crawler service using python django web framework

## Description
This is a simple API Service that crawl the website and return its html

## Dependencies
* [Django web framework](https://www.djangoproject.com/) - The web framework used
* memcached
* [cfscrape](https://github.com/Anorov/cloudflare-scrape) - the html scrapper used
* [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - the html parser

## Instalation Guide
This installation guide assumed that python 3.5 and pip3 is already installed.
First install all the dependencies

```
sudo pip3 install Django
sudo pip3 install cfscrape
sudo pip3 install bs4
```
Next, clone this repository

```
git clone https://github.com/hobertho/initiator.git
```
To run the server, first enter the initiator project directory, and then run in terminal:

```
python3 manage.py runserver 0.0.0.0:8080
```

## How To Use
There's only one API route for the moment. In order to obtain the html text from website, use:

```
[GET] http://localhost:8080/scrapper/
```
Parameters:

* link -> required, example (http://google.com)

The response format:

```
{
  "code": 200,
  "head_message": "<head>...</head>",
  "body_message": "<body>...</body>"
}
```
* the head and the body is separated because of maximum string length limitation
