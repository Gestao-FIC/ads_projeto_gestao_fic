import pandas as pd
from io import BytesIO
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


from sgset.scrapper.Page import Page


class Scraper:
    def __init__(self, driver: webdriver.Chrome):
        self.page = Page(driver)

    def scrape_data(self, url: str) -> pd.DataFrame:
        """Método principal para visitar a página e baixar o Excel."""

        try:
            # Acess SGSET web record link
            self.page.visit(url)

            # Wait for page to load
            wait = WebDriverWait(self.page.driver, 40)

            # Wait for download excel button to load
            download_button = wait.until(EC.element_to_be_clickable(
                (By.ID, 'imgExportarXLS')))

            # Click download excel butto
            download_button.click()
        except:
            return Exception(f"Falha ao acessar o relatório do SGSET")

        try:

            url = "https://sgset.sp.senai.br/Consultas/ExportarResultado.aspx?valor=2"

            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "_hjSessionUser_3611024=eyJpZCI6IjU5ODJkZjBlLWM1MjgtNWYwZi1iODNlLTBmNGQyMDEyMTdkZiIsImNyZWF0ZWQiOjE3MjUzMjE1NDk1NzUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_1NSPT63KB0=GS1.1.1725321549.1.1.1725321617.0.0.0; _ga_NPNLFFWFHT=GS1.2.1725321618.1.0.1725321618.60.0.0; _hjSessionUser_1518986=eyJpZCI6ImY2NjcyODUxLTEwOTUtNTY4NC1iYzA4LWI0ZjQzNTc2NjkzOCIsImNyZWF0ZWQiOjE3MjUzMjE2MjQ5NTcsImV4aXN0aW5nIjpmYWxzZX0=; _ga_4NE68PDN95=GS1.1.1725325071.2.0.1725325071.60.0.0; _ga_LN2SGDFD9Y=GS1.1.1725325071.2.0.1725325071.0.0.0; ASP.NET_SessionId=uwznoufxkvdayt451b4cp4zm; ARRAffinity=c4f09a0188b16d6936fec4a4f68ce4a6a781d0a5d6f6de65b89bbed18b850125; ARRAffinitySameSite=c4f09a0188b16d6936fec4a4f68ce4a6a781d0a5d6f6de65b89bbed18b850125; _fbp=fb.1.1730160320610.97897464424094184; _clck=1dea1sn%7C2%7Cfqf%7C0%7C1763; _gcl_au=1.1.544992455.1730160321; cookie-consent-banner=true; _ga=GA1.1.214132983.1716420201; _ga_RB2RLL3PQR=GS1.1.1730162383.2.0.1730162383.0.0.0; ADRUM=s=1730167475563&r=https%3A%2F%2Ffaculdades.sp.senai.br%2Fcurso%2F93225%2Fdata-science-e-big-data-aplicados-na-industria; _ga_5SV6KGGN3C=GS1.1.1730167475.2.0.1730167475.60.0.0; _ga_EKZCT7XQ85=GS1.1.1731358809.3.0.1731358809.0.0.0; _ga_Q9MZ352JZJ=GS1.1.1731524504.77.1.1731524623.0.0.0; ADRUM_BTa=R:0|g:948b471d-737d-4856-b751-b7e9c2f7ea9f|n:sesisenaisp_36d9c7a8-2e58-4933-8556-bdea7fae7c11; SameSite=None; ADRUM_BT1=R:0|i:1484583",
                "Host": "sgset.sp.senai.br",
                "Origin": "https://sgset.sp.senai.br",
                "Pragma": "no-cache",
                "Referer": "https://sgset.sp.senai.br/Consultas/Resultado.aspx?Processo=%27Resultado+-+Oferta+-+Anal%u00c3%u00adtico%27&Controle=3&Visao=183&Titulo=gestao_curso_fic&Xml=%27%3CBusca%3E%3CDados+Colunas%3d%2212%2c15%2c19%2c16%2c13%2c54%2c53%2c22%2c21%2c75%2c77%2c109%2c5%2c97%2c29%22+Tipo%3d%220%22+Esco%3d%22402%22+Nivel%3d%228%22+PerDe%3d%2201%2f01%2f2024%22+PerAte%3d%2231%2f12%2f2024%22%3E%3C%2fDados%3E%3C%2fBusca%3E%27",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
            }

            # Request excel download
            response = requests.post(url, headers=headers)
            status_code = response.status_code

            # Check response status
            if status_code == 200:

                # Read response content
                excel_data = BytesIO(response.content)

                # Transform excel in a pandas dataframe
                df = pd.read_excel(excel_data)

                return df
            else:
                raise Exception(
                    f"Falha na resposta do SGSET (STATUS {status_code})")
        except ValueError:
            raise ValueError(
                f"SGSET não retornou o relatório de cursos corretamente")
        except Exception as e:
            print(e)
            raise Exception(f"Falha na requisição para o SGSET")
