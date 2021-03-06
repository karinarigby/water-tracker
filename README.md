![](/docs/title-pic.png)
#  Water Tracker Garden App

This is a web app that helps bring the user closer to their water consumption goals.

Every day the user gets a new seed. As they log their water intake throughout the day, their seed grows up into a mature and beautiful plant. At the end of the day the new little plant is added to the user's garden.

Garden needs the ongoing watering by daily logging, otherwise they'll whither away one by one until you have to start over.

There's two parts to the app: 
 - The administrative side, where the admin can manage users, different kinds of plants, and the activities.
 - The actual tracking logic itself, where the user can login, log water intake, set goals, view their garden and progress, challenge friends, etc.
 
 I am focusing on the administrative stuff first, and then will shift my focus to the actual tracking afterwards.

##  Demo

Take a look [here](http://3.97.179.20) for a running demo. 

##  Tech Stack

It's a LEMP Stack, that is, (**e**)NGINX, **M**ySQL, and **P**ython (Flask).

The Dockerized solution has an NGINX container exposed to the outside that forwards to the Flask container.

Here's the current deployment structure, with the Database ER diagram on the right:

<img src="/docs/AWS-project-structure-diagram.png" width="300"> <img src="/docs/Database-ER-diagram.png" width="300">

Both of these diagrams may change as the app grows in complexity.

## To Do:
For current status of the specific project management tasks, take a look at my app's public [Trello Board](https://trello.com/b/S0eno1QN/water-tracker-consumption-app).


## What's Missing:
  - CI/CD config setup
  - AWS S3 content delivery for the static files
  - Taking advantage of AWS's ECS and ECR for Docker images
  - DNS config with AWS Route 53
  - Fun plant animations and evolutions
  - AJAX calls to update the pages without refreshing
  - Functional tests (i.e., Selenium)

##  Credits and License

Note: I followed along with the tutorial series by Mbithe Nzomo to get the initial structure of the Flask part of the project. Then I expanded upon it by adapting the view functions according to my needs, adding Pytest test package, Docker settings, etc. 

Mbithe's project can be found [here](https://github.com/mbithenzomo/project-dream-team-three).

Part of Mbithe's License terms are to put the following content in the project, so here they are below. :point_down: 

Credits and License

Copyright (c) 2017 Mbithe Nzomo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
