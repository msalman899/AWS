Provided a list of IPs with descriptions and a security group name, create a lambda that updates the security group with ingress rules for the IPs & descriptions.
Ensure that IAM permissions for the lambda should only include permissions needed to execute the task.
Make assumptions as necessary, but please include a section for assumptions in your solution.
Tools: Terraform, Python/any other language
SAMPLE:

+-------------+------------------+------+
|     IP      |   Description    | Port |
+-------------+------------------+------+
| 192.168.1.2 | karachi-office   | 443  |
| 192.168.9.2 | islamabad-office | 443  |
+-------------+------------------+------+
Security Group Name: my-vpc-https-sg


#####
- terraform init
- terraform plan
- terraform apply

