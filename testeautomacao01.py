import pyautogui
from time import sleep
pyautogui.click(1489,19, duration=2)
pyautogui.moveTo(1590,208, duration=2)
pyautogui.mouseDown(button='left', x=1591, y=208)
pyautogui.moveTo(1591,278, duration=2)
pyautogui.mouseUp(button='left', x=1591,y=278)
pyautogui.click(230,486, duration= 2)
pyautogui.click(346,64, duration=2)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(655,870, duration=2)

pyautogui.tripleClick(643,540, duration=2)

pyautogui.press('del')
pyautogui.press('enter')
pyautogui.hotkey('shift', '8')
pyautogui.hotkey('shift', '"')
#realizar requisicoes para o servidor
import requests
from bs4 import BeautifulSoup
response = requests.get(

'https://www.kabum.com.br/produto/472908/monitor-gamer-lg-ultragear-lg-34-curvo-led-wqhd-ultrawide-160hz-1ms-displayport-e-hdmi-amd-freesync-premium-hdr10-99-srgb-34gp63a-b'                         

)
#####
#variavel contendo todo conteudo html da pagina
contentHtml = response.content

#transformando a var com conteudo em um objeto e validando o html dele
site = BeautifulSoup(contentHtml, 'html.parser')
contentCard = site.find('div', attrs={'class': 'container-purchase'})
#print(contentCard.prettify())
titulo = contentCard.find('h1', attrs={'class': 'dVrDvy'})
print(titulo.text)

precoAvista = contentCard.find('h4', attrs={'class': 'finalPrice'})
print(precoAvista.text)

