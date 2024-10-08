# SubProcessBot    

**SubProcessBot** - это бот на Python, использующий библиотеку `subprocess` для управления сервером, на котром хостится бот

## Требования
- Учетная запись Telegram с полученными API-ключами (API_ID, API_HASH)
- Установленные зависимости, указанные в файле requirements.txt 

## Установка и настройка
- Склонируйте репозиторий
- Перед запуском бота создайте папку внутри репозитория с названием `secret_data`, в неё создайте файл `config.ini` с ключами и токенами
- config.ini должен иметь следующий вид:
```
[Telegram]
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
creator_id = CREATOR_ID
```
- где api_id и api_hash - ваши Telegram API ключи(более подробная информация в интернете), bot_token - ваш идентификационный токен бота, creator_id - ваш id(не юзернейм) в Telegram
- установить зависмости консольной командой:
```
pip install -r requirements.txt
```

## Особенности использования
- Основной функционал бота заключается в управлении сервером, на котором хостится бот
- Бот позволяет добавлять, удалять и запускать команды на сервере


**Бот находится на стадии альфа-теста, поэтому баги и ошибки вполне вероятны и ожидаемы, в случае нахождения такого просьба скинуть скрины переписки с ботом в Telegram - <a href="https://t.me/kolo_id">@kolo_id<a>**


**Примечание:** Использование данного бота может быть ограничено правилами и политикой Telegram. Пожалуйста, убедитесь, что соблюдаете все правила Telegram при использовании этого бота.

