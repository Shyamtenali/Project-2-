#!/usr/bin/env python
# coding: utf-8

# # Project: Exploring Hacker News Posts
# 

# *The project explores the dataset from the Kaggle competition: hacker News Posts, to run exploratory analysis on which posts recieve more comments and to see if posts created at a certain time recieve more comments*

# *For this analysis, I will 2 different kinds of posts on Hacker News, a popular site where technology related stories (or 'posts') are voted and commented upon. The two types of posts I'll explore begin with either Ask HN or Show HN.*
# 
# *Quick context here - Users submit Ask HN posts to ask the Hacker News community a specific question, such as "Which is the best online course for python?". Similarly, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting.*
# 
# *I'll specifically compare these two types of posts to determine the following:*
# 
# * Do Ask HN or Show HN receive more comments on average?
# 
# * Do posts created at a certain time receive more comments on average?
# 
# *Like any data science project, we begin by reading the dataset*

# In[2]:


from csv import reader 
file = open('hacker_news.csv')
hn1 = reader(file)
hn = list(hn1)


# In[3]:


hn[:6]


# In[4]:


headers = hn[0]
hn = hn[1:]


# In[5]:


print(headers)


# In[6]:


print(hn[:6])


# In[7]:


ask_posts = []
show_posts = []
other_posts = []


# In[8]:


for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
   


# In[9]:



print('The number of ask hn posts are ', len(ask_posts))
print('The number of show hn posts are ',len(show_posts))
print('The number of other posts are ', len(other_posts))


# In[10]:


#Now let us have a look at the comments across the ask hn and show hn posts

#Creating a function to calculate the total and average number of posts 

def totandavg(templist): # will return the total number and mean number of comments
    temp_total = 0
    temp_count = 0
    for row in templist:
        num_comments = row[4]
        num_comments = int(num_comments)
        temp_total += num_comments
        temp_count += 1
        
    temp_mean = temp_total/temp_count
    
    return temp_total, temp_mean

total_ask_comments, avg_ask_comments = totandavg(ask_posts)

print('The average number of Ask HN comments are ',round(avg_ask_comments, 2))

total_show_comments, avg_show_comments = totandavg(show_posts)
print('The average numnber of Show HN comments are ', round(avg_show_comments, 2))


# In[11]:


import datetime as dt 
result_list = []

for row in ask_posts:
    temp = []
    temp.append(row[6])
    num_comments = int(row[4])
    temp.append(num_comments)
    result_list.append(temp)
    


# In[12]:


counts_by_hour = {}
comments_by_hour = {}


# In[13]:


comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    dt_created = each_row[0]
    num_comment = each_row[1]
    time = dt.datetime.strptime(dt_created, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += num_comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = num_comment
        counts_by_hour[time] = 1

print("Hourly comments number : ", comments_by_hour)
print("\n")
print("Hourly counted number :", counts_by_hour)


# In[17]:


avg_by_hour = []

for comment in comments_by_hour:
    avg_by_hour.append([comment, comments_by_hour[comment] / counts_by_hour[comment]])
    


# In[18]:


print(avg_by_hour)


# In[19]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
print(swap_avg_by_hour)


# In[20]:


sorted_swap = sorted(swap_avg_by_hour, reverse = True)


# In[23]:


print("Top 5 Hours for Ask Posts Comments: ", sorted_swap[:5])


# In[24]:


for avg, hr in sorted_swap[:5]:
    print("{}:{:.2f}".format(
        dt.datetime.strptime(hr, "%H").strftime("%H:%M"), avg))


# *Based on the dataset documentation, the timezone used is the eastern time in the US, 15:00 will be equivalent to 3:00 pm est. The top 5 hours for most comments on Ask Posts are 15:00, 02:00, 20.00, 16:00 and 21.00. The hour that receives the most comments on average is 15:00 with thirty nine comments per post.*
# 

# In[ ]:




