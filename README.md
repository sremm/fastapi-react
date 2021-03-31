# App with FastAPI backend and React frontend

I built this following the blog post series called Up and Running with FastAPI by [Jeff Astor](https://www.jeffastor.com/blog/up-and-running-with-fastapi-and-docker), in order to learn more how to use authentication with FastAPI and consume the API from a React frontend.


# Docker

Had some issues with docker on Ubuntu-20.04. THe post-install instrucitons of adding user to docker group did not want to work. Finally found something that worked in [this post](https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket). Doing the regular steps and `sudo chmod 666 /var/run/docker.sock`

# Database migrations

downgrading `alembic downgrade base`
run migration `alembic upgrade head`