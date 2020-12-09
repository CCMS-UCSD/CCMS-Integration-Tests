-include Makefile.credentials

test-push:
	act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-schedule:
	act schedule -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

#######################
# Individual Targets
#######################

## API targets
test-api:
	act -j api-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}



## Selenium targets
test-selenium-result-proteomics:
	act -j result-proteomics-selenium -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -b -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-selenium-input-forms:
	act -j input-forms-selenium -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -b -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}



## Workflow Targets
test-workflow-beta-fbmn:
	act -j workflow-beta-fbmn-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-library:
	act -j workflow-beta-library-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-masst:
	act -j workflow-beta-masst-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-misc:
	act -j workflow-beta-misc-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD} -b

test-workflow-beta-qemistree:
	act -j workflow-beta-qemistree-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD} -b	

test-workflow-beta-networking:
	act -j workflow-beta-networking-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-gc:
	act -j workflow-beta-gc-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-workflow-beta-mergepolarity:
	act -j workflow-beta-mergepolarity-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-ms2lda:
	act -j workflow-beta-ms2lda-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}


test-workflow-gnps-fbmn:
	act -j workflow-gnps-fbmn-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-gnps-library:
	act -j workflow-gnps-library-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-gnps-masst:
	act -j workflow-gnps-masst-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-gnps-misc:
	act -j workflow-gnps-misc-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-gnps-networking:
	act -j workflow-gnps-networking-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}


## Manual Workflow Test outside of Act

test-manual-gnps-all: test-manual-gnps-fast test-manual-gnps-networking test-manual-gnps-fbmn test-manual-gnps-library test-manual-gnps-masst test-manual-gnps-gc test-manual-gnps-mergepolarity test-manual-gnps-qemistree test-manual-gnps-misc

test-manual-gnps-fast:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file CCMSDeployments/fast_test_workflow/test-integration-workflow/test_tasks.tsv

test-manual-gnps-networking:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/metabolomics-snets-v2/test-integration-workflow/test_tasks.csv \

test-manual-gnps-fbmn:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/feature-based-molecular-networking/test-integration-workflow/test_tasks.csv \

test-manual-gnps-library:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/molecular-librarysearch-v2/test-integration-workflow/test_tasks.csv \

test-manual-gnps-masst:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/search_single_spectrum/test-integration-workflow/test_tasks.csv \

test-manual-gnps-gc:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/molecular-librarysearch-gc/test-integration-workflow/test_tasks.csv

test-manual-gnps-mergepolarity:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/merge_networks_polarity/test-integration-workflow/test_tasks.csv

test-manual-gnps-qemistree:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/qemistree/test-integration-workflow/test_tasks.csv

test-manual-gnps-misc:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server gnps.ucsd.edu \
	--workflow_task_file GNPS_Workflows/workflow-integration-misc-tests/test_tasks.csv


# Beta

test-manual-beta-all: test-manual-beta-fast test-manual-beta-networking test-manual-beta-fbmn test-manual-beta-library test-manual-beta-masst test-manual-beta-gc test-manual-beta-mergepolarity test-manual-beta-qemistree test-manual-beta-misc

test-manual-beta-fast:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file CCMSDeployments/fast_test_workflow/test-integration-workflow/test_tasks.tsv


test-manual-beta-networking:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/metabolomics-snets-v2/test-integration-workflow/test_tasks.csv \

test-manual-beta-fbmn:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/feature-based-molecular-networking/test-integration-workflow/test_tasks.csv \

test-manual-beta-library:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/molecular-librarysearch-v2/test-integration-workflow/test_tasks.csv \

test-manual-beta-masst:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/search_single_spectrum/test-integration-workflow/test_tasks.csv \

test-manual-beta-gc:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/molecular-librarysearch-gc/test-integration-workflow/test_tasks.csv

test-manual-beta-mergepolarity:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/merge_networks_polarity/test-integration-workflow/test_tasks.csv

test-manual-beta-qemistree:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/qemistree/test-integration-workflow/test_tasks.csv

test-manual-beta-misc:
	python workflow_integration/submit_test_job_batch.py \
	--credential_username ${CCMS_TESTUSER_USERNAME} \
	--credential_password ${CCMS_TESTUSER_PASSWORD} \
	--workflow_version ${WORKFLOW_VERSION} \
	--credential_server proteomics3.ucsd.edu \
	--workflow_task_file GNPS_Workflows/workflow-integration-misc-tests/test_tasks.csv