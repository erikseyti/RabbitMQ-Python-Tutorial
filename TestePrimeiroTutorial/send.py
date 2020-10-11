#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

channel.basic_publish(exchange='', routing_key='hello', body='Teste de envio de mensagem!')
print(' [x] Foi mandado "Teste de envio de mensagem!" ')

connection.close()