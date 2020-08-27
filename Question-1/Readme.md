According to the scenario, there are multiple hosts on multiple environments.

I am assuming as dev and prod environments.

So, mutli-stage ansible setup is required for this scenario. I have created environments dev and prod with their own group_vars,host_vars and inventory files.

The recommended approach is to work with multistage environments by completely separating each operating environment. Instead of maintaining all of your hosts within a single inventory file, an inventory is maintained for each of your individual environments. Separate group_vars,host_vars directories are also maintained.


Sharing variable files across environments can be accomplished by using the ‘vars_files’ statement in the playbook.

Modules used to achieve are:

1. 'git' module to clone the repo

2. 'copy' module to copy the configuration file to /etc with changing ownership and mode.

3. 'lineinfile' module to update the configuartion file with databaseServer based on the environment we deploy. However, we can also    use 'replace' module to achieve this task.

4. To Update 'DataBaseServer' value in configuartion file dynamically we are using 
     {{ hostvars['database']["hostname"] }} -> this will fetch the hostname value of database host(This is mentioned in inventory file)

Note: ansible.cfg is currently defaults to dev environment.


export ENV before running the playbook and based on the env it will fetch the hosts and its variables and specific inventory file.

ansible-playbook -i "environment/$ENV" --extra-vars "env=$ENV" config-provision.yml


The folder structure looks as below:

![Multi-stageAnsibleSetup](https://user-images.githubusercontent.com/49281318/91426870-b3e4ec80-e87a-11ea-860d-7523b9536031.PNG)
