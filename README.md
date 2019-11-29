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
  * Create Route Table for public Rou*tes
  * Add IGW Route to Route table
  * Associate Public Subnet with Public Route Table
  * Allowed Ip Auto-assign on Public Subnet
  * Create Private Subnet
* EC2
  * Create a Key pair for private and public EC2 instances
  * Create 2 Segurity group(for private/public)
  * Simple Start-up Sript for our Public EC2 Instance
  
