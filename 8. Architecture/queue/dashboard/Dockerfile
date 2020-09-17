FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install rq-dashboard
CMD ["rq-dashboard", "-H", "redis"]