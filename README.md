# Assignment task for Data Engineer notes.

#### S3 files access
I was able to directly read and access the files using the given links and so did not create boto3 instances to access it.

#### Unclear data dictionary
I could not confirm if the "ID" column is the user_id. I had doubts on the column since it had only 16 distinct ids and all the rest of the dataset contained nulls. And issue I noticed with the field was that it did not have any corresponding article views and had only card views. This would not help with the ctr calculations.
And so, I used the original "id" column which is also used as the "article_id" for the article_performance table.

#### Postgres connection
I have not modified the connection parameters for the Postgres database. And I have not tested the connection and the Docker file since I dont't have postgres setup on my personal machine and I have not worked with Docker before.

#### Further notes
* I have included pandas and sqlalchemy in the requirements.txt file
* I have not setup any tests due to lack of knowledge and experience with this, but the test that I would use on the provided datasets is to check for nulls in the TIMESTAMP and id columns. This can be setup using pytest, however I have never done this before and I only know this after my explorations related to the task.

****
I have also included a jupyter notebook with my exploration code.
