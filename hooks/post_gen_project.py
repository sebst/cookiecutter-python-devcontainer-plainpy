# #!/usr/bin/env python3

# import os, random, string

# # print("Initializing Django project")


# pwd = os.getcwd()

# directory_name = '{{ cookiecutter.directory_name }}'
# container_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
# service_name = '{{ cookiecutter.service_name }}'

# # Build container, run with mount, startproject

# # os.chdir(os.path.join(pwd, '.devcontainer'))
# # os.system("docker build -t %s -f Dockerfile.dev .."%(container_name))
# # os.system("docker run -v %s:/usr/src/app %s /root/.poetry/bin/poetry run django-admin startproject %s"%(pwd, container_name, service_name))
# # os.system("docker image rm %s --force"%(container_name))

# # Initialize git repository on new project

# os.chdir(pwd)
# # os.system("git init")


# print("Done generating project…")


# # print("Starting VSCode…")
# # os.chdir(pwd)
# # os.system("code .")