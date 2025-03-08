"""
//Setting up the tables

Table activities {
  activity_id integer [primary key]
  title varchar[30]
  description text
  tags varchar[20]
  expense float
  duration time 
  location float
  min_people integer
  max_people integer //if maximum = -1 then no maximum
}

Table users {
  user_id integer [primary key]
  username varchar
  password varchar
  activ_done integer
  faves integer
}

// Relations between activities and user
// Completed activies
Ref: activities.activity_id < users.activ_done
// Favourite activites
Ref: activities.activity_id < users.faves
"""

import sqlite3

