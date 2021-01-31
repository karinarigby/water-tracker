#  Water Tracker Garden App

This is a web app that helps bring the user closer to their water consumption goals.

Every day the user gets a new seed. As they log their water intake throughout the day, their seed grows up into a mature and beautiful plant. At the end of the day the new little plant is added to the user's garden.

Garden needs the ongoing watering by daily logging, otherwise they'll whither away one by one until you have to start over.

##  Tech Stack

It's a LEMP Stack, minus the Linux part this time. :wink: EMP - That is, (**e**)NGINX, **M**ySQL, and **P**ython (Flask).

We got some Pytest stuff going on for Unit testing the models.

The Dockerized solution has an NGINX container and a Flask container.
  
##  Demo

  
## What's Missing:
  - CI/CD config files
  - Calling AWS SDKs for stuff stored in S3 buckets
  - Fun plant animations
  - AJAX calls to update the pages without refreshing
  

##  Credits and License
I don't really know how to do the license attributions correctly, but I followed along with the tutorial series by Mbithe Nzomo to get the initial structure of this project going. Then I expanded upon it by adapting the view functions to my needs, adding Pytest test package, Docker settings, etc.

Mbithe's project can be found [here](https://github.com/mbithenzomo/project-dream-team-three).

  

Part of Mbithe's License terms are to put the following content in the project, so here they are below. :point_down: 

  

Credits and License

  

Copyright (c) 2017 Mbithe Nzomo

  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.