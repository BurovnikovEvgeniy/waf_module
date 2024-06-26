# waf_module

Тема 3. Реализация модуля выявления и блокировки атак типа SQL Injection на HTTP-сервер. (ключевые слова: ModSecurity, NAXSI, нормализация URL, null bytes)

Для запуска и ручного тестирования модуля необходимо инициировать запуск main скрипта
```
python3 main.py
```
Далее необходимо перейти по адресу (http://127.0.0.1:5000) и протестировать waf в форме
<img width="662" alt="image" src="https://github.com/BurovnikovEvgeniy/waf_module/assets/71849985/e772c5e7-5242-404f-a717-9deb1f433f7d">

Для демонстрации waf модуля в составе сервера были реализованы две программы client и server. Для их запуска в отдельных консолях в произвольном порядке необходимо выполнить следующие команды:
```
python3 client.py
```
<img width="566" alt="image" src="https://github.com/BurovnikovEvgeniy/waf_module/assets/71849985/5db03df1-f8d2-4716-a4a3-7a0bd6efe38d">

```
python3 server.py
```
<img width="562" alt="image" src="https://github.com/BurovnikovEvgeniy/waf_module/assets/71849985/9732c4b4-bf33-4a91-85cd-9fadd65319de">

