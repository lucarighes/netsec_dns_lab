#!/bin/bash

#clean cache
rndc flush
rndc reload

echo "The cash is clean now!" 
