From python
COPY main.py /
COPY requirements.txt /
RUN pip install pip update
RUN pip install -r requirements.txt
ENV ACCESS_TOKEN  5160604243:AAE6Qs-_21_3325ONlKIpO-gybcsYQzaqlA
ENV HOST "redis-13194.c258.us-east-1-4.ec2.cloud.redislabs.com:13194"
ENV PASSWORD "D3lKGgY0sQfjsUuuMSnYmBDcWvzttUSt"
ENV REDISPORT 13194
CMD python main.py