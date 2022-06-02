#!/usr/bin/zsh
sassfile=/home/ivan/Документы/PROJECT/OPS2/app/static/main.scss
cssfile=/home/ivan/Документы/PROJECT/OPS2/app/static/main.css
#pipenv shell
flask run&
sass --watch "$sassfile" "$cssfile"&
