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

## Tag tests

### Get

```bash
curl 'http://localhost:8088/tags' | jq

curl 'http://localhost:8088/tags/1' | jq
```

### POST

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"label":"test"}' \
  'http://localhost:8088/tags'
```

### PUT

```bash
curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"label":"Sports"}' \
  'http://localhost:8088/tags/5'
```

### DELETE

```bash
curl -v --header "Content-Type: application/json" \
  --request DELETE \
  'http://localhost:8088/tags/5' | jq
```

## Users test

### Register

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"first_name":"Patrick", "last_name":"Starr", "username":"This_Is_Patrick1", "email":"NO!ThisIsPatrick*84@bikinibottom.oc", "password":"wombo", "bio":"WHO ARE YOU PEOPLE!"}' \
  'http://localhost:8088/register'
```

### Login

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"ready2fry", "password":"krabbypatty1"}' \
  'http://localhost:8088/login'
```

## Posts tests

### Get

```bash
curl 'http://localhost:8088/posts' | jq

curl 'http://localhost:8088/posts/1' | jq

curl 'http://localhost:8088/approved-posts' | jq

```

### POST

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"userId":1,"categoryId":1,"title":"test title","imageUrl":"test.url","content":"test post please ignore"}' \
  'http://localhost:8088/posts'
```
