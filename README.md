# Code Scanning Python Tutorial

Welcome to the Code Scanning Python Tutorial! This tutorial will take you through how to set up Github Advanced Security: Code Scanning as well as interpret results that it may find. The following repository contains SQL injection vulnerability for demonstration purpose.

## Introduction

Code scanning is a feature that you use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Any problems identified by the analysis are shown in GitHub.

You can use code scanning with CodeQL, a semantic code analysis engine. CodeQL treats code as data, allowing you to find potential vulnerabilities in your code with greater confidence than traditional static analyzers.

This tutorial with use CodeQL Analysis with Code Scanning in order to search for vulnerabilities within your code. 

## Instructions

<details>
<summary>Fork this repo</summary>
<p> 
  
Begin by [forking this repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

NOTE: Make sure you uncheck "Copy the `main` branch only"

<img src="images/17-fork-repo.png" width="70%"/>

</p>

</details>

<details>
<summary>Enable Code Scanning</summary>
<p> 

#### Security tab

Click on the `Security` tab.


<img src="images/00-repo-security-tab.png" width="70%"/>

#### Set up code scanning

Click `Set up code scanning`.

<img src="images/01-repo-secruity-setup-code-scanning.png" width="70%"/>

#### Setup Workflow

Click the `Setup this workflow` button by CodeQL Analysis.

<img src="images/02-repo-security-setup-codeql-workflow.png" width="70%"/>

This will create a GitHub Actions Workflow file with CodeQL already set up. Since Python is an interpreted language you do not need to add any additional compile flags. See the [documentation](https://docs.github.com/en/free-pro-team@latest/github/finding-security-vulnerabilities-and-errors-in-your-code/running-codeql-code-scanning-in-your-ci-system) if you would like to configure CodeQL Analysis with a 3rd party CI system instead of using GitHub Actions.
</p>
</details>

<details>
  
<summary>Actions Workflow file</summary>
<p>

#### Actions Workflow

The Actions Workflow file contains a number of different sections including:
1. Checking out the repository
2. Initializing the CodeQL Action
3. Running the CodeQL Analysis

<img src="images/03-actions-sample-workflow.png" width="80%"/>

Click `Start Commit` -> `Commit this file` to commit the changes to _main_ branch.
</p>
</details>

<details>
  
<summary>Workflow triggers</summary>
<p>

#### Workflow triggers

There are a [number of events](https://docs.github.com/en/free-pro-team@latest/actions/reference/events-that-trigger-workflows) that can trigger a GitHub Actions workflow. In this example, the workflow will be triggered on

<img src="images/04-actions-sample-events.png" width="50%"/>

- push to _main_ branch
- pull request to merge to _main_ branch
- on schedule, at 6:33 every Thursday

Setting up the new CodeQL workflow and committing it to _main_ branch in the step above will trigger the scan.

</p>
</details>


<details>
<summary>GitHub Actions Progress</summary>

<p>
 
#### GitHub Actions Progress

Click `Actions` tab -> `CodeQL`

Click the specific workflow run. You can view the progress of the Workflow run until the analysis completes.

<img src="images/05-actions-completed.png" width="80%"/>

</p>
</details>

<details>
<summary>Security Issues</summary>
<p>
  
Once the Workflow has completed, click the `Security` tab -> ` Code Scanning Alerts`. An security alert "Query built from user-controlled sources" should be visible.

#### Security Alert View

Clicking on the security alert will provide details about the security alert including: <br/>
<ul>
<li>A description of the issue </li>
<li>A tag to the CWE that it is connected to as well as the type of alert (Error, Warning, Note)</li>
<li>The line of code that triggered the security alert</li>
<li>The ability to dismiss the alert depending on certain conditions (`False positive`? `Won't fix`? `Used in tests`?)</li>
</ul>
<img src="images/06-security-codeql-alert.png" width="80%"/>

#### Security Alert Description

Click `Show more` to view a full desciption of the alert including examples and links to additional information.

<img src="images/07-security-codeql-show-more.png" width="80%"/>

#### Security Full Description

<img width="80%" src="images/08-security-codeql-full-desc.png">

</p>
</details>

<details>
<summary>Show Paths</summary>
<p>

#### Show Paths Button

CodeQL Analysis is able to trace the dataflow path from source to sink and gives you the ability to view the path traversal within the alert.

Click `show paths` in order to see the dataflow path that resulted in this alert.

<img src="images/09-security-codeql-show-paths.png" width="80%"/>

#### Show Paths View

<img src="images/10-security-codeql-show-paths-details.png" width="80%"/>

</p>
</details>

<details>
<p>  
  
<summary>Fix the Security Alert</summary>

In order to fix this specific alert, we will need to ensure parameters used in the SQL query is validated and sanitized.

Click on the `Code` tab and [Edit](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/editing-files-in-your-repository) the file [`routes.py`](./server/routes.py) in the `server` folder, replace the content with the file [`fixme`](./fixme).

<img src="images/11-fix-source-code.png" width="30%"/>

Click `Create a new branch for this commit and start a pull request`, name the branch `fix-sql-injection`, and create the Pull Request.

#### Pull Request Status Check

In the Pull Request, you will notice that the CodeQL Analysis has started as a status check. Wait until it completes.

<img src="images/12-fix-pr-in-progress.png" width="80%"/>

#### Security Alert Details

After the Workflow has completed click on `Details` by the `Code Scanning Results / CodeQL` status check. 

<img src="images/13-fix-pr-done.png" width="80%"/>

#### Fixed Alert

Notice that Code Scanning has detected that this Pull Request will fix the SQL injection vulnerability that was detected before.

<img src="images/14-fix-detail.png" width="80%"/>

Merge the Pull Request. After the Pull Request has been merged, another Workflow will kick off to scan the repository for any vulnerabilties. 

#### Closed Security Alerts

After the final Workflow has completed, navigate back to the `Security` tab and click `Closed`. Notice that the **Query built from user-controlled sources** security alert now shows up as a closed issue.

<img src="images/15-fixed-alert.png" width="80%"/>

#### Traceability

Click on the security alert and notice that it details when the fix was made, by whom, and the specific commit. This provides full traceability to detail when and how a security alert was fixed and exactly what was changed to remediate the issue.

<img src="images/16-fix-history.png" width="80%"/>

</p>
</details>

<details>
<summary>Introduce a Security Vulnerability in a PR</summary>
<p>

Now let's explore the typical developer view when introducing a vulnerability.

A branch called `new-feature` introduces a new feature but also security vulnerabilities. Open a Pull Request comparing `new-feature` to `main`:

1. Go to the Pull Request tab
2. Select "New Pull Request"
3. Create the PR with 
    - `base repository: <YOUR FORK>`
    - `head repository: <YOUR FORK>`
    - `base: main`
    - `compare: new-feature`
4. _If you don't see the `new-feature` branch, change the `head repository: octodemo/advanced-security-python`_ 

<img src="images/18-create-vulnerable-pr.png" width="80%"/>

#### Pull Request Status Check

In the Pull Request, you will notice that the CodeQL Analysis has started as a status check again. Wait until it completes.

#### Security Alert Details

After the Workflow has completed click on `Details` by the `Code Scanning Results / CodeQL` status check. 

#### Security Alert

Notice that Code Scanning has detected that this Pull Request will introduce 2 medium-severity vulnerabilties

<img src="images/19-vulnerabiltliy-detail.png" width="80%"/>

#### 'Files Changed' tab

Click on the "Files Changed" tab of the PR. Scroll down and notice the Advanced Security annotations for new vulnerabilities.

You have the ability to dismiss, dive deeper into, or comment on these alerts directly from here.

<img src="images/20-files-changed-vulnerabilities.png" width="80%"/>

As a developer, this is where you would be interacting with Code Scanning

</details>
  
## Next Steps

Ready to talk about advanced security features for GitHub Enterprise? [Contact Sales](https://enterprise.github.com/contact) for more information!

Check out [GitHub's Security feature page](https://github.com/features/security) for more security features embedded into GitHub.

Check out the Code Scanning [documentation](https://docs.github.com/en/free-pro-team@latest/github/finding-security-vulnerabilities-and-errors-in-your-code/about-code-scanning) for additional configuration options and technical details.

