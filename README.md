# Boto3-EC2-VPC

VPC and EC3 setting up using Boto 3. The configuration looks like this:

![Scheme](https://github.com/ederfduran/Boto3-EC2-VPC/blob/master/ec2-vpc.png)

#### Requirements:
* Python 3.6
* Boto3
* AWS CLI
* AWS account


#### Content Includes :

* VPC creation
  * Internet Gateway creation(IGW)
  * Attached IGW to VPC
  * Create a Public Subnet
  * Create Route Table for public Routes
  * Add IGW Route to Route table
  * Associate Public Subnet with Public Route Table
  * Allowed Ip Auto-assign on Public Subnet
  * Create Private Subnet(with default route table)
* EC2
  * Create a Key pair for private and public EC2 instances
  * Create 2 Segurity group(for private/public)
  * Simple Start-up Sript for our Public EC2 Instance
  * Describe EC2 instance
  * Modify EC2 instance
  * Stop EC2 instance
  * Terminate EC2 instace
  

For further Information you can always check boto3 documentation
[Boto3 doc](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) 
