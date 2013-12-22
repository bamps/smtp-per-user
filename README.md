smtp-per-user
=============
Модуль добавляет возможность выбрать пользователя, к которому
относятся конкретные настройки smtp сервера.
Возможно применять, когда сервер отправки почты требует авторизацию
отправителя (например smtp.yandex.ru).

После установки модуля нужно добавить Read Access к ir.mail_server
для нужных групп через интерфейс OpenERP:
Database Structure -> Models -> ir.mail_server -> Access Rights.

smtp-per-user
=============
This module adds the ability to select the user to whom include
specific smtp settings.
Possible to use when smtp server requires
sender authentification (e.g. smtp.yandex.ru).

After setup you should add Read Access to ir.mail_server for relevant
groups via OpenERP interface:
Database Structure -> Models -> ir.mail_server -> Access Rights.
