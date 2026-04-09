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

- pytest
```
pytest store/tests
pytest store/tests/test_collections.py
pytest store/tests/test_collections::TestCreateCollection
pytest store/tests/test_collections::TestCreateCollection::tes_something
pytest -k anonymous
```

@pytest.mark.skip

- Continuous testing
pytest-watch => ptw