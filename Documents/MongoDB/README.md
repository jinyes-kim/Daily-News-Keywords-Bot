# MongoDB Install Script

- [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [Mongo Express - Docker](https://hub.docker.com/_/mongo-express)


## 몽고디비 기본 설정
```bash
# Add IP bind, Auth Option
vi /etc/mongod.conf

# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0

#security:
security:
    authorization: enabled

```


## 몽고 익스프레스 컨테이너 템플릿
```bash
sudo docker run -itd \
    --name mongo-express \
    -p 8081:8081 \
    -e ME_CONFIG_MONGODB_SERVER="host" \
    -e ME_CONFIG_MONGODB_PORT=27017 \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME="root" \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD="password" \
    mongo-express
```