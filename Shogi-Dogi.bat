@echo off
:: Aktywuj wirtualne środowisko
call .venv\Scripts\activate
pip install -r requirements.txt
:: Uruchom skrypt Python
python game.py

