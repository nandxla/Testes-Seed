from faker import Faker
import threading

from datetime import date
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def test_contratos(n):
    chorme = webdriver.Chrome()
    fake = Faker()

    # Login
    chorme.get("https://salta.seedtec.com.br/")
    sleep(3)

    chorme.find_element(By.CSS_SELECTOR, 'input[placeholder="E-mail"]').send_keys("fernando@seedtec.com.br")
    chorme.find_element(By.CSS_SELECTOR, 'input[placeholder="Senha"]').send_keys("fernandoSeed")
    chorme.find_element(By.CSS_SELECTOR, 'button[class="ui teal large fluid button"]').click()

    chorme.get("https://salta.seedtec.com.br/contracts/registration")
    sleep(3) 


    for i in range(n):
        cost_center = fake.random_element([
            "Centro de Custo 1",
            "Centro de Custo 2",
            "Centro de Custo 3",
            "Centro de Custo 4",
            "Centro de Custo 5",
        ])
        cnpj_cpf = fake.random_element([
            "75988048000159",
            "72041049000101",
            "51894435000168",
            "47889005000180",
            "23780602000104",
            "48831081000106",
            "25333730000135",
            "01339738000140",
            "15256011000104",
            "11778699001707",
        ])
        corporate_reason = fake.text(max_nb_chars=11)
        contract_value = fake.random_int(min=1000, max=9999)
        form_payment = fake.random_element(["Boleto", "Pix", "Depósito Bancário"])
        contract_validity = fake.date_this_year().strftime("%d/%m/%Y")
        service_description = fake.text()
        contract_date = fake.date_this_year().strftime("%d/%m/%Y")
        legal_control = fake.random_int(min=100, max=999)


        chorme.find_element(By.NAME, "cost_center").send_keys(cost_center)
        chorme.find_element(By.NAME, "cnpj_cpf").send_keys(cnpj_cpf)
        chorme.find_element(By.NAME, "corporate_reason").send_keys(corporate_reason)
        chorme.find_element(By.NAME, "contract_value").send_keys(contract_value)
        chorme.find_element(By.NAME, "form_payment").send_keys(form_payment)
        chorme.find_element(By.NAME, "contract_validity").send_keys(contract_validity)
        chorme.find_element(By.NAME, "service_description").send_keys(service_description)
        chorme.find_element(By.NAME, "contract_date").send_keys(contract_date)
        chorme.find_element(By.NAME, "legal_control").send_keys(legal_control)
        chorme.find_element(By.ID, "contract_document").send_keys(r'C:\Users\nando\Documents\Projetos\Seed\Testes-Seed\PDF Teste.pdf')
        
        chorme.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
        chorme.get("https://salta.seedtec.com.br/contracts/registration")

        sleep(3)
    


if __name__ == "__main__":
    thread = []
    
    for _ in range(15):
        t = threading.Thread(target=test_contratos, args=(100,))
        thread.append(t)
        t.start()
        
    for t in thread:
        t.join()    
    
    print("Foi")
    