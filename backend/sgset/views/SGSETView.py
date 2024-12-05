from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sgset.services.sgsetNormalizer import SGSETNormalizer
from sgset.services.scraperService import ScraperService
from sgset.serializers.SGS7Serializer import SGSETSerializer
from sgset.models import SGSETModel


class SGSETView(APIView):
    def get(self, request):
        try:
            # Get data from SGSET
            df_data = ScraperService.scrape_data()

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
            # SGSETNormalizer.find_dayofweek_fk(df_data=df_data)

            return Response(data)
        except ValidationError as e:
            return Response(
                {'error': "Dados não estão conformes às regras do banco de dados"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
