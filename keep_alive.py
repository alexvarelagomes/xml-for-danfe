from playwright.sync_api import sync_playwright
import time

def manter_ativo():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://xml-for-danfe.streamlit.app/", wait_until="networkidle")     

        botao_restaurar = page.locator('//*[@id="root"]/div[1]/div/div/div/div/button')
        
        if botao_restaurar.is_visible():
            print("Aplicação em repouso detectada. Clicando no botão para reativar...")
            botao_restaurar.click()
            time.sleep(15) 
            print("Processo de reativação concluído.")
        else:
            print("A aplicação já está ativa e rodando normalmente. Nenhum clique necessário.")
            
        browser.close()

if __name__ == "__main__":
    manter_ativo()