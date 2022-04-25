# celery_stalin

Step to configure:
   1. First install celery: pip3 install celery
   2. Configure RabbitMQ: brew install rabbitmq
   3. Start RabbitMQ: rabbitmq-server
   4. Configure RabbitMQ for Celery:
        # add user 'stalin' with password 'stalin123'
        $ rabbitmqctl add_user stalin stalin123
        # add virtual host 'stalin_vhost'
        $ rabbitmqctl add_vhost stalin_vhost
        # add user tag 'stalin_tag' for user 'stalin'
        $ rabbitmqctl set_user_tags stalin stalin_tag
        # set permission for user 'stalin' on virtual host 'stalin_vhost'
        $ rabbitmqctl set_permissions -p stalin_vhost stalin ".*" ".*" ".*"
   5. Start Celery Worker: celery -A celery_stalin worker --loglevel=info
   6. Run task: python3 -m celery-stalin.run_tasks
   7. Monitor Celery in Real Time: 
         pip3 install flower
         celery -A celery_stalin flower
   8. Sqilite DB:
         -> sqlite3 db.sqlite3
         -> .tables
         -> select * from celery_taskmeta
