# CCMS-Tests

## Proteosafe Tests

| Feature  | Server Status |
|---|---|
| GNPS/Beta/MassIVE API Tests | ![web-ccms-api](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/web-ccms-api/badge.svg) |
| GNPS/Beta/MassIVE Selenium Tests | ![web-ccms-selenium](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/web-ccms-selenium/badge.svg) |
| GNPS Workflows Fast Test | ![workflow-proteomics3-fast](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-fast/badge.svg) |
| Beta Workflows Fast Test | ![workflow-proteomics3-fast](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-proteomics3-fast/badge.svg) |


## Specific Workflow Tests

| Workflow  | GNPS Link  | Beta Link  | Unit Test | Workflow GNPS Test | Workflow Beta Test |
|---|---|---|---|---|---|
| Molecular Networking  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22METABOLOMICS-SNETS-V2%22,%22library_on_server%22:%22d.speclibs;%22%7D)  | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22METABOLOMICS-SNETS-V2%22,%22library_on_server%22:%22d.speclibs;%22%7D) | ![](https://github.com/CCMS-UCSD/GNPS_Workflows/workflows/workflow-unit-networking/badge.svg) | ![workflow-gnps-networkingv2](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-networkingv2/badge.svg) | ![workflow-beta-networkingv2](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-networkingv2/badge.svg)
| Large Scale Library Search  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLECULAR-LIBRARYSEARCH-V2%22,%22library_on_server%22:%22d.speclibs;%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLECULAR-LIBRARYSEARCH-V2%22,%22library_on_server%22:%22d.speclibs;%22%7D) |---| ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-librarysearchv2/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-librarysearchv2/badge.svg)
| MASST  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22SEARCH_SINGLE_SPECTRUM%22,%22library_on_server%22:%22d.speclibs;%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22SEARCH_SINGLE_SPECTRUM%22,%22library_on_server%22:%22d.speclibs;%22%7D) |---|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-masst/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-masst/badge.svg)
| Feature-Based Molecular Networking  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22FEATURE-BASED-MOLECULAR-NETWORKING%22,%22library_on_server%22:%22d.speclibs;%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22FEATURE-BASED-MOLECULAR-NETWORKING%22,%22library_on_server%22:%22d.speclibs;%22%7D) |![](https://github.com/CCMS-UCSD/GNPS_Workflows/workflows/workflow-unit-fbmn/badge.svg)| ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-fbmn/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-fbmn/badge.svg)
| MS2LDA Motif DB  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MS2LDA_MOTIFDB%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MS2LDA_MOTIFDB%22%7D) |---|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| MolNetEnhancer/MetaboDistTree  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLNETENHANCER%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLNETENHANCER%22%7D) |![](https://github.com/CCMS-UCSD/GNPS_Workflows/workflows/workflow-unit-molnet/badge.svg)|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| MSMS-Chooser  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MSMS-CHOOSER%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MSMS-CHOOSER%22%7D) |---|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| OpenMS Feature Detector for FBMN - Future Feature  | [Workflow]()   | [Workflow]() |---|
| MSHub-GC Deconvolution  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B"workflow":"MSHUB-GC"%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B"workflow":"MSHUB-GC"%7D) |![](https://github.com/CCMS-UCSD/GNPS_Workflows/workflows/workflow-unit-gc-mshub/badge.svg)|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| Library Search/Molecular Networking GC  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLECULAR-LIBRARYSEARCH-GC%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLECULAR-LIBRARYSEARCH-GC%22%7D) |![](https://github.com/CCMS-UCSD/GNPS_Workflows/workflows/workflow-unit-gc-networking/badge.svg)|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| Merge Polarity Networks  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MERGE_NETWORKS_POLARITY%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MERGE_NETWORKS_POLARITY%22%7D) | ![](https://github.com/mwang87/MergePolarity/workflows/unit-test/badge.svg) |
| Microbiome-Metabolomics Association - mmvec  | [Workflow - Inactive](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MMVEC%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MMVEC%22%7D) |---|
| Sirius - Bocker Lab | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22SIRIUS%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22SIRIUS%22%7D) |---|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| Qemistree | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22QEMISTREE%22%7D)   | [Workflow](https://proteomics2.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22QEMISTREE%22%7D) |---|![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-misc/badge.svg) | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-beta-misc/badge.svg)
| Legacy Networking  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22METABOLOMICS-SNETS%22,%22library_on_server%22:%22d.speclibs;%22%7D)  | --- | --- | ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-legacynetworking/badge.svg) | 
| Legacy Library Search  | [Workflow](https://gnps.ucsd.edu/ProteoSAFe/index.jsp?params=%7B%22workflow%22:%22MOLECULAR-LIBRARYSEARCH%22,%22library_on_server%22:%22d.speclibs;%22%7D)   | --- |---| ![](https://github.com/CCMS-UCSD/CCMS-Integration-Tests/workflows/workflow-gnps-librarysearch/badge.svg) | 

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

Now we can simulate actions in github that will force the running of these actions:

```
make test-push
```

This will run most of the tests including all the workflow tests. 

```
make test-schedule
```
