# docker-deployment-aws

# Pushing an Image to Docker Hub

To push an image to Docker Hub using the CLI, follow these steps:

1. **Create a Docker account:** If you don't already have a Docker account, you can create one for free at [https://www.docker.com/](https://www.docker.com/)

2. **Create a Docker repository:** Log in to Docker Hub and click the **Create Repository** button on the [Repositories](https://hub.docker.com/repositories) page. Give your repository a name, a description, and choose whether it should be public or private. Then click the **Create** button.


3. **Build your Docker image:** Build your Docker image using the `docker build` command. For example, to build an image from a Dockerfile named `Dockerfile` in the current directory, you would run the following command:

    ```bash
    docker build -t image-name .
    ```

4. **Tag your Docker image:** Tag your Docker image with your Docker Hub username and the name of the repository you want to push it to. For example, to tag the image you built in step 2 with the username `my-user` and the repository name `my-repo`, you would run the following command:

    ```bash
    docker tag image-name user-name/repo-name:tag-name
    ```

5. **Login to Docker Hub:** Login to Docker Hub using the `docker login` command. For example, to log in with the username `my-user` and password `my-password`, you would run the following command:

    ```bash
    docker login -u user-name -p password
    ```
	or
	```bash
	docker login -u user-name
	```

6. **Push your Docker image to Docker Hub:** Push your Docker image to Docker Hub using the `docker push` command. For example, to push the image you tagged in step 3 to Docker Hub, you would run the following command:

    ```bash
    docker push user-name/repo-name:tag-name
    ```


```bash
cd docker-deployment-aws
docker build -t docker-deployment-aws .
docker tag docker-deployment-aws maniprakashreddy/rps:latest
docker login -u <username>
docker push maniprakashreddy/rps:latest
```

# Deploying a Docker Image to AWS ECS
