# rabbitMQ
sample code base to understand the producer and consumer wrking in rabbitMQ

# run rabbit in docker
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

to access docker hub go to : localhost:15672

# Notes:
## Important concepts of rabbit MQ 
https://www.youtube.com/watch?v=iIjCjUKwzZw&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO&index=3

rabbit MQ is a message Broker
producers -> entities that produce messages to be consumed by the consumer| can have multiple producers that  sends messages to consumers

exchange is the core of rabbitMQ, it knows how to root messages from producer to consumers|there will be different exchanges in a rabbitMQ| producer is tied to one or more exchange

Queues-> exchanges push messages to queue . a message wil sit in this queues until it get consumed by a consumer|Queue is tied to none(queue wont recieve any messages),one or more exchanges

consumers -> entities that listen to messages of producers|can have multiple producers|consumers might not listen to many messages or might listen from multiple queues

connection-> every producer or consumer will have a tcp connection rabbitmq broker.there will be mutliple channels used by producer to send in messages using different threads.. 

channels-> the messages are send to each connection   using threads.. each threads use seperate channels.such that the channels are isolated from one another

## rabbit mq working
Producers send messages to exchanges. Producers are clients or applications that send messages to RabbitMQ for processing. These messages are sent to exchanges, which are the routing components of RabbitMQ.

Exchanges route messages to queues. Exchanges receive messages from producers and route them to queues based on the exchange type and routing key. Queues are storage components that hold the messages until they are consumed.

Consumers receive messages from queues. Consumers are clients or applications that receive messages from RabbitMQ. They subscribe to specific queues and consume messages from them as they become available.

Messages are acknowledged or rejected. After a message is consumed, the consumer sends an acknowledgement to RabbitMQ to let it know that the message has been successfully processed. If the message cannot be processed, it is rejected and RabbitMQ can take appropriate action, such as requeueing the message or discarding it.

RabbitMQ ensures message delivery. RabbitMQ provides several features to ensure that messages are delivered reliably, including message acknowledgements, message persistence, and message retries.
