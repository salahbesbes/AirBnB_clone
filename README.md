# AirBnB_clone
<p align="center"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210217T160904Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=deb6ae0aa841f34ac6441ffcfaac9bb3e5ce65dce58fcdd73c87522f726d2b70" alt="AirBnb  logo"></p>

## Descreption:
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project . This the first part of it the console( command line interepteur)

## Installation
* Clone This Repo `git clone https://github.com/salahbesbes/AirBnB_clone.git`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Available Command:
* quit and EOF to exit the program
* help for every Command
* create 
* show
* destroy
* all
* update
* count

## Examples


## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Authors
* Ahmed Belhaj [Theemiss](https://github.com/Theemiss)
*  Mohamed Salah Besbes [salah_besbes](https://github.com/salahbesbes)

<p align="center"><img src="http://www.holbertonschool.com/holberton-logo.png" alt="Holberton School logo"></p>
