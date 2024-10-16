# Семестровый проект по портированию игры на различные платформы
### Автор: Журавлев Данил Сергеевич ИКБО-08-21

# Описание проекта
Этот проект посвящен портированию игры из сборника More BASIC Computer Games на различные платформы, включая Windows, Linux, NetBSD и Web. Целью проекта является обеспечение точности работы портированной версии игры в соответствии с её оригиналом, написанным на Microsoft BASIC. Для запуска оригинальной версии использовался эмулятор Vintage BASIC.

Основной задачей было не только портировать игру, но и создать автоматические тесты, которые подтверждают, что портированная игра ведет себя точно так же, как и оригинальная. Это достигается через набор диалогов между игроком и компьютером, результаты которых сравниваются с эталонными логами оригинальной игры.

Поддерживаемые платформы
Windows
Linux
NetBSD (повышенной сложности)
Web

# Сборка проекта

Для сборки проекта на различных платформах используется утилита make. 
Ниже приведены команды для каждой из поддерживаемых платформ.

### Windows
mingw32-make windows

### Linux
make linux

### NetBSD
make netbsd

### Web
mingw32-make web

# Примеры работы проекта

Для демонстрации работы портированной игры прилагаются примеры запуска на различных платформах:

Windows:

![windows bocce](https://github.com/user-attachments/assets/2b475753-036b-44d2-b984-4b4f2d2403bb)


Linux:
![linux bocce](https://github.com/user-attachments/assets/3da4e84b-0d96-411a-9171-3513320c56b3)


NetBSD: 
![netbsd main](https://github.com/user-attachments/assets/dba9103a-905d-47f6-86c1-8d360473ac1f)
Web:

![изображение](https://github.com/user-attachments/assets/c97f7c41-6014-43c8-b481-30357255c69d)




# Автоматическое тестирование

![изображение](https://github.com/user-attachments/assets/00bb84ff-74c7-45b0-8167-52aa5ebb7ca1)


# История разработки

Разработка велась в публично доступном Git-репозитории. Весь ход проекта зафиксирован в коммитах с подробными сообщениями, отражающими прогресс работы.


# Заключение

Этот проект является демонстрацией возможностей кроссплатформенного портирования старинных игр, выполненного с соблюдением требований оригинала и автоматического тестирования.
