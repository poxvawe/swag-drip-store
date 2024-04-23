# название: SWAG DRIP STORE
# автор: Кушманов Леонид

## суть проекта: мой проект - интернет-магазин одежды. здесь возможна регистрация как покупателей, так и продавцов, добавление товаров на сайт для продажи, добавление товаров в корзину для покупки

___ТЗ:___
1. Создание базы данных пользователей(покупателей и продавцов) с полями: id, name, mail, password-hash, cart и type

2. Создание базы данных с товарами: id, name, price.

3. Создание следующих HTML-страниц: аутентификация и авторизация пользователей, главная страница(с карточками товаров), корзина, страница загрузки(добавления) товара для продавцов

4. Реализация возможности для продавцов добавлять товары

5. Создание корзины, в которую можно добавить товары

6. Обеспечить связь между базой данных товаров и пользователями (через поле seller_id, чтобы определить, какой продавец добавил каждый товар)


__Пояснительная записка__: **SWAG DRIP STORE - магазин одежды, автор - Кушманов Леонид**. У меня уже был дизайн сайта на html и css, поэтому мне стало интересно попробовать доработать его, используя flask и базу данных, то есть сделать полноценный рабочий прототип интернет-магазина.
Для реализации использовались следующие библиотеки:
1. **flask:** это основа моего проекта, с её помощью происходит регистрация и авторизация пользователей, проверка, создание форм, заполнение страниц, работа с api
2. **sqalchemy, sqlite:** эти библиотеки необходимы для работы с базой данных, в них хранятся данные и пользователях, товарах и карточках товаров. С помощью этих инструментов было организовано удобное взаимодействие внутри приложения
3. **werkzeug:** библиотека для хэширования и проверки паролей пользователей

Ссылка на презентацию: [https://disk.yandex.ru/i/ypnBCdU9NCMGjw](ссылка_на_презентацию)

