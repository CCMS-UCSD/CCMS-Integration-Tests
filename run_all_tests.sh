#!/bin/bash

python --version

#cd api_tests && nose2 -v && cd ..

cd selenium_tests/result_views && export SERVER_URL="https://gnps.ucsd.edu" && nose2 -v && cd ../..
cd selenium_tests/result_views && export SERVER_URL="https://proteomics2.ucsd.edu" && nose2 -v && cd ../..
cd selenium_tests/result_views && export SERVER_URL="https://proteomics3.ucsd.edu" && nose2 -v && cd ../..
cd selenium_tests/input_form && export SERVER_URL="https://gnps.ucsd.edu" && nose2 -v && cd ../..
cd selenium_tests/input_form && export SERVER_URL="https://proteomics2.ucsd.edu" && nose2 -v && cd ../..
cd selenium_tests/input_form && export SERVER_URL="https://proteomics3.ucsd.edu" && nose2 -v && cd ../..