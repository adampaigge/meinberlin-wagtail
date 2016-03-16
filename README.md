# CMS for Meinberlin Project

## Requires

*   python 3.x (+ virtualenv + pip)


## How to start

1.  clone repository
2.  `cd meinberlin_wagtail`
3.  create virtualenv (make sure to add virtualenv name to .gitignore)
4.  run `pip install -r requirements.txt`
5.  run `python manage.py migrate`
6.  run `python manage.py loaddata initial_content.json`
7.  run `python manage.py createsuperuser`
8.  run `python manage.py runserver`
9.  Browse to <http://localhost:8000/w/admin>

## run wagtail and adhocracy on same origin

Running adhocracy and wagtail on the same origin is required if you want to
have a tight integration, e.g.  show an adhocracy login in wagtail.  An example
nginx config is included. You also have to adjust the following settings in
your adhocracy frontend config:

    adhocracy.frontend.ws_url = ws://localhost/ws/
    adhocracy.frontend.rest_url = http://localhost/api/

## TODOs

-   write script to to automatically import processes from adhocracy
    (see unfinished branch feature-adh-pull)
-   build sass instead of just linking pre-build file
-   make home page more customizable (e.g. cover image)
