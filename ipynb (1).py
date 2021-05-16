#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = ['p','p','e','s']
list2 = ['e','e','s','p']
list3 = ['e','p','p','s']

    ## Создаем словарь со всеми возможными значениями из списка 1 ## 

dict = {'list1':[], 'list2':[], 'list3':[]}
for i in range(len(list1)):
    if list1[i] not in dict['list1']:
        dict['list1'].append(list1[i])
        i+=1
    else:
        i+=1

list1_dict = {}
for i in dict['list1']:
    list1_dict[i]=list1.count(i)

    ##  Создаем словарь со всеми возможными значениями из списка 2 ##

for i in range(len(list2)):
    if list2[i] not in dict['list2']:
        dict['list2'].append(list2[i])
        i+=1
    else:
        i+=1
        
list2_dict = {}
for i in dict['list2']:
    list2_dict[i]=list2.count(i)
    
    ##  Создаем словарь со всеми возможными значениями из списка 3 ##

for i in range(len(list3)):
    if list3[i] not in dict['list3']:
        dict['list3'].append(list3[i])
        i+=1
    else:
        i+=1
        
list3_dict = {}
for i in dict['list3']:
    list3_dict[i]=list3.count(i)


# In[2]:


## Смотрим на наши словари (просто для себя) ##

print(list1_dict,list2_dict,list3_dict)


# In[6]:


## Находим, какое максимально часто встречающееся значение и сколько раз встречается для Списка 1 ##

max_count_list1 = 0

for i in range(len(list(list1_dict.items()))):
if list(list1_dict.items()) [i][1] > max_count_list1:
    max_count_list1 = list(list1_dict.items()) [i][1] 

for i in range(len(list(list1_dict.items()))):
if list(list1_dict.items()) [i][1] == max_count_list1:
    max_list1_key = list(list1_dict.items()) [i][0]
    
print(max_count_list1,max_list1_key) 

## Находим, какое максимально часто встречающееся значение и сколько раз встречается для Списка 2 ##

max_count_list2 = 0

for i in range(len(list(list2_dict.items()))):
if list(list2_dict.items()) [i][1] > max_count_list2:
    max_count_list2 = list(list2_dict.items()) [i][1] 
    
for i in range(len(list(list2_dict.items()))):
if list(list2_dict.items()) [i][1] == max_count_list2:
    max_list2_key = list(list2_dict.items()) [i][0]

print(max_count_list2,max_list2_key) 

## Находим, какое максимально часто встречающееся значение и сколько раз встречается для Списка 3 ##

max_count_list3 = 0


for i in range(len(list(list3_dict.items()))):
if list(list3_dict.items()) [i][1] > max_count_list3:
    max_count_list3 = list(list1_dict.items()) [i][1] 
    
for i in range(len(list(list3_dict.items()))):
if list(list3_dict.items()) [i][1] == max_count_list3:
    max_list3_key = list(list3_dict.items()) [i][0]
    
print(max_count_list3,max_list3_key) 


# In[ ]:




