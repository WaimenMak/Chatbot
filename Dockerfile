From tvbot
COPY main.py /
COPY api.py /
COPY data.py /
COPY secret_key.json /
COPY requirements.txt /
RUN pip install pip update
RUN pip install -r requirements.txt
ENV ACCESS_TOKEN  5160604243:AAE6Qs-_21_3325ONlKIpO-gybcsYQzaqlA
ENV databaseURL "https://comp7940projectmt-default-rtdb.asia-southeast1.firebasedatabase.app/"
ENV PASSWORD "sEETHrRREvQ3H1zfzd59Wat2fjLKCq1naAzCaKDaa8E="
ENV REDISPORT 6380
CMD python main.py