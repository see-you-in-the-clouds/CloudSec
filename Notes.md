## Senior Gaming Cloud Engineer Pre-Screen Code Assessment

### Problem Statement
You are tasked with developing a web application that helps users identify and mitigate potential security vulnerabilities in their cloud infrastructure. The application should allow users to upload a configuration file (in JSON format) that describes their cloud resources and security settings. The application will then analyze the configuration and provide a report highlighting any security issues and recommendations for improvement.

Select a GCP centric technology stack to complete this assessment. Please document any assumptions and necessary configurations around this web application clearly. During project submission, provide a link to the GitHub repository where your code is located. It is recommended not to spend more than 1 day on this assessment.
Solution towards innovation and simplicity and prepare to present your understanding of cloud security principles, along with a thorough comprehension of your web application, clean coding practices, and clarity of documentation.

#### Requirements
- **Technology Stack**: Using GCP free tier, and one of these services, GCP Compute Engine, Google Kubernetes Engine, App Engine, Cloud Run, or Google Cloud Deployment Manager. Deploy an app that scans JSON configuration files and identifies security issues within that configuration file.

- **File Upload**: The web app should have a feature that allows users to upload a JSON file containing their cloud configuration.

- **Configuration Analysis**: The application should parse the JSON file and analyze the configuration for common security issues.

- **Report Generation**: After analyzing the configuration, the application should generate a security report that includes:
  1. A summary of the identified security issues
  2. Detailed descriptions of each issue
  3. Recommendations for mitigating each issue

- **Documentation**: Include a README file in your project that explains how to set up and run your solution. This should be clear and detailed and include relevant screenshots demonstrating the functionalities.  


### Issue Understanding.

The concept behind the tool is a linter (***Static Code Analyzer***) maybe not in the classic sense (as JSON are not executable files), but the concept remains the same, checking the parsed code against a set of pre-defined rules.

### Concept

#### Platform
The problem statement directly refers to build something aiming for solution and innovation, at first glance it seems a **Serverless** solution could be the best option, GKE Autopilot could become a solution if this webapp belongs to a broader platform but as standalone solution App Engine and/or Cloud Run is what makes the most sense. Researching a bit how to convert this into a functional solution this SkillBoost outlines the idea [Deploying a Python Flask Web Application to App Engine Flexible](https://www.cloudskillsboost.google/focuses/3334?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=42350417)

#### Functionality
Thinking about similar solutions to better understand "how others have implemented similar ideas" the first thing that comes to mind is [GCPDiag](https://gcpdiag.dev/).

