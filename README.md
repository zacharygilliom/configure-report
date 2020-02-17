# configure-report
This script works to eliminate the hassle of working with reports in excel.  Many people keep a large master spreadsheet and over time add data to the master spreadsheet.  This works to get rid of the manual tasks of copying and pasting data and gives you back a clean copy of the updated info.

So we first start with our raw data in our excel sheet.

![Initial-data](https://user-images.githubusercontent.com/23482152/74616902-70a20800-50f8-11ea-93e9-5cf2fe139c0a.png)

From here, we want to add some calculated columns so we can get some useful numeric values.  

![cleaned-and-formatted](https://user-images.githubusercontent.com/23482152/74616957-af37c280-50f8-11ea-8d5a-08e6db831507.png)

There are also some useful info in some of our other columns, but we still need to clean up how it's formatted so we can use it.  With some of our cleaned columns, we will also join this table with some of our other tables that we have.

![referencetable](https://user-images.githubusercontent.com/23482152/74616999-e73f0580-50f8-11ea-88b6-3bcc834831df.png)

This table is not imported with our raw data, this is a table that is created manually, so we need to be able to join this info with our raw data.

We can also print out some quick pivot tables to show our data.

![pivot table by location](https://user-images.githubusercontent.com/23482152/74617043-2bcaa100-50f9-11ea-9c80-002a5ee648ac.png)

This is useful, because if we create these in excel we have to worry about going back in and refreshing the data, and making sure it's picking up all the information within the table.

Lastly we want to include some type of visuals.

![kdeplots](https://user-images.githubusercontent.com/23482152/74617091-6d5b4c00-50f9-11ea-83d3-b62c133285e5.png)

![morekdeplots](https://user-images.githubusercontent.com/23482152/74617119-a09ddb00-50f9-11ea-8e88-4e5515038692.png)

![barplots](https://user-images.githubusercontent.com/23482152/74617176-e0fd5900-50f9-11ea-959f-d51c1fbe1f1b.png)

Currently have the visuals not all in the same figure.  Want to get it to a point where we have all the visuals in one figure and export it as an image to be sent via email or some other method.