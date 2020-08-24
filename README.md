magleads.com

Database Layout
---------------

Know: id, name, type, location, phone number, website, email

Ideas: How to divide databases? (Ranked by priority)

    2. All in one database (Not recommended)
        
        If we do this the places.txt file will be good because it has most of the major cities in the U.S.
        which contains 832 entrees. Databases can hold 20,000,000 entries. The amount of types that will be used
        in the project will be around 68-80. 832 * 68 = 56576. The max results are 60 per categories. Therefore
        there should be around 40 on average for the categories maybe less, around like 30? If 40 (more likely)
        56576 * 40 = 2,263,040. This is most likely a minimum number of entries. More accurate number would be 
        around 10,000,000 which is half the max number of entries.

    1. By state and start with connecticut (copy list of towns)

        If we do this the cttowns.txt (and other statetowns.txt) file(s) will be good because it has all the towns
        in each state and the databases can hold more information. Databases can hold 20,000,000 entries.
        The amount of types will be around 80 since we have more room or 90. There are 170 towns in CT.
        90 * 170 = 15300 * 60 = 918,000

    3. By type (ex. one for restaurants, one for dry cleaners)

        Would work weird with the websites search methods and stuff 

Python
------

Google places API can get name, location, type, phone number

Google places API can sometimes get the website? (Can we make this better?)

For the email use various sources

    Facebook (m.facebook)

    RateMyArea

    ...

For the types searching will have to be from Google API places


Website
-------

Ideas: How to do searching, members, login, register (paypal payments)

    1. Certain amount of emails per month (monthly fee) and the emails aren't visible on the website
       so that it cannot be manipulated.

    2. 

Other Services
--------------

Email Service

    Should be easy to implement will be something that will be part of being someone who pays for it.