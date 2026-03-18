## Categories tests

### Get

```bash
curl 'http://localhost:8088/categories' | jq

curl 'http://localhost:8088/categories/1' | jq
```

### POST

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"label":"test"}' \
  'http://localhost:8088/categories'
```

### PUT

```bash
curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"id":1,"label":"Sports"}' \
  'http://localhost:8088/categories/1'
```

### DELETE

```bash
curl -v --header "Content-Type: application/json" \
  --request DELETE \
  'http://localhost:8088/categories/1' | jq
```
