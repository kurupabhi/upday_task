# Assignment task for Data Engineer notes.

#### S3 files access
I was able to directly read and access the files using the given links and so did not create boto3 instances to access it.

#### Unclear data dictionary
I could not confirm if the "ID" column is the user_id. I had doubts on the column since it had only 16 distinct ids and all the rest of the dataset contained nulls. And issue I noticed with the field was that it did not have any corresponding article views and had only card views. This would not help with the ctr calculations.
And so, I used the original "id" column which is also used as the "article_id" for the article_performance table.

****
I have also included a jupyter notebook with my exploration code.
