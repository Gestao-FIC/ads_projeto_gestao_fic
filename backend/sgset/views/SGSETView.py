from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sgset.scrapper.DriverManager import DriverManager
from sgset.scrapper.Scraper import Scraper
from sgset.services.SGSETNormalizer import SGSETNormalizer
from sgset.serializers.SGS7Serializer import SGSETSerializer
from sgset.models import SGSETModel


class SGSETView(APIView):
    def get(self, request):
        url = "https://sgset.sp.senai.br/Consultas/Resultado.aspx?Processo=%27Resultado%20-%20Oferta%20-%20Anal%C3%ADtico%27&Controle=3&Visao=183&Titulo=gestao_curso_fic&Xml=%27%3CBusca%3E%3CDados%20Colunas=%2212,15,19,16,13,54,53,22,21,75,77,109,5,97,29%22%20Tipo=%220%22%20Esco=%22402%22%20Nivel=%228%22%20PerDe=%2201/01/2024%22%20PerAte=%2231/12/2024%22%3E%3C/Dados%3E%3C/Busca%3E%27"

        # Init o WebDriver
        driver_manager = DriverManager()
        driver_manager.start_driver()
        scraper = Scraper(driver_manager.get_driver())

        try:
            # Get data from SGSET
            df_data = scraper.scrape_data(url)

            # Instance normalizer class
            df_data = SGSETNormalizer.rename_columns(df_data=df_data)
            df_data = SGSETNormalizer.remove_duplicates(df_data=df_data)

            # Transform dataframe in python dict
            data = df_data.to_dict(orient='records')
            serializer = SGSETSerializer(data=data, many=True)

            # Save rows in database
            SGSETModel.objects.all().delete()
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Replace day of week string for foreing key
            SGSETNormalizer.find_dayofweek_fk(df_data=df_data)

            return Response(data)
        except ValidationError as e:
            return Response(
                {'error': "Dados não estão conformes às regras do banco de dados"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            # Fecha o WebDriver
            driver_manager.stop_driver()
