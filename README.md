# Twitter-Sentiment-Analysis
Please follow below steps to execute this project :
1) Download zoopkeeper, kafka, elastic search , kibana. 
2) Start the servers in the given sequence below : 

      a) Use below command to Start ZooKeeper <br />
      &nbsp;&nbsp;&nbsp;&nbsp;cd C:\kafka .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties  <br />
      b) Use below command to Start kafka-Server <br />
            cd C:\kafka .\bin\windows\kafka-server-start.bat .\config\server.properties  \
      c) Use below command to start Elastic-Search(Run as Admin)\
            cd C:\elastic_stack\elasticsearch-7.9.3-windows-x86_64\elasticsearch-7.9.3\bin>elasticsearch.bat  \
      d) Use below command to start Kibana(Run as Admin)\
            cd C:\elastic_stack\kibana-7.2.0-windows-x86_64\kibana-7.2.0-windows-x86_64\bin>kibana.bat 

3) Run Producer
Run command:- python Sentiment_Analysis_Producer.py on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

4) Run Consumer
Run command:- python Sentiment_Analysis_Consumer.py on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

5) for visualization in kibana please find your localhost port for kibana: usually its 5601 -> localhost:5601/
search for the index you have created in elastic search engine. In my case this part can be found in "consumer.py" with value "elastictweet".
You can choose the type of chart for visualization.
