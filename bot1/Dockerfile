From tvbot
COPY main.py /
COPY search.py /
COPY secret_key.json /
COPY requirements.txt /
RUN pip install pip update
RUN pip install -r requirements.txt
ENV ACCESS_TOKEN  5398859275:AAH5X0dOUBOspdDvhcVUYoM93TRJu-e8m2g
ENV DATABASE_URL  https://comp7940projectmt-default-rtdb.asia-southeast1.firebasedatabase.app/
ENV KEY_PATH  secret_key.json
CMD python main.py