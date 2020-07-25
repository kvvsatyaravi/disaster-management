from .models import A, B, C

A.objects.values('b__color', 'c__taste', 'c__smell')\
         .order_by('id') \
         .distinct()
