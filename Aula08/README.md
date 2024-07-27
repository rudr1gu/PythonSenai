># Bibliotecas

>### Instalação de bibliotecas...

- `pip install keyboard`

```python
# importando keyboar e renomeando como kb
import keyboard as kb
```
 - `pip install pyautogui`
 ```python
 import pyautogui
 ```

> ## Usando bibliotecas no Python
 ```py
import webbrowser as wb
import pyautogui as pg
import time
import keyboard as kb

wb.open('https://www.google.com.br')
time.sleep(2)
pg.write('One Piece')
pg.press('enter')
time.sleep(2)
pg.click(300,200)
time.sleep(2)
pg.click(500,400)
time.sleep(2)
```

## Selenium

```python
# importa a biblioteca selenium e o módulo webdriver
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

# Abre o navegador
navegador = webdriver.Chrome()
time.sleep(5)

# Acessa a página
navegador.get('https://www.youtube.com/')
time.sleep(5)
# Procura o campo de busca e digita 'rock lee vs gaara ao som de linkin park'
navegador.find_element(By.NAME, 'search_query').send_keys('rock lee vs gaara ao som de linkin park')

# Clica no botão de busca
navegador.find_element(By.ID, 'search-icon-legacy').click()
time.sleep(5)

# Clica no primeiro vídeo
navegador.find_element(By.ID, 'video-title').click()
# time.sleep(60)
enter = input('Pressione Enter para fechar o navegador...')
#manter a janela aberta
```