# Xeye
Xeye is made by python 3.7, Flask and Teachable machine.

# Purpose
Xeye work to filter porno image.

# Service
## API
### {http://127.0.0.1:5000}/
* method: GET
* Service page:
    
### {http://127.0.0.1:5000}/xeye/predict/file
### {http://127.0.0.1:5000}/xeye/predict/url

# Version 
| Version | Release date | Normal fail/total count | Normal accuracy | Porno fail/total count | Porno accuracy | Remark                                              |
|---------|--------------|-------------------------|-----------------|------------------------|----------------|-----------------------------------------------------|
| 1.0.0   | 05/06/2020   | 45/3020                 | 98.50%          | 48/6622                | 99.27%         | Learning normal image 200 and porn image 200        |
| 1.0.1   | 05/06/2020   | 5/3020                  | 99.83%          | 30/6681                | 99.55%         | Version 1.0.0 add normal image 45 and porn image 48 |
| 1.0.2   | 05/06/2020   | 6/3020                  | 99.70%          | 25/6687                | 99.62%         | Version 1.0.1 add normal image 4 and porn image 30  |
| 1.0.2   | 05/06/2020   |                         |                 | 12/34331               | 99.96%         | Others(redtube) 34,331 porn image                   |
