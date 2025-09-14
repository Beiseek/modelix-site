@echo off
echo Загружаем изменения на GitHub...

REM Добавляем Git в PATH
set PATH=%PATH%;C:\Program Files\Git\bin

REM Переходим в папку проекта
cd /d "C:\Users\MOD PC COMPANY\Desktop\kwork.Modelix.сайт"

REM Проверяем статус Git
git status

REM Добавляем файлы
git add static/css/styles.css main/templates/main/index.html

REM Коммитим изменения
git commit -m "Исправил размер заголовка 'ОСТАВЬТЕ ЗАЯВКУ' на мобилке"

REM Загружаем на GitHub
git push origin main

echo Изменения успешно загружены!
pause

