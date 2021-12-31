FLAGS = -O0
FLAGS_RELEASE = -Ofast
debug : 
	@echo "Running checks"

checks : 
	xargs -a files -I {} sh -c "echo -n Checking file {}: && [ -f {} ] && echo Passed || echo Failed"