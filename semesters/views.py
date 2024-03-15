# from rest_framework import viewsets
# from . import models, serializers

# class SemesterViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         return models.Semester.objects.all()
    
#     def get_serializer_class(self):
#         return serializers.SemesterSerializer
    
#     def get_serializer_context(self):
#         return {'request': self.request}


# class StudentViewSet(serializers.ModelViewSet):
#     def get_queryset(self):
#         return models.Student.objects.filter(product_id=self.kwargs['product_pk']).all()
    
#     def get_serializer_class(self):
#         return ReviewSerializer
    
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}