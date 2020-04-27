# CCMS-Tests

## Proteosafe Tests

| Feature  | Server Status |
|---|---|
| GNPS/Beta/MassIVE API Tests | ![web-ccms-api](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/web-ccms-api/badge.svg) |
| GNPS/Beta/MassIVE Selenium Tests | ![web-ccms-selenium](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/web-ccms-selenium/badge.svg) |
| GNPS Workflows Fast Test | ![workflow-proteomics3-fast](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-fast/badge.svg) |
| Beta Workflows Fast Test | ![workflow-proteomics3-fast](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-proteomics3-fast/badge.svg) |
| GNPS Full Workflows Test | ![workflow-gnps](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps/badge.svg) |
| Beta Full Workflows Test | ![workflow-beta](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta/badge.svg) |


## Selenium Testing

In order to have selenium tests run, we recommend placing them in the appropriate locations depending on what they are testing:

```
selenium_tests/input_form/
```

and 

```
selenium_tests/result_views/
```

These two locations are called automatically with ```nose2``` with github actions. To run them manually, see below. 


## Testing Workflows

In order to test workflows in a production setting, we have created a utility to do that. Specificaly, if a csv file containing test tasks is provided, then they will be run. 

The required column headers is:

1. test_id - this is the proteosafe task id to clone
1. description - this is the description to be human readable
1. regressioncountviews - this is the set of semicolon separated views that we will check for the total number of rows to be present

An example can be found [here](https://github.com/CCMS-UCSD/CCMSDeployments/blob/master/fast_test_workflow/test-workflow/test_tasks.tsv). 

Additionally, we have integrated this utility into github actions but can be called manually in this fashion:

```python ./submit_test_job_batch.py --credential_username <username> --credential_password <password> --workflow_task_file test_tasks.tsv```

where the utility can be found in testing-utilities. 


### Adding your own Github Actions Tests for Workflows

We rely on the continuous integration from github actions. There are several steps you'll need to accomplish:

1. Add a submodule to your repository that has a csv file described above to say which task ids you want to test
1. Create a new yml file describing the new CI job for github actions. You can copy one from the .github/workflows folder and obey the naming convention
1. Alter the path to the test_tasks.csv to yours 
1. Commit and push. It should be running once its gets into master
1. Add badge to readme

## Actions Run Schedule

We run the tests once every 24 hours. Additionally, we enable a way to manually enable all of them to run. This is used when there is new code that will want to be deployed. 
Please create a pull request and then only admins can lock and then unlock the conversation. This unlock operation triggers the workflows to run. 

## Manually Running API/Selenium Tests

To manually run these tests, we will be using nose2. You will have to either:

1. Create a Makefile.credentials file that includes CCMS_TESTUSER_USERNAME and CCMS_TESTUSER_PASSWORD
2. Explicitly set the CCMS_TESTUSER_USERNAME and CCMS_TESTUSER_PASSWORD environment variables. 

We will use the act program found [here](https://github.com/nektos/act). 

To simulate a push of commits to the repo (which will include Selenium and API tests), run this command:
```
make test-push
```
 
To run nearly everything (including workflow tests), run this command: 
```
make test-schedule
```
