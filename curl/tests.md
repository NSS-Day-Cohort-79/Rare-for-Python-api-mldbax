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
