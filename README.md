smtp-per-user
=============
Модуль добавляет возможность выбрать пользователя, к которому
относятся конкретные настройки smtp сервера.

В настройках сервера исходящей почты появляется поле "Owner", в котором
возможно выбрать пользователя для этого сервера.

Возможно применять, когда сервер отправки почты требует авторизацию
отправителя (например smtp.yandex.ru).

После установки модуля нужно добавить Read Access к ir.mail_server
для нужных групп через интерфейс OpenERP / Odoo:
Database Structure -> Models -> ir.mail_server -> Access Rights.

smtp-per-user
=============
This module adds the ability to select the user to whom include
specific smtp settings.

Adds "Owner" field for outgoing mail server settings. It becames
possible to point User for this settings.

Possible to use when smtp server requires
sender authentification (e.g. smtp.yandex.ru).

After setup you should add Read Access to ir.mail_server for relevant
groups via OpenERP / Odoo interface:
Database Structure -> Models -> ir.mail_server -> Access Rights.
