# CCMS-Integration-Tests

## Proteosafe Tests

![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/web-ccms-api/badge.svg)
![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/web-ccms-selenium/badge.svg)

## Workflow Tests

![workflow-integration-gnps-fast](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-integration-gnps-fast/badge.svg)
![workflow-integration-proteomics3-fast](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-integration-proteomics3-fast/badge.svg)


## Testing Workflows

In order to test workflows in a production setting, we have created a utility to do that. Specificaly, if a csv file containing test tasks is provided, then they will be run. 

The required column headers is:

1. test_id - this is the proteosafe task id to clone
1. description - this is the description to be human readable
1. regressioncountviews - this is the set of semicolon separated views that we will check for the total number of rows to be present

An example can be found [here](https://github.com/CCMS-UCSD/CCMSDeployments/blob/master/fast_test_workflow/test-integration-workflow/test_tasks.tsv). 

Additionally, we have integrated this utility into github actions but can be called manually in this fashion:

```python ./submit_test_job_batch.py --credential_username <username> --credential_password <password> --workflow_task_file test_tasks.tsv```

where the utility can be found in testing-utilities. 


## Adding your own Github Actions Tests

We rely on the continuous integration from github actions. There are several steps you'll need to accomplish:

1. Add a submodule to your repository that has a csv file described above to say which task ids you want to test
1. Create a new yml file describing the new CI job for github actions. You can copy one from the .github/workflows folder and obey the naming convention
1. Alter the path to the test_tasks.csv to yours 
1. Commit and push. It should be running once its gets into master. 