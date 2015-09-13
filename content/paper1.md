Title: cisco sigcomm2015
Date: 2015-09-01
Category: reading paper
Tags:
Slug: 
Author:
Summary: 

##Name
[Large-scale Measurements of Wireless Network Behavior](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p153.pdf)

### Summary
This is the typical measurement paper. The paper is organised as : section 2: system architecture, section3: measurement exp1 section4: measurement exp2, section5: measurement exp3, section6, lessons learned from the large scale deployment. The biggest selling point of this paper is scale, scale and scale!
Most of the The paper contributes the following:
**1. exp1** 
reveal the usage, device type, Oses using the record data of a large amount of networks. Network is consists of 2~3 APs which is operated by the same administrative organizations. Here I highlight some results: 
> a1. the total population of clients grows by approximately 37% from 4.07million to 5.58 million. Total usage grow by roughly 62%. The one with the largest usage whose OS is windows.

> a2. Mobile devices download roughly 9 times more than they upload.

> a3. Video and music application such as youtube, netflix make up the largest fraction of usage at 34%. Looking specifically at Netflix, each client consume nearly 1.2GB in a week.

**2. exp2**
Using the Meraki MR16 scan for nearby access points whenever there is no actively transferring traffic. They can only sense the AP which share the same channel. 

> a1. The average number of interferring AP in the 2.4GHz band is 55 and 3.68 in 5GHz.
 
> a2. The energe-detect trigger time, i.e., airtime utilization of 2.4GHz is 25% of median number. 90th percentile access points report 50%. For 5Ghz, median access point report 5% and the 90th percentile access point reporting 30%.

 **3. exp3**
 The Meraki MR18 includes a third 802.11n radio that is dedicated to scanning the entrire 2.4Ghz and 5Ghz spectrum and does not serve client. The highlighted results shows:

 > a1. There is no clear relationship between number of heard interfering APs and utilization in either band. 

 > a2. non-wifi time = time spending on performing energy detection - time receiving 802.11 traffic. 


###Limitations
most of the result from this paper is under my expectations. 


###Question

> 1. how did they make it possible to have a third radio scans both bands(2.4Ghz+5Ghz) simultaneously.

> 2. What is the difference between **Channel State Information(CSI)** and **RSSI** 

> 3. New topic? interference alignment and cancellation??? 