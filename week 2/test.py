import sys
sys.path.append('/home/user/Desktop/task/week 1/algorithim/week 2')

#!/usr/bin/env python
# coding: utf-8

# In[1]:


class listnode:
    def __init__(self,data):
        self.data=data
        self.next=None


# In[2]:


a=listnode(5)
b=listnode(10)
c=listnode(15)
d=listnode(20)
e=listnode(25)
f=listnode(30)


# In[3]:


a.next=b
b.next=c
c.next=d
d.next=e
e.next=f


# In[4]:


a.next.next.data


# In[5]:


b,c=None,None


# In[6]:


a.next.data


# In[7]:


a.next.next.data


# In[8]:


t=listnode(0)
t.next=a


# In[9]:


head=t
while head is not None:
    print(head.data)
    head=head.next


# In[10]:


curnode=a
while curnode is not None and curnode.data!=25:
    curnode = curnode.next
print(curnode.data)


# In[11]:


t=listnode(0)


# In[12]:


t.next=a


# In[13]:


prednode=None
curnode=t
while curnode is not None and curnode.data!=25:
    prednode=curnode
    curnode=curnode.next
prednode.next=curnode.next


# In[14]:


head=t
while head is not None:
    print(head.data)
    head=head.next


# In[15]:


new=listnode(35)


# In[16]:


tail=a
while tail.next is not None:
    tail=tail.next
tail.next=new


# In[17]:


ins=listnode(25)


# In[18]:


pred=None
curnode=t
while curnode is not None and curnode.data!=30:
    pred=curnode
    curnode=curnode.next
pred.next=ins
ins.next=curnode


# In[19]:


head=t
while head is not None:
    print(head.data)
    head=head.next

