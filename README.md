- mixins
- serializer
  - serializers.ModelSerializer
  - serializers.Serializer
- deserializer
- generic views
  - APIView
  - ListCreateAPIView
  - RetrieveUpdateDestroyAPIView

- ModelViewSet
- ReadOnlyModelViewSet

- Routers
  - SimpleRouter
  - DefaultRouter
  - Nested Router

- Generic filter / django-filter

- Signal

- Sending Emails

- Running Background Tasks (Celery)
  - Message Broker
    - Redis (in-memory data store)
    - RabbitMQ (real, enterprise-grade broker)
celery -A storefront worker --loglevel=info
celery -A storefront beat --loglevel=info