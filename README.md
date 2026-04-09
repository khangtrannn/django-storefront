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

- Performance testing (locust)
locust -f locustfiles/browse_products.py
django-silk

- Performance optimization
Optimize the Python code
```
# Preload related objects
Product.objects.select_related('...')
Product.objects.prefetch_related('...')

# Load only what you need
Product.objects.only('title)
Product.objects.defer('description')

# Use values
Product.objects.values()
Product.objects.values_list()

# Count properly
Product.objects.count()
len(Product.objects.all()) # BAD

# Bulk create/update
Product.objects.bulk_create([])
```

Re-write the query

Tune the database

Cache the result