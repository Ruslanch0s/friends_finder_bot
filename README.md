# Aiogram bot template
> Outline a brief description of your project.

## Table of Contents
* [Антифлуд](#)

## Антифлуд
###Отдельно для хендлера
1) utils.antiflood import rate_limit
2) @rate_limit(`seconds`, `command`)
   - `seconds` is required
###Для всех хендлеров
1) middlewares/antiflood... > 2 (2 is seconds)



## Занятые порты на MacOC
1) sudo lsof -i :5432 
2) kill -id-


## Отправка фото/документов
      root_path = config.tg_bot.root_path
      path_to_download = path.joinpath("tgbot", "pictures", "instruction.png")  # preview
      
      with open(path_to_download, 'rb') as photo:
         await callback.bot.send_photo(callback.message.chat.id, photo)

## Миграции
### создать автоматическую миграцию
1)my-project/db/alembic $ alembic revision --autogenerate -m "first migrate"  
### применить последнюю миграцию
2)my-project/db/alembic $ alembic upgrade head  

# RUN
0) настроить .env
1) запустить бд в докере
2) $ngrok http 3001
3) $python main.py

## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
