Basically, Ansible will accept any kind of executable files(.sh,.py). So, we can build our own dynamic inventory however we like as long as we can pass it to Ansible as JSON.

Ansible will call it with the argument --list when we run as example "ansible all -i <inventory_file> -m ping".

Ansible expects a dictionary of groups (ie.,each group having a list of hosts and group variables in the group's vars dictionary) and a _meta dictionary stores host variables for all hosts individually (ie.,inside hostvars).

Note:
When we return a _meta dictionary in our inventory script, Ansible stores that data in its cache and doesn't call your inventory script N times for all the hosts in the inventory.

We can also implement to fetch host variables per host with "--host [hostname]" arguments but it's often faster and easier to simply return al the variables in the first call.

Implementation:

In this scenario, I assumed there is a table in oracle db namely 'host_vars' with host_name,var_name,var_value as columns.

configuration/connection string values maintained in a separate module as config.py and import it as config in script to utilise it.

To connect with oracle db used 'cx_Oracle' module.

To use this inventory, move the two .py files to ansible hosts directory and give executable permissions and run it like static inventory format (ansible all -i <inventory_file> -m ping).
