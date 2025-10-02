import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.selenium
def test_login_page(live_server, selenium):
    selenium.get(f'{live_server.url}/users/login/')
    
    username_input = selenium.find_element(By.NAME, 'username')
    password_input = selenium.find_element(By.NAME, 'password')
    submit_button = selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    
    username_input.send_keys('testuser')
    password_input.send_keys('password123')
    submit_button.click()
    
    # Espera a mensagem de sucesso aparecer
    WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    
    assert selenium.current_url == f'{live_server.url}/'

@pytest.mark.selenium
def test_cadastrar_serie(live_server, selenium, user):
    # Faz login primeiro
    selenium.get(f'{live_server.url}/users/login/')
    username_input = selenium.find_element(By.NAME, 'username')
    password_input = selenium.find_element(By.NAME, 'password')
    username_input.send_keys(user.username)
    password_input.send_keys('password123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Vai para a página de criar série
    selenium.get(f'{live_server.url}/series/create/')
    
    # Preenche o formulário
    titulo_input = selenium.find_element(By.NAME, 'titulo')
    descricao_input = selenium.find_element(By.NAME, 'descricao')
    ano_input = selenium.find_element(By.NAME, 'ano')
    
    titulo_input.send_keys('Nova Série')
    descricao_input.send_keys('Descrição da série')
    ano_input.send_keys('2024')
    
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Verifica se a série foi criada
    WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    
    # Verifica se está na página de detalhes da série
    assert 'Nova Série' in selenium.page_source