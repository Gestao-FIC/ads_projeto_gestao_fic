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

            # Persist sgset rows in database
            self._save_sgset(df_data=df_data)

            # Extract course name and persist in database
            SGSETNormalizer.persist_course_info(df_data=df_data)

            # Extract class infos and persist in database
            df_classes = SGSETNormalizer.persist_class_info(df_data=df_data)

            # Transform dataframe in python dict
            data = df_data.to_dict(orient='records')

            # Get class id and relate with dayofweek
            df_data['class_id'] = [
                str(obj.code).replace('-', '')
                for obj in df_classes
            ]

            # Replace day of week string for foreing key and persist in table "class_schedule"
            df_class_schedule = SGSETNormalizer.find_dayofweek_fk(
                df_data=df_data
            )
            # SGSETNormalizer.persist_class_schedule(df_data=df_class_schedule)

            return Response(data)
        except ValidationError as e:
            return Response(
                {'error': "Dados não estão conformes às regras do banco de dados"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _save_sgset(self, df_data):
        """_summary_

        Args:
            df_data (_type_): _description_
        """

        # Transform dataframe in python dict
        data = df_data.to_dict(orient='records')

        # Save rows in database
        serializer = SGSETSerializer(data=data, many=True)
        SGSETModel.objects.all().delete()
        serializer.is_valid(raise_exception=True)

        return serializer.save()
