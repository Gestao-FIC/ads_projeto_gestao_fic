import pandas as pd
from io import BytesIO
import requests


class ScraperService:

    @staticmethod
    def scrape_data() -> pd.DataFrame:
        """Método principal para visitar a página e baixar o Excel."""

        try:

            url = "https://sgset.sp.senai.br/Consultas/Resultado.aspx?Processo=%27Resultado%20-%20Oferta%20-%20Anal%C3%ADtico%27&Controle=3&Visao=183&Titulo=gestao_curso_fic&Xml=%27%3CBusca%3E%3CDados%20Colunas=%2212,15,19,16,13,54,53,22,21,75,77,109,5,97,29%22%20Tipo=%220%22%20Esco=%22402%22%20Nivel=%228%22%20PerDe=%2201/01/2024%22%20PerAte=%2231/12/2024%22%3E%3C/Dados%3E%3C/Busca%3E%27"

            # Acess SGSET web record link
            response = requests.get(url)

            # Get cookies
            cookies = response.cookies

        except:
            raise Exception(f"Falha ao acessar o relatório do SGSET")

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
            response = requests.post(url, headers=headers, cookies=cookies)
            status_code = response.status_code

            # Check response status
            if status_code == 200:

                # Read response content
                excel_data = BytesIO(response.content)

                # Transform excel in a pandas dataframe
                df = pd.read_excel(excel_data, engine='xlrd')

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
