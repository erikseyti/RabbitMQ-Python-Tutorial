#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Sent from the Send2 file process')
print(" [x] Sent 'Sent from the Send2 file process'")

for n in range(10):
    print(n)
    channel.basic_publish(exchange='', routing_key='hello', body='Mensagem Enviada no for de numero' + str(n+1))
    print(" [x] Sent 'Mensagem Enviada no for de numero'")
    print(f" Interacao {n}")

connection.close()