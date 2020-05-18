FROM django2.2:latest


ENV APP_PATH /opt/apps
COPY . $APP_PATH/
WORKDIR $APP_PATH

RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt
RUN python manage.py collectstatic --noinput
