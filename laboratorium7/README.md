# Load tests on GuidePRO application
Application is my team's Bachelor of engineering project. 
For now application on Github has a private visibility.

## Test preview:
Our application has requirement to be able to handle 3000 of end users in total.
In this set of load tests we are going to send this amount of responses in different
periods of time to test capabilities of our back-end service.

### 1 Case:
3000 requests in 150 seconds(2.5 min.)
![plot](./result_images/3000,150.png)
<br>
Results in latency are:
<br>
Average - 7ms
<br>
Min - 5ms
<br>
Max - 18ms
<br>
Error percentage - 0%
![plot](./result_images/3000,150stat.png)
### 2 Case:
3000 requests in 120 seconds(2 min.)
![plot](./result_images/3000,120.png)
<br>
We don't see any significant change in latency.
<br>
Results in latency:
<br>
Average - 7ms
<br>
Min - 5ms
<br>
Max - 13ms
<br>
Error percentage - 0%
![plot](./result_images/3000,120stat.png)
### 3 Case:
3000 requests in 90 seconds(1.5 min.)
![plot](./result_images/3000,90.png)
<br>
We can observe very small increase in maximum latency, to be specific 3ms.
This change won't really cause any issue in application.

<br>
Results in latency:
<br>
Average - 7ms
<br>
Min - 5ms
<br>
Max - 31ms
<br>
Error percentage - 0%

![plot](./result_images/3000,90stat.png)
### 4 Case:
3000 requests in 60 seconds
![plot](./result_images/3000,60.png)
<br>
We can observe minimal decrease in average, min and max latency.
It's not really a change which make a difference for us.

<br>
Results in latency:
<br>
Average - 6ms
<br>
Min - 4ms
<br>
Max - 14ms
<br>
Error percentage - 0%

![plot](./result_images/3000,60stat.png)
### 5 Case:
3000 requests in 40 seconds
![plot](./result_images/3000,40.png)
<br>
We can observe increase in average latency. It almost doubled, 
but still is only 24ms so we don't see it as an issue.

<br>
Results in latency:
<br>
Average - 6ms
<br>
Min - 4ms
<br>
Max - 24ms
<br>
Error percentage - 0%

![plot](./result_images/3000,40stat.png)
### 6 Case:
3000 requests in 30 seconds
![plot](./result_images/3000,30.png)
<br>
We don't see any significant changes in latency.

<br>
Results in latency:
<br>
Average - 6ms
<br>
Min - 4ms
<br>
Max - 28ms
<br>
Error percentage - 0%

![plot](./result_images/3000,30stat.png)
### 7 Case:
3000 requests in 20 seconds
![plot](./result_images/3000,20.png)
<br>
We can see first significant increase in maximum latency.
It increased 3.5 times. Still it didn't reached 100ms, so 
it's not causing any real issues, but it can be sign of reaching 
the first limit. 

<br>
Results in latency:
<br>
Average - 7ms
<br>
Min - 4ms
<br>
Max - 81ms
<br>
Error percentage - 0%

![plot](./result_images/3000,20stat.png)
### 8 Case:
3000 requests in 15 seconds
![plot](./result_images/3000,15.png)
<br>
We can see one more time decrease of average latency. 
It's a sign that previous assumption about reaching 
the first limit was incorrect.

<br>
Results in latency:
<br>
Average - 8ms
<br>
Min - 4ms
<br>
Max - 26ms
<br>
Error percentage - 0%

![plot](./result_images/3000,15stat.png)
### 9 Case:
3000 requests in 10 seconds
![plot](./result_images/3000,10.png)
<br>
We can now finally declare that we reached first limit. Limit of 
high increasing of latency. Average latency jumped from 8ms to over 
1000ms. Max latency increased from 26ms to over 4.5 thousands ms. 
Test will be continued to find next limits, like for example when first 
HTTP connections errors will appear.

<br>
Results in latency:
<br>
Average - 1041ms
<br>
Min - 7ms
<br>
Max - 4549ms
<br>
Error percentage - 0%

![plot](./result_images/3000,10stat.png)
### 10 Case:
3000 requests in 6 seconds
![plot](./result_images/3000,6.png)
<br>
One more time we can see increase in average and maximum latency. 
Average latency trippled from 1s to 3s, and max latency doubled 
from 4.5s to 9.5s. Test will be continued to find first occuring 
HTTP connections errors.

<br>
Results in latency:
<br>
Average - 3144ms
<br>
Min - 9ms
<br>
Max - 9479ms
<br>
Error percentage - 0%

![plot](./result_images/3000,6stat.png)
### 11 Case:
3000 requests in 4 seconds
![plot](./result_images/3000,4.png)
<br>
We've reached new limit. Average and maximum latency decreased, 
but also error percentage jumped from 0% to 47.67%. We reached 
limit where we stop to continue load testing.

<br>
Results in latency:
<br>
Average - 3144ms
<br>
Min - 9ms
<br>
Max - 9479ms
<br>
Error percentage - 47.67%

![plot](./result_images/3000,4stat.png)