![Normal image result](static/image/logo.png)

Xeye is made by python 3.7, Flask and Machine learning(Tensorflow).

# Demo video
[![Demo video](static/image/youtube.png)](https://www.youtube.com/watch?v=pLcgKzmTZXE)


# Purpose
Xeye work to filter porn image.

# Accuracy
**Average: 97.49%**

# Caution
Accuracy may vary depending on the quality of the photo.

# Service
## Page
### http://127.0.0.1:5001/
* Method: GET
* Service page:
    * ![Normal image result](static/image/xeye_filter_page_normal_result.png)
    * ![Porn image result](static/image/xeye_filter_page_porn_result.png)
## API
### http://127.0.0.1:5001/xeye/predict/file
* Method: POST
* Request:
```
<form action="/xeye/predict/file" method="POST"
      enctype="multipart/form-data">
    <input type="file" name="file"/>
    <input type="submit"/>
</form>
```
### http://127.0.0.1:5001/xeye/predict/url
* Method: POST
* Request: 
```
Request body:
{
	"url": "https://ei.rdtcdn.com/m=eGJF8f/media/videos/201902/28/14197691/original/13.jpg"
}
```

### Response
#### SUCCESS
```
Response nody:
{
    "status": "SUCCESS"
    "data": "{0: {'label': 'Porn_Image', 'rate': ca}, 1: {'label': 'Normal_Image', 'rate': 0.0000001‬}}",
}
```
#### FAIL
```
Response nody:
{
    "status": "FAIL"
    "message": "Can't predict image file.",
}
```
# Version 
| Version | Release date | Normal fail/total count | Normal accuracy | Porno fail/total count | Porno accuracy | Remark                                                  |
|---------|--------------|-------------------------|-----------------|------------------------|----------------|---------------------------------------------------------|
| 1.0.0   | 05/06/2020   | 45/3020                 | 98.50%          | 48/6622                | 99.27%         | Learning normal image 200 and porn image 200            |
| 1.0.1   | 05/06/2020   | 5/3020                  | 99.83%          | 30/6681                | 99.55%         | Version 1.0.0 add normal image 45 and porn image 48     |
| 1.0.2   | 05/06/2020   | 6/3020                  | 99.70%          | 25/6687                | 99.62%         | Version 1.0.1 add normal image 4 and porn image 30      |
| 1.0.2   | 05/06/2020   |                         |                 | 12/34331               | 99.96%         | Others(redtube) 34,331 porn image                       |
| 1.0.4   | 05/07/2020   |                         |                 | 34/2190                | 98.44%         | Others(xxxvideo) 2,190 porn image including text banner |
| 1.0.5   | 05/07/2020   | 29/3013                 | 99.03%          | 40/2370                | 98.34%         | Others 2,370 porn image including text banner           |
| 1.0.6   | 05/07/2020   | 3/94                    | 96.80%          | 44/550                 | 92.00%         | Others 550 porn image including text banner             |
| 1.0.7   | 05/07/2020   |                         |                 |                        | 98.68%         | Random website image search                             |
| 1.0.8   | 05/07/2020   |                         |                 |                        | 98.86%         | instagram image upload                                  |
| 1.0.9   | 05/07/2020   |                         |                 |                        | 98.43%         | facebook image upload                                   |
| 1.0.10  | 05/08/2020   |                         |                 |                        | 98.84%         | image upload                                            |
| 1.0.11  | 05/08/2020   |                         |                 |                        | 97.29%         | image upload (Porn: 666, Normal: 856)                   |
| 1.0.12  | 05/08/2020   |                         |                 |                        | 97.95%         | image upload (Porn: 715, Normal: 865)                   |
| 1.0.13  | 05/09/2020   |                         |                 |                        | 97.85%         | image upload (Porn: 720, Normal: 899)                   |
| 1.0.14  | 05/09/2020   |                         |                 |                        | 97.36%         | image upload (Porn: 747, Normal: 925)                   |
| 1.0.15  | 05/09/2020   |                         |                 |                        | 97.49%         | image upload (Porn: 807, Normal: 940)                   |
| 1.0.16  | 05/09/2020   |                         |                 |                        | 97.49%         | image upload (Porn: 865, Normal: 940)                   |

# License
```
Copyright (c) 2020 by Hyunkeun Park (https://github.com/hermes7308/xeye)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
