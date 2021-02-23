#! /bin/bash

cd /detector
ARGS=$@

param=$(printenv 'METHOD')
# check for openvino
if [[ ! -z "$INTEL_OPENVINO_DIR" ]]; then 
    source $INTEL_OPENVINO_DIR/bin/setupvars.sh
    ARGS="$ARGS --device MYRIAD --detector openvino"
fi

if [ -z "$param" ];then
	param="$param"
else
	param="--$param"
fi 

python3 $ARGS $param