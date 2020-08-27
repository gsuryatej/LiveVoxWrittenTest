We can divide the list of hosts into groups in our inventory file using grouping concept and group of groups concept in ansible.

For example [oracle] [mysql] are two separate groups for oracle hosts and mysql hosts in our inventory file.

we can group them as 
[database:children]
oracle
mysql

Now, for this scenario I have created hosts file with two different groups one as db and other as app.

Configuartion parameters mentioned in the question can be retrived with the help of setup module in ansible.

setup module is used to gather facts or information like OS family,CPU,RAM etc.,

There are predefined facts which we have used for this scenario. If required we can also create our own custom facts and use them.

Process to create custom facts:
 
 1. create /etc/ansible/facts.d on Managed nodes. (Assuming ansible at /etc)
 2. inside facts.d place one or more custom facts files(.sh,.py) with extension as ".fact".
 3. output of the fact file should be json.
 4. fact file should be given executable permission.

We can validate the parameters with "assert" module and print success msg or fail msg based on the assertion.