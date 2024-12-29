▎Skillzone_study

▎Обзор

Этот проект представляет собой веб-сервис для управления курсами обучения, разработанный с использованием фреймворка Django. Сервис включает в себя функционал авторизации пользователей, кэширование данных, использование классовых представлений (CBV), шаблонов HTML, а также систему прав доступа и валидаторы. Все данные хранятся в реляционной базе данных SQL.

▎Функциональные возможности

• Авторизация пользователей: Регистрация, вход и выход из системы.

• Управление курсами: Создание, редактирование и удаление курсов.

• Кэширование: Оптимизация производительности за счет кэширования часто запрашиваемых данных.

• Права доступа: Разграничение прав пользователей (администраторы, преподаватели, студенты).

• Валидация данных: Использование валидаторов для проверки корректности вводимых данных.

• Интерфейс пользователя: Простой и интуитивно понятный интерфейс на основе HTML-шаблонов.

▎Установка

▎Предварительные требования

• Python 3.x

• Django 4.x

• PostgreSQL

▎Шаги по установке

1. Клонируйте репозиторий:

      git clone https://github.com/Zix-01/skillzone_study.git
      cd skillzone_study
   

2. Создайте виртуальное окружение:

      python -m venv venv
   source venv/bin/activate  # Для Windows используйте venvScriptsactivate
   

3. Установите зависимости:

      pip install -r requirements.txt
   

4. Настройте базу данных:

   Измените настройки базы данных в settings.py на свои данные.

5. Примените миграции:

      python manage.py migrate
   

6. Создайте суперпользователя:

      python manage.py createsuperuser
   

7. Запустите сервер разработки:

      python manage.py runserver

▎Использование

• Для доступа к административной панели перейдите по адресу: http://127.0.0.1:8000/admin и войдите с учетными данными суперпользователя.

• Пользователи могут регистрироваться и входить в систему для доступа к курсам.



Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по электронной почте: ваш_email@example.com.

---

Это базовый шаблон README файла для вашего проекта. Вы можете дополнить его конкретными деталями вашего приложения и инструкциями по его использованию.