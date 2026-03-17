## Categories tests

### Get

curl 'http://localhost:8000/categories' | jq

### POST

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"label":"test"}' \
  'http://localhost:8000/categories'
```

### PUT

```bash
curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"id":1,"label":"Sports"}' \
  'http://localhost:8000/categories/1'
```
