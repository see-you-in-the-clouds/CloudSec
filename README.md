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

While the traditional use of a Liner is to ensure code-related errors, enforcing coding standards not only to improve the quality of the code as is, but also ensure the interoperability between the different actors that interact with the code, as now or in the future.

In this case, the application of the concept presents some shortcomings, both for the user at use time, and the person who develops this solution.

### Solution Caveats

A better implementation would be to pipe and API call over a Infrastructure resource (like a simple gcloud compute describe) at the end the more stiff and predectible outputs are could potentially allow a better backend logic, more tailored rules. Which at the end would put this solution closer to the [GCPDiag](https://gcpdiag.dev/) tool, which is what has been used as a reference.

### Future Improvements

This could potentially be expanded to a bigger functionality.
  1. Storing the JSON and report could eventually grow an internal knowledge to add/improve detection rules
     1. I would consider a GCS as Cloud Run Volume for this Step (Which could eventually also handle PII concerns with DLP)
  2. Gather volumetric data of common issues Cloud operators / Dev recurrently fall into, to later educate Devs / Cloud Operators or decide if its worth to apply actions at bigger scale (Organizational Policies)
     1. In this case I would consider a Cloud SQL In case refactoring the code to keep track of the volumetric data.
   
### Concept

#### Platform
The problem statement directly refers to build something aiming for solution and innovation, at first glance it seems a **Serverless - Cloud Run**  could fulfill the requirements, while keeping costs down, Without the need of persistent storage and while code being lean there is no reason to think about bigger implementation, especially as it directly mentions that only one tool must be used.

At the same time the Issue Statement requires to upload the Code in GitHub, Cloud Run allows Github as Container source, and DockerFile as Kickstart point.

#### Functionality
Thinking about similar solutions to better understand "how others have implemented similar ideas" the first thing that comes to mind is [GCPDiag](https://gcpdiag.dev/), where the idea is based on.

## How to set it up

### Fork
For the reprository ![fork](/readme/1.png)
###
