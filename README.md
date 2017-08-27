# www.feifeiwd.com

## docker部署博客

### 构建博客镜像
docker  build -t ffwd/blog:latest  .

### 启动服务
docker-compose  -f docker-compose.deploy.yaml  up

### 进入mysql容器导入备份

#### mysql备份
docker exec -ti wwwfeifeiwdcom_mysql_1 sh -c "mysqldump  -uroot -ppasswd ffdata > /opt/`date +%F`ffwd.sql"