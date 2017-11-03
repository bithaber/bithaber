FROM owl.registry/bithaber:base

MAINTAINER Hasan Basri <hbasria@gmail.com>

COPY . /app

RUN /home/user/.virtualenvs/app/bin/pip install -r /app/resources/requirements/prod.txt

RUN chown -R user:user /home/user /app

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

WORKDIR /app

EXPOSE 8000

VOLUME ["/app", "/var/log/user"]

CMD ["runserver", "0.0.0.0:8000"]

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
