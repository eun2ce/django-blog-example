# realworld

## run
```
$ docker-compose up -d --build
```

## containerized
frontend, backend, db 세 개의 컨테이너로 실행합니다.
docker-compose를 이용해 한 번에 구성을 실행할 수 있습니다.

### frontend containerize

node alpine 중에서도 상세 버전이 확인 가능한 아래 버전을 사용합니다.
```buildoutcfg
FROM node:14.15.4-alpine3.11
```

```buildoutcfg

```