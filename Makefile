-include Makefile.credentials

test-push:
	act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-schedule:
	act schedule -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

# Individual targets
test-api:
	act -j api-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-selenium:
	act -j selenium-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -b -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-workflow-beta-fbmn:
	act -j workflow-beta-fbmn-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-library:
	act -j workflow-beta-library-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-masst:
	act -j workflow-beta-masst-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-misc:
	act -j workflow-beta-misc-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
test-workflow-beta-networking:
	act -j workflow-beta-networking-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}
	
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
	